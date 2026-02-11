from collections.abc import Callable, Mapping
from typing import Any, TextIO

from BaseClasses import CollectionState, ItemClassification, Location, LocationProgressType, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .Items import SpiritIslandItem, filler_items, item_descriptions, item_id_to_name, item_name_groups, item_name_to_id
from .Locations import SpiritIslandLocation, defeat_with_string, si_location_id_to_name, si_location_name_to_id
from .Options import SpiritIslandOptions, map_str_to_spirit_aspect, si_option_groups
from .SpiritIslandLevels import Adversary, Aspect, CardType, ContentSource, Powercard, Spirit


class SpiritIslandWeb(WebWorld):
    option_groups = si_option_groups
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

    gen_offset = 0
    """Offset for items-locations (positive if items > locations)"""

    def generate_early(self):
        self.pre_fill_item_placement = []

        selected_spirits_and_aspects = [sa for sa in (map_str_to_spirit_aspect(
            s) for s in self.options.spirit_play.value) if sa is not None]
        unique_pool = {unique for spirit_aspect in selected_spirits_and_aspects for unique in spirit_aspect.uniques}

        max_pair: dict[tuple[Adversary, Spirit | Aspect | None], int] = {}
        for boss, difficulty, spirit in self.options.goals.parsed:
            difficulty_offset = difficulty + 1
            key = (boss, spirit)
            if key not in max_pair or difficulty_offset > max_pair[key]:
                max_pair[key] = difficulty_offset

        self.gen_offset = abs(self.options.max_energy - self.options.starting_energy) \
            + abs(self.options.max_cardplays - self.options.starting_cardplays) \
            + abs(self.options.max_blight - self.options.starting_blight) \
            - len(unique_pool) \
            - sum(max_pair.values())

    def create_regions(self) -> None:
        self.add_region("Menu")
        self.add_region("Island")
        self.connect_regions("Menu", "Island")

        # Unique card locations
        selected_spirits_and_aspects = [sa for sa in (map_str_to_spirit_aspect(
            s) for s in self.options.spirit_play.value) if sa is not None]
        unique_pool = {unique for spirit_aspect in selected_spirits_and_aspects for unique in spirit_aspect.uniques}

        for card in unique_pool:
            self.add_unique_powercard_location(card)

        # Power card locations
        enabled_sources = {ContentSource(key)
                           for key in self.options.enabled_expansions.value}
        card_pool = [card for card in Powercard if \
                card.expansion in enabled_sources and \
                card.card_type is not CardType.Unique and \
                card not in unique_pool]
        card_pool = card_pool[:self.gen_offset] if self.gen_offset < 0 else card_pool

        for card in card_pool:
            self.add_powercard_location(card)

        boss_event_names = []
        previous: tuple[None|Adversary, None|Spirit|Aspect] = (None, None)

        # Boss locations
        for boss, difficulty, spirit in sorted(self.options.goals.parsed,
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

        # Card play progression
        for _ in range(self.options.starting_cardplays, self.options.max_cardplays):
            self.itempool.append(
                self.create_item("+1 Cardplay", ItemClassification.useful)
            )

        # Blight progression
        for _ in range(self.options.starting_blight, self.options.max_blight):
            self.itempool.append(
                self.create_item("+1 Blight", ItemClassification.useful)
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

        remaining = sum(1 for loc in self.multiworld.get_locations(self.player) if not loc.locked) \
            - len(self.itempool)
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
        goals = [defeat_with_string(*goal) for goal in self.options.goals.parsed]
        return {
            "base_locked_cards": card_pool,
            "base_energy_offset": self.options.starting_energy.value,
            "base_cardplay_offset": self.options.starting_cardplays.value,
            "base_blight_offset": self.options.starting_blight.value,
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

    def add_unique_powercard_location(self, card: Powercard) -> None:
        region = self.multiworld.get_region("Island", self.player)

        loc = SpiritIslandLocation(
            self.player,
            f"Play: {card.value}",
            self.location_name_to_id[f"Play: {card.value}"],
            region
        )
        loc.progress_type = LocationProgressType.PRIORITY

        region.locations.append(loc)

    def add_boss_location(self, boss: Adversary, difficulty: int, spirit: Spirit | Aspect | None, goal=False) -> None:
        region = self.multiworld.get_region("Island", self.player)

        name = defeat_with_string(boss, difficulty, spirit)
        loc = SpiritIslandLocation(
            self.player,
            name,
            self.location_name_to_id[name],
            region
        )
        loc.progress_type = LocationProgressType.PRIORITY
        region.locations.append(loc)

        if goal:
            vic_name = f"{name} (victory condition)"
            vic_loc = SpiritIslandLocation(
                self.player,
                vic_name,
                None,
                region
            )
            vic_loc.progress_type = LocationProgressType.PRIORITY

            victory_item = self.create_event(defeat_with_string(boss, difficulty, spirit, True),
                                            ItemClassification.progression_skip_balancing)

            # Each boss completion creates a unique event
            region.locations.append(vic_loc)
            vic_loc.place_locked_item(victory_item)
