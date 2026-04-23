import logging  # noqa: N999
import re
from dataclasses import dataclass
from enum import IntEnum
from random import Random
from typing import ClassVar, Literal

from schema import And, Optional, Or, Schema

from Options import (
    Choice,
    DefaultOnToggle,
    OptionDict,
    OptionError,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    Range,
    Toggle,
)

from .SpiritIslandLevels import Adversary, Aspect, ContentSource, Spirit


def map_str_to_spirit_aspect(spirit_raw: str) -> Spirit | Aspect | None:
    spirit_match = re.fullmatch(
        r"\s*([^()]+?)\s*(?:\(([^()]+)\))?\s*", spirit_raw)
    if not spirit_match:
        return None
    spirit_name, aspect_name = spirit_match.groups()
    try:
        if aspect_name is not None:
            return Aspect(aspect_name)
        if spirit_name == "Any":
            return None
        return Spirit(spirit_name)
    except ValueError as err:
        raise OptionError(
            f"{spirit_raw} is not a valid spirit option") from err


def parse_boss_option(entry: str) -> tuple[Adversary, int, Spirit | Aspect | None]:
    boss_raw, spirit_raw, difficulty_raw = [
        x.strip() for x in entry.split("|")]

    try:
        adversary = Adversary(boss_raw)
    except ValueError as err:
        raise OptionError(
            f"Adversary must be an Adversary in '{entry}', got '{boss_raw}'.") from err

    try:
        difficulty = int(difficulty_raw)
    except ValueError as err:
        raise OptionError(
            f"Level must be an integer in '{entry}', got '{difficulty_raw}'") from err

    try:
        spirit = map_str_to_spirit_aspect(spirit_raw)
    except OptionError as err:
        raise OptionError(
            f"Spirit must be an Spirit in '{entry}', got '{spirit_raw}'") from err
    return adversary, difficulty, spirit


class LocationBalancingMode(IntEnum):
    disabled = 0
    compromise = 1
    full = 2


class DeathLinkMode(IntEnum):
    disabled = 0
    lost_game = 1

class HintCardsMode(IntEnum):
    disabled = 0
    on_hover = 1
    always = 2

class SpiritIslandOnToggle(DefaultOnToggle):
    @property
    def result(self) -> bool:
        return bool(self.value)


class SpiritIslandToggle(Toggle):
    @property
    def result(self) -> bool:
        return bool(self.value)


class BossGoals(OptionSet):
    """Which spirits, need to defeat which adversaries, at what level, to have completed the game.

        Defeating an adversary at a level higher than the target level also counts as defeating them on a lower level.
        Selecting multiple levels for the same spirit + adversary will have the lower values ignored.
        Selecting many goals may introduce a lot of useless filler items.
    """
    display_name = "Victory Goals"
    valid_keys = sorted([f"{adv.value} | {spirit_name} | {diff}"
                         for adv in Adversary
                         for spirit_name in (*(spirit.full_name for spirit in list(Spirit) + list(Aspect)), "Any")
                         for diff in range(0, 7)])

    @property
    def parsed(self) -> list[tuple[Adversary, int, Spirit | Aspect | None]]:
        return [parse_boss_option(line) for line in self.value]


class AdvancedBossGoals(OptionDict):
    """Which spirits, need to defeat which adversaries, at what level, to have completed the game.

        This setting replaces the settings in "Victory Goals" if present.
        This setting allows you to specify the boss as an yaml in the form.
        It allows you to weight spirit selection chances.
        See the Game Page for examples.
    """
    display_name = "Advanced Victory Goals"

    Difficulty_schema = And(int, lambda n: 0 <= n <= 10)
    Adversary_schema = And(str, lambda s: s in Adversary)
    Spirit_schema = And(str, lambda s: s in [
                        n.full_name for n in list(Spirit) + list(Aspect)] + ["Any"])
    Count = And(int, lambda n: n >= 1)

    unweighted_schema: ClassVar = {
        Difficulty_schema: {
            Adversary_schema: [Spirit_schema]
        }
    }

    weighted_schema: ClassVar = {
        Optional("min"): Count,
        Optional("max"): Count,

        Difficulty_schema: {
            Adversary_schema: {
                Spirit_schema: Count
            }
        }
    }

    default: ClassVar = {}

    schema = Schema(Or(
        {},
        unweighted_schema,
        weighted_schema
    ))

    @property
    def combinations(self) -> int:
        total = 0
        for diff, advs in self.value.items():
            if diff in ("min", "max"):
                continue
            for adversary_map in advs.values():
                total += len(adversary_map)
        return total

    def verify(self, world, player_name, plando_options):
        super().verify(world, player_name, plando_options)
        if "min" in self.value:
            total = self.combinations
            if total < self.value["min"]:
                raise OptionError(f"Minimum selection set to {self.value['min']} spirits, "
                                  f"but only {total} goals are given")

        if "min" in self.value and "max" in self.value and self.value["max"] < self.value["min"]:
            raise OptionError(f"Maximum number of spirits ({self.value['max']}) "
                              f"should be larger than minimum ({self.value['min']})")

    def parsed(self, random: Random) -> None | list[tuple[Adversary, int, Spirit | Aspect | None]]:
        if self.value == {}:
            return None
        weighted_list: list[tuple[tuple[Adversary,
                                        int, Spirit | Aspect | None], int]] = []
        unweighted_list: list[tuple[Adversary,
                                    int, Spirit | Aspect | None]] = []
        min_count = 1
        max_count = None
        for diff, advs in self.value.items():
            if diff == "min":
                min_count = int(advs)
                continue
            if diff == "max":
                max_count = int(advs)
                continue
            difficulty = int(diff)
            first_spirit: list[Spirit | Aspect | Literal["Any"]] | dict[Spirit | Aspect | Literal["Any"], int] | None\
                = next(iter(advs.values()), None)
            if first_spirit is None:
                continue

            weighted = isinstance(first_spirit, dict)

            for adversary, spirit_container in advs.items():
                if weighted:
                    for spirit, weight in spirit_container.items():
                        spirit_value = None if spirit == "Any" else map_str_to_spirit_aspect(
                            spirit)
                        weighted_list.append(
                            ((Adversary(adversary), difficulty, spirit_value), weight))
                else:
                    for spirit in spirit_container:
                        spirit_value = None if spirit == "Any" else map_str_to_spirit_aspect(
                            spirit)
                        unweighted_list.append(
                            (Adversary(adversary), difficulty, spirit_value))
        if not weighted_list and not unweighted_list:
            return []
        if weighted_list:
            return self.randomized(weighted_list, random, min_count, max_count)
        return unweighted_list

    def randomized(
            self,
            lst: list[tuple[tuple[Adversary, int, Spirit | Aspect | None], int]],
            random: Random,
            min_count: int,
            max_count: int | None
    ) -> list[tuple[Adversary, int, Spirit | Aspect | None]]:
        max_spirits = self.combinations if max_count is None else max_count
        total_spirit = random.randint(min_count, max_spirits)

        keys: list[tuple[int, tuple[Adversary, int, Spirit | Aspect | None]]] = []
        for item, weight in lst:
            u = random.random()
            key = u ** (1.0 / weight)
            keys.append((key, item))

        keys.sort(key=lambda x: x[0], reverse=True)

        return [v for _, v in keys[:total_spirit]]


class StartingEnergy(Range):
    """The starting amount energy per turn offset the spirit starts with (-1 would mean you get 1 less energy per turn. 2 Would mean you get +2 energy per turn)
    """
    display_name = "Starting energy offset"
    range_start = -5
    range_end = 0
    default = 0


class MaxEnergy(Range):
    """The final amount (when all +Energy checks have been gotten) energy per turn offset the spirit ends with (-1 would mean you get 1 less energy per turn. 2 Would mean you get +2 energy per turn)

    This value needs to be higher than or equal to the starting energy offset
   """
    display_name = "Ending energy offset"
    range_start = 0
    range_end = 5
    default = 0


class StartingCardplays(Range):
    """The starting amount energy per turn offset the spirit starts with (-1 would mean you get 1 less energy per turn. 2 Would mean you get +2 energy per turn)
    """
    display_name = "Starting cardplays offset"
    range_start = -3
    range_end = 0
    default = 0


class MaxCardplays(Range):
    """The final amount (when all +Cardplay checks have been gotten) cardplays per turn offset the spirit ends with (-1 would mean you get 1 less cardplay per turn. 2 Would mean you get +2 cardplays per turn)

    This value needs to be higher than or equal to the starting cardplays offset
   """
    display_name = "Ending cardplays offset"
    range_start = 0
    range_end = 3
    default = 0


class StartingBlight(Range):
    """The starting amount blight offset the game starts with (-1 would mean you start with 1 fewer blight)
    """
    display_name = "Starting blight offset"
    range_start = -3
    range_end = 0
    default = 0


class MaxBlight(Range):
    """The final amount blight offset when all '+ Blight' check have been collected (-1 would mean you always have at least with 1 fewer blight)

    This value needs to be higher than or equal to the starting blight offset
   """
    display_name = "Ending blight offset"
    range_start = 0
    range_end = 3
    default = 0


class DeathLink(Choice):
    """DeathLink is an opt-in feature for Multiworlds where individual death events are propagated to all games with DeathLink enabled.

    - Disabled: Nothing will happen when you die or when other players trigger a death event.

    - Lost game: A DeathLink broadcast will be sent every time you lose or abbandon a game.
    """
    auto_display_name = True
    display_name = "DeathLink"
    option_disabled = DeathLinkMode.disabled.value
    option_lost_game = DeathLinkMode.lost_game.value
    default = DeathLinkMode.disabled.value


class SpiritPlayOptionSet(OptionSet):
    """For which spirits should playing unique cards earns you checks"""
    display_name = "Spirit unique checks"
    default: ClassVar[set[str]] = set()
    valid_keys = sorted([s.full_name for s in Spirit] +
                        [a.full_name for a in Aspect])


class UnlockableSpiritAspects(OptionSet):
    """Which spirits (and aspects) should be locked by default and unlockable through checks.

    To play an aspect you must first unlock its spirit.
    """
    display_name = "Unlockable spirits & aspects"
    default: ClassVar[set[str]] = set()
    valid_keys = sorted([s.full_name for s in Spirit] +
                        [a.full_name for a in Aspect])

    @property
    def spirits(self) -> list[Spirit]:
        return [s for s in map(map_str_to_spirit_aspect, self.value) if isinstance(s, Spirit)]

    @property
    def aspects(self) -> list[Aspect]:
        return [a for a in map(map_str_to_spirit_aspect, self.value) if isinstance(a, Aspect)]

    @property
    def parsed(self) -> list[Spirit | Aspect]:
        return [sa for sa in map(map_str_to_spirit_aspect, self.value) if sa is not None]


class EnabledExpansions(OptionSet):
    """Which expansions should be included when creating checks for playing cards"""
    display_name = "Card unlocking expansions"
    default: ClassVar[set[str]] = {ContentSource.BASE.value}
    valid_keys = [cs.value for cs in ContentSource]  # noqa: RUF012


class LockNotInPlayCards(SpiritIslandOnToggle):
    """Remove minors and majors not selected in 'Card unlocking expansions' from the game"""
    display_name = "Remove not in play cards"

class SpoilLocations(SpiritIslandOnToggle):
    """Display on the powercards what item they will unlock"""
    display_name = "Spoil items on cards"

class HintReceivedCards(Choice):
    """Hint cards that have been added to the deck or are in hand

    - Disabled: No hints.

    - On Hover: Whenever the card is viewed, a hint is generated for what it will unlock.

    - Always: The moment a card is received, a hint is generated for what it will unlock.
    """
    auto_display_name = True
    display_name = "Hint received cards"
    default = HintCardsMode.always.value
    option_disabled = HintCardsMode.disabled.value
    option_on_hover = HintCardsMode.on_hover.value
    option_always = HintCardsMode.always.value

class PrioritisedShuffle(SpiritIslandOnToggle):
    """When shuffling the power decks, put cards with unexplored locations on top"""
    display_name = "Prioritised Shuffle"

class RemoveCardsWhenFill(SpiritIslandToggle):
    """When the game has more locations than items, reduce the number of powercards to reduce the number of locations.

    Prevents having a lot of filler items, at the cost of losing some major and minor power cards.
    """
    display_name = "Remove cards when filling"

class SpiritShards(Range):
    """Divides the unlocks for spirits and aspects across that many items."""
    display_name = "Spirit Shards"
    default = 1
    range_start = 1
    range_end = 10

class ExtraCopiesOfSpirits(Range):
    """Adds (up to this many) extra copies of spirit and aspect unlocking items.

    Does not increase the amount of items required to unlock the spirit/aspect.
    """
    display_name = "Extra copies of spirits and aspects"
    default = 0
    range_start = 0
    range_end = 3

class ElementsFillRatio(Range):
    """What percentage of filler items (after filling with extra spirits) should be +element.

    0 means no filler items are +element.
    100 means all filler items are +element.

    Bonus elements last only a single turn.
    Fill items that are not +element, are friendly greetings that do not have an effect on the game.
    """
    display_name = "Elements Fill Ratio"
    default = 50
    range_start = 0
    range_end = 100

si_option_groups = [
    OptionGroup("Energy and Cardplays", [
        StartingEnergy, MaxEnergy, StartingCardplays, MaxCardplays, StartingBlight, MaxBlight
    ]),
    OptionGroup("Unlocks", [
        EnabledExpansions, SpiritPlayOptionSet, LockNotInPlayCards, UnlockableSpiritAspects
    ]),
    OptionGroup("Hints & Quality of Life", [
        SpoilLocations, HintReceivedCards, PrioritisedShuffle, RemoveCardsWhenFill
    ]),
    OptionGroup("Sharding & Filler", [
        SpiritShards, ExtraCopiesOfSpirits, ElementsFillRatio
    ])
]


@dataclass
class SpiritIslandOptions(PerGameCommonOptions):
    goals: BossGoals
    advanced_goals: AdvancedBossGoals

    enabled_expansions: EnabledExpansions
    spirit_play: SpiritPlayOptionSet
    spirit_aspect_locked: UnlockableSpiritAspects
    deathlink: DeathLink

    starting_energy: StartingEnergy
    max_energy: MaxEnergy
    starting_cardplays: StartingCardplays
    max_cardplays: MaxCardplays
    starting_blight: StartingBlight
    max_blight: MaxBlight

    lock_not_in_play_cards: LockNotInPlayCards
    spoil_locations: SpoilLocations
    hint_received_cards: HintReceivedCards
    prioritised_shuffle: PrioritisedShuffle
    remove_cards_when_fill: RemoveCardsWhenFill

    spirit_shards: SpiritShards
    copies_of_spirit: ExtraCopiesOfSpirits
    elements_fill_ratio: ElementsFillRatio

    def __post_init__(self):
        self.goals_parsed = None

    def parsed_goals(self, random: Random) -> list[tuple[Adversary, int, Spirit | Aspect | None]]:
        if self.goals_parsed is not None:
            return self.goals_parsed

        advanced = self.advanced_goals.parsed(random)
        simple = self.goals.parsed
        if advanced is not None:
            if simple:
                logging.warning("Spirit Island: Both advanced goals and (basic) goals have been specified: "
                                "ignoring basic goals")
            self.goals_parsed = advanced
            return advanced
        self.goals_parsed = simple
        return simple
