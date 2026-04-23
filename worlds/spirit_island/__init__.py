from collections import defaultdict
from collections.abc import Callable, Mapping
from typing import Any, TextIO

from BaseClasses import CollectionState, ItemClassification, Location, LocationProgressType, Region, Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .Items import SpiritIslandItem, filler_items, item_descriptions, item_id_to_name, item_name_groups, item_name_to_id
from .Locations import SpiritIslandLocation, defeat_with_string, si_location_id_to_name, si_location_name_to_id
from .Options import SpiritIslandOptions, map_str_to_spirit_aspect, si_option_groups
from .Presets import extra_presets
from .SpiritIslandLevels import Adversary, Aspect, CardType, ContentSource, Element, Powercard, Spirit


class SpiritIslandWeb(WebWorld):
    rich_text_options_doc = True
    option_groups = si_option_groups
    options_presets = extra_presets
    theme = "grassFlowers"

    bug_report_page = "https://github.com/wouter17/Spirit-Archipelago/issues"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Spirit Island randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["wouter17"]
    )

    tutorials = [setup_en]  # noqa: RUF012


class SpiritIslandWorld(World):
    """
    Spirit island is a boardgame where players play spirits to prevent the invaders from destroying the island.
    """

    # Autoworld API

    game = "Spirit Island"
    web = SpiritIslandWeb()
    required_client_version = (0, 3, 8)
    topology_present: bool = False

    item_name_groups = item_name_groups
    item_descriptions = item_descriptions

    item_name_to_id = item_name_to_id
    item_id_to_name = item_id_to_name

    location_id_to_name = si_location_id_to_name
    location_name_to_id = si_location_name_to_id

    options_dataclass = SpiritIslandOptions
    options: SpiritIslandOptions # pyright: ignore[reportIncompatibleVariableOverride]
    itempool: list[SpiritIslandItem]

    pre_fill_item_placement: list[tuple[Location, SpiritIslandItem]]

    # Helper Functions

    def create_item(self, name: str,
                    classification: ItemClassification = ItemClassification.progression) -> SpiritIslandItem:
        return SpiritIslandItem(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: str, classification: ItemClassification) -> SpiritIslandItem:
        return SpiritIslandItem(event, classification, None, self.player)

    def place_event(self, location_name: str, item_name: str,
                    classification: ItemClassification = ItemClassification.progression_skip_balancing):
        location: Location = self.multiworld.get_location(
            location_name, self.player)
        location.place_locked_item(
            self.create_event(item_name, classification))

    def add_region(self, region_name: str):
        region = Region(
            region_name,
            self.player,
            self.multiworld,
        )
        self.multiworld.regions.append(region)

    def connect_regions(self, source: str, target: str, rule: Callable[[CollectionState], bool] | None = None):
        source_region = self.multiworld.get_region(source, self.player)
        target_region = self.multiworld.get_region(target, self.player)
        source_region.connect(target_region, rule=rule)

    # Helper Data

    # Autoworld Hooks

    def generate_early(self):
        self.pre_fill_item_placement = []

    def create_regions(self) -> None:
        self.add_region("Menu")
        self.add_region("Island")
        self.connect_regions("Menu", "Island")

        # Unique card locations
        selected_spirits_and_aspects = [sa for sa in (map_str_to_spirit_aspect(s)
            for s in self.options.spirit_play.value) if sa is not None]
        unique_pool: defaultdict[Powercard, set[Spirit | Aspect]] = defaultdict(set)
        for spirit_aspect in selected_spirits_and_aspects:
            for unique in spirit_aspect.uniques:
                unique_pool[unique].add(spirit_aspect)

        for card, spirits in unique_pool.items():
            self.add_unique_powercard_location(card, spirits)

        # Power card locations
        enabled_sources = {ContentSource(key)
                           for key in self.options.enabled_expansions.value}
        base_card_pool = {card for card in Powercard if \
                card.expansion in enabled_sources and \
                card.card_type is not CardType.Unique}
        overlap_count = len(base_card_pool & set(unique_pool))
        card_pool = [card for card in base_card_pool if card not in unique_pool]

        # Calculate number of checks due to adversary
        max_pair: defaultdict[tuple[Adversary, Spirit | Aspect | None], int] = defaultdict(int)
        for boss, difficulty, spirit in self.options.parsed_goals(self.random):
            difficulty_offset = difficulty + 1
            key = (boss, spirit)
            if difficulty_offset > max_pair[key]:
                max_pair[key] = difficulty_offset

        # Offset for items-locations (positive if items > locations)
        gen_offset: int = abs(self.options.max_energy - self.options.starting_energy) \
            + abs(self.options.max_cardplays - self.options.starting_cardplays) \
            + abs(self.options.max_blight - self.options.starting_blight) \
            - (len(unique_pool) - overlap_count) \
            - sum(max_pair.values())

        # Check if sharding not too large and add to offset
        if len(self.options.spirit_aspect_locked.value) > 0:
            max_sharding = -gen_offset // len(self.options.spirit_aspect_locked.value)
            if max_sharding < self.options.spirit_shards.value:
                if max_sharding > 1:
                    raise OptionError(f"Not enough locations to shard into {self.options.spirit_shards.value} pieces. "
                                    f"Maximum possible is {max_sharding}.")
                raise OptionError(f"Not enough locations, {gen_offset} extra locations required. "
                                  "Try adding more goals.")
            gen_offset += self.options.spirit_shards.value * len(self.options.spirit_aspect_locked.value)

        if self.options.remove_cards_when_fill.value:
            if gen_offset < 0:
                card_pool = card_pool[:gen_offset]

        for card in card_pool:
            self.add_powercard_location(card)

        boss_event_names = []
        previous: tuple[None|Adversary, None|Spirit|Aspect] = (None, None)

        # Boss locations
        for boss, difficulty, spirit in sorted(self.options.parsed_goals(self.random),
            key=lambda x: (x[0].value, x[2].value if x[2] is not None else "", x[1]), reverse=True):
            # prevent duplicate goals
            if previous == (boss, spirit):
                continue
            previous = (boss, spirit)

            for diff in range(0, difficulty + 1):
                self.add_boss_location(boss, diff, spirit, diff == difficulty)

            boss_event_names.append(
                defeat_with_string(boss, difficulty, spirit, True))

        # Victory requires ALL boss defeat events
        self.multiworld.completion_condition[self.player] = \
            lambda state, boss_event_names=boss_event_names: state.has_all(boss_event_names, self.player)

    def create_items(self):
        self.itempool = []

        # Energy progression
        for _ in range(self.options.starting_energy, self.options.max_energy):
            self.itempool.append(
                self.create_item("+1 Energy", ItemClassification.useful)
            )
        if self.options.starting_energy < 0:
            self.multiworld.early_items[self.player]["+1 Energy"] = -self.options.starting_energy

        # Card play progression
        for _ in range(self.options.starting_cardplays, self.options.max_cardplays):
            self.itempool.append(
                self.create_item("+1 Cardplay", ItemClassification.useful)
            )
        if self.options.starting_cardplays < 0:
            self.multiworld.early_items[self.player]["+1 Cardplay"] = -self.options.starting_cardplays

        # Blight progression
        for _ in range(self.options.starting_blight, self.options.max_blight):
            self.itempool.append(
                self.create_item("+1 Blight", ItemClassification.useful)
            )
        if self.options.starting_blight < 0:
            self.multiworld.early_items[self.player]["+1 Blight"] = -self.options.starting_blight

        # Spirit Unlocks
        for sa in self.options.spirit_aspect_locked.parsed:
            self.itempool.extend(
                self.create_item(sa.full_name, ItemClassification.progression | ItemClassification.useful)
                for _ in range(self.options.spirit_shards.value)
            )

        enabled_sources = {ContentSource(key)
                           for key in self.options.enabled_expansions.value}

        card_pool = (
            card for card in Powercard if card.expansion in enabled_sources and card.card_type is not CardType.Unique)
        # Power card unlocks
        for card in card_pool:
            self.itempool.append(
                self.create_item(
                    card.value, ItemClassification.progression_deprioritized)
            )

        # Filler
        remaining = len(self.multiworld.get_unfilled_locations(self.player)) - len(self.itempool)

        # Extra copy filler
        extra_copies = []
        if self.options.copies_of_spirit.value > 0:
            copies = self.options.copies_of_spirit.value
            max_copies = remaining // len(self.options.spirit_aspect_locked.value)
            if copies <= max_copies:
                extra_copies = [
                    self.create_item(spirit_aspect.full_name,
                                     ItemClassification.useful & ItemClassification.filler)
                    for spirit_aspect in self.options.spirit_aspect_locked.parsed
                    for _ in range(copies)
                ]
            else:
                spirits = list(self.options.spirit_aspect_locked.parsed)
                self.random.shuffle(spirits)

                extra_copies = [
                    self.create_item(spirits[i % len(spirits)].full_name,
                                    ItemClassification.useful & ItemClassification.filler)
                    for i in range(remaining)
                ]
        self.itempool.extend(extra_copies)
        remaining -= len(extra_copies)

        # Element filler
        element_filler_count = int(remaining * (float(self.options.elements_fill_ratio) / 100.0))
        element_filler = [self.random.choice(list(Element)).value for _ in range(element_filler_count)]
        for item_name in element_filler:
            self.itempool.append(self.create_item(item_name, ItemClassification.filler))
        remaining -= element_filler_count

        # Useless filler
        random_filler_items = [self.get_filler_item_name() for _ in range(remaining)]
        for item_name in random_filler_items:
            self.itempool.append(self.create_item(item_name, ItemClassification.filler))

        self.multiworld.itempool += self.itempool

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def set_rules(self) -> None:
        pass

    def generate_basic(self) -> None:
        pass

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        pass

    def fill_slot_data(self) -> Mapping[str, Any]:
        # Power card locations
        enabled_sources = {ContentSource(key)
                            for key in self.options.enabled_expansions.value}
        card_pool = [card.value for card in Powercard
                            if (self.options.lock_not_in_play_cards.result or (card.expansion in enabled_sources)) \
                            and card.card_type is not CardType.Unique]
        goals = [defeat_with_string(*goal) for goal in self.options.parsed_goals(self.random)]
        return {
            "base_locked_cards": card_pool,
            "base_locked_spirits": [s.value for s in self.options.spirit_aspect_locked.spirits],
            "base_locked_aspects": [a.full_name for a in self.options.spirit_aspect_locked.aspects],
            "base_energy_offset": self.options.starting_energy.value,
            "base_cardplay_offset": self.options.starting_cardplays.value,
            "base_blight_offset": self.options.starting_blight.value,
            "spirit_shards": self.options.spirit_shards.value,
            "spoil_locations": self.options.spoil_locations.value,
            "hint_cards": self.options.hint_received_cards.value,
            "prioritised_shuffle": self.options.prioritised_shuffle.value,
            "deathlink": self.options.deathlink.value,
            "goals": goals
        }

    def add_powercard_location(self, card: Powercard,
                               progression: LocationProgressType = LocationProgressType.DEFAULT) -> None:
        region = self.multiworld.get_region("Island", self.player)

        loc = SpiritIslandLocation(
            self.player,
            f"Play: {card.value}",
            self.location_name_to_id[f"Play: {card.value}"],
            region
        )
        loc.progress_type = progression

        # Becomes reachable when the card is unlocked
        loc.access_rule = lambda state, card=card: state.has(card.value, self.player)

        region.locations.append(loc)

    def add_unique_powercard_location(self, card: Powercard, spirits_aspects: set[Spirit | Aspect]) -> None:
        region = self.multiworld.get_region("Island", self.player)

        loc = SpiritIslandLocation(
            self.player,
            f"Play: {card.value}",
            self.location_name_to_id[f"Play: {card.value}"],
            region
        )
        loc.progress_type = LocationProgressType.PRIORITY

        locked = set(self.options.spirit_aspect_locked.parsed)

        if spirits_aspects.issubset(locked):
            required_count = self.options.spirit_shards.value
            loc.access_rule = lambda state, sa=spirits_aspects, req=required_count: \
                any(state.has(spirit.full_name, self.player, req) for spirit in sa)

        region.locations.append(loc)

    def add_boss_location(self, boss: Adversary, difficulty: int, spirit: Spirit | Aspect | None, goal=False) -> None:
        region = self.multiworld.get_region("Island", self.player)

        shard_count = self.options.spirit_shards.value
        locked = self.options.spirit_aspect_locked

        def make_access_rule(spirit):
            if spirit not in locked.parsed:
                return None

            requirements = [(spirit.full_name, shard_count)]

            if isinstance(spirit, Aspect) and spirit.spirit in locked.spirits:
                requirements.append((spirit.spirit.value, shard_count))

            return lambda state, reqs=requirements: all(
                state.has(item, self.player, count) for item, count in reqs
            )

        def create_location(name, loc_id):
            loc = SpiritIslandLocation(self.player, name, loc_id, region)
            loc.progress_type = LocationProgressType.PRIORITY

            rule = make_access_rule(spirit)
            if rule:
                loc.access_rule = rule

            region.locations.append(loc)
            return loc

        # Main boss location
        name = defeat_with_string(boss, difficulty, spirit)
        create_location(name, self.location_name_to_id[name])

        # Victory condition location
        if goal:
            vic_name = f"{name} (victory condition)"
            vic_loc = create_location(vic_name, None)

            victory_item = self.create_event(
                defeat_with_string(boss, difficulty, spirit, True),
                ItemClassification.progression_skip_balancing
            )

            vic_loc.place_locked_item(victory_item)
