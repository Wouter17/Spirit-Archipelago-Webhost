import re  # noqa: N999
from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar

from Options import (
    Choice,
    DefaultOnToggle,
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
        return Spirit(spirit_name)
    except ValueError:
        return None


def parse_boss_option(entry: str) -> tuple[Adversary, int, Spirit | Aspect]:
    boss_raw, spirit_raw, difficulty_raw = [
        x.strip() for x in entry.split("|")]
    try:
        adversary = Adversary(boss_raw)
    except ValueError:
        raise Exception(
            f"Adversary must be an Adversary in '{entry}', got '{boss_raw}'. Please contact a developer.") from None
    try:
        difficulty = int(difficulty_raw)
    except ValueError:
        raise Exception(
            f"Difficulty must be an integer in '{entry}', got '{difficulty_raw}'.\
                  Please contact a developer.") from None
    try:
        spirit_match = re.fullmatch(
            r"\s*([^()]+?)\s*(?:\(([^()]+)\))?\s*", spirit_raw)
        if not spirit_match:
            raise Exception(f"No match in {spirit_raw}")
        spirit_name, aspect_name = spirit_match.groups()
        if aspect_name is not None:
            spirit = Aspect(aspect_name)
        else:
            spirit = Spirit(spirit_name)
    except ValueError:
        raise Exception(
            f"Spirit must be an Spirit in '{entry}', got '{spirit_raw}'. Please contact a developer.") from None
    return adversary, difficulty, spirit


class LocationBalancingMode(IntEnum):
    disabled = 0
    compromise = 1
    full = 2


class DeathLinkMode(IntEnum):
    disabled = 0
    lost_game = 1


class SpiritIslandOnToggle(DefaultOnToggle):
    @property
    def result(self) -> bool:
        return bool(self.value)


class SpiritIslandToggle(Toggle):
    @property
    def result(self) -> bool:
        return bool(self.value)


class BossGoals(OptionSet):
    """Which spirits, need to defeat which adversaries, at what difficulty, to have completed the game.

        Defeating an advisary at a difficulty higher than the target difficulty also counts as defeating them on a lower difficulty.
        Selecting multiple difficulties for the same spirit + difficulty will have the lower values ignored.
        Selecting many goals may introduce a lot of useless filler items.
    """
    display_name = "Victory Goals"
    valid_keys = sorted([f"{adv.value} | {spirit.full_name} | {diff}"
                  for adv in Adversary
                  for spirit in list(Spirit) + list(Aspect)
                  for diff in range(0, 7)])


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
    display_name = "Enabled spirit unique checks"
    default: ClassVar[set[str]] = set()
    valid_keys = sorted([s.full_name for s in Spirit] + [a.full_name for a in Aspect])


class EnabledExpansions(OptionSet):
    """Which expansions should be included when creating checks for playing cards"""
    display_name = "Card unlocking expansions"
    default: ClassVar[set[str]] = {ContentSource.BASE.value}
    valid_keys = [cs.value for cs in ContentSource]  # noqa: RUF012

class LockNotInPlayCards(SpiritIslandOnToggle):
    """Remove minors and majors not selected in 'Card unlocking expansions' from the game"""
    display_name = "Remove not in play cards"

si_option_groups = [
    OptionGroup("Energy and Cardplays", [
        StartingEnergy, MaxEnergy, StartingCardplays, MaxCardplays
    ]),
    OptionGroup("Unlocks", [
        EnabledExpansions, SpiritPlayOptionSet, LockNotInPlayCards
    ])
]


@dataclass
class SpiritIslandOptions(PerGameCommonOptions):
    goals: BossGoals
    enabled_expansions: EnabledExpansions
    spirit_play: SpiritPlayOptionSet
    deathlink: DeathLink
    starting_energy: StartingEnergy
    max_energy: MaxEnergy
    starting_cardplays: StartingCardplays
    max_cardplays: MaxCardplays
    lock_not_in_play_cards: LockNotInPlayCards
