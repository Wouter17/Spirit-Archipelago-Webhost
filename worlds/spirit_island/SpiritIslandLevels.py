from abc import abstractmethod  # noqa: N999
from enum import Enum, EnumMeta


class ContentSource(Enum):
    BASE = "Spirit Island"
    PP1 = "Promo Pack 1: Flame"
    PP2 = "Promo Pack 2: Feather"
    BC = "Branch and Claw"
    JE = "Jagged Earth"
    NI = "Nature Incarnate"
    HORIZONS = "Horizons of Spirit Island"

class Element(Enum):
    SUN = "Sun"
    MOON = "Moon"
    FIRE = "Fire"
    AIR = "Air"
    WATER = "Water"
    EARTH = "Earth"
    PLANT = "Plant"
    ANIMAL = "Animal"

class PlayableSpirit(metaclass=EnumMeta):

    @property
    @abstractmethod
    def full_name(self) -> str:
        pass

    @property
    @abstractmethod
    def spirit(self) -> "Spirit":
        pass

    @property
    @abstractmethod
    def uniques(self) -> "set[Powercard]":
        pass


class Spirit(Enum, PlayableSpirit):
    Lightning = "Lightning's Swift Strike"
    River = "River Surges in Sunlight"
    Shadows = "Shadows Flicker Like Flame"
    Earth = "Vital Strength of the Earth"
    Green = "A Spread of Rampant Green"
    Thunderspeaker = "Thunderspeaker"
    Bringer = "Bringer of Dreams and Nightmares"
    Ocean = "Ocean's Hungry Grasp"
    Keeper = "Keeper of the Forbidden Wilds"
    Fangs = "Sharp Fangs Behind the Leaves"
    Wildfire = "Heart of the Wildfire"
    Snek = "Serpent Slumbering Beneath the Island"
    Trickster = "Grinning Trickster Stirs Up Trouble"
    Lure = "Lure of the Deep Wilderness"
    MM = "Many Minds Move as One"
    Memory = "Shifting Memory of Ages"
    Stone = "Stone's Unyielding Defiance"
    Volcano = "Volcano Looming High"
    Shroud = "Shroud of Silent Mist"
    Vengeance = "Vengeance as a Burning Plague"
    Fractured = "Fractured Days Split the Sky"
    Starlight = "Starlight Seeks Its Form"
    Downpour = "Downpour Drenches the World"
    Finder = "Finder of Paths Unseen"
    Teeth = "Devouring Teeth Lurk Underfoot"
    Eyes = "Eyes Watch From the Trees"
    Otter = "Fathomless Mud of the Swamp"
    Heat = "Rising Heat of Stone and Sand"
    Whirlwind = "Sun-Bright Whirlwind"
    Behemoth = "Ember-Eyed Behemoth"
    HearthVigil = "Hearth-Vigil"
    Roots = "Towering Roots of the Jungle"
    BODDYS = "Breath of Darkness Down Your Spine"
    Gaze = "Relentless Gaze of the Sun"
    Voice = "Wandering Voice Keens Delirium"
    WWB = "Wounded Waters Bleeding"
    Earthquakes = "Dances Up Earthquakes"

    @property
    def full_name(self) -> str:
        return self.value

    @property
    def spirit(self) -> "Spirit":
        return self

    @property
    def uniques(self) -> "set[Powercard]":
        return {card for card in Powercard if card.spirit == self} - {
            Powercard.Belligerent_and_Aggressive_Crops,
            Powercard.Smite_the_Land_with_Fulmination,
        }


class Aspect(Enum, PlayableSpirit):
    Pandemonium = "Pandemonium"
    Wind = "Wind"
    Sunshine = "Sunshine"
    Madness = "Madness"
    Reach = "Reach"
    Resilience = "Resilience"
    Immense = "Immense"
    Travel = "Travel"
    Amorphous = "Amorphous"
    Foreboding = "Foreboding"
    Might = "Might"
    Regrowth = "Regrowth"
    Tangles = "Tangles"
    Enticing = "Enticing"
    Violence = "Violence"
    Transforming = "Transforming"
    SpreadingHostility = "Spreading Hostility"
    Sparking = "Sparking"
    Lair = "Lair"
    Deeps = "Deeps"
    Haven = "Haven"
    Locus = "Locus"
    DarkFire = "Dark Fire"
    Encircle = "Encircle"
    Unconstrained = "Unconstrained"
    Intensify = "Intensify"
    Mentor = "Mentor"
    Stranded = "Stranded"
    Tactician = "Tactician"
    Warrior = "Warrior"
    Nourishing = "Nourishing"

    @property
    def spirit(self) -> Spirit:
        return aspect_to_spirit[self]

    @property
    def full_name(self) -> str:
        return f"{self.spirit.value} ({self.value})"

    @property
    def uniques(self) -> "set[Powercard]":
        cards = {card for card in Powercard if card.spirit == self.spirit}
        match self:
            case Aspect.Sunshine:
                cards.remove(Powercard.Boon_of_Vigor)
            case Aspect.Tangles:
                cards.remove(Powercard.Gift_of_Proliferation)
                # unique
                cards.add(Powercard.Belligerent_and_Aggressive_Crops)
            case Aspect.Violence:
                cards.remove(Powercard.Dreams_of_the_Dahan)
                # minor
                cards.add(Powercard.Bats_Scout_For_Raids_By_Darkness)
            case Aspect.Sparking:
                cards.remove(Powercard.Raging_Storm)
                # unqiue
                cards.add(Powercard.Smite_the_Land_with_Fulmination)
            case Aspect.Locus:
                cards.remove(Powercard.Elemental_Aegis)
                # minor
                cards.add(Powercard.Pull_Beneath_the_Hungry_Earth)
            case Aspect.DarkFire:
                # minor
                cards.add(Powercard.Unquenchable_Flames)
            case Aspect.Warrior:
                cards.remove(Powercard.Manifestation_of_Power_and_Glory)
                # minor
                cards.add(Powercard.Call_to_Bloodshed)
            case Aspect.Nourishing:
                cards.remove(Powercard.A_Year_of_Perfect_Stillness)
                # minor
                cards.add(Powercard.Voracious_Growth)
        return cards


aspect_to_spirit = {
    Aspect.Pandemonium: Spirit.Lightning,
    Aspect.Wind: Spirit.Lightning,
    Aspect.Sunshine: Spirit.River,
    Aspect.Madness: Spirit.Shadows,
    Aspect.Reach: Spirit.Shadows,
    Aspect.Resilience: Spirit.Earth,
    Aspect.Immense: Spirit.Lightning,
    Aspect.Travel: Spirit.River,
    Aspect.Amorphous: Spirit.Shadows,
    Aspect.Foreboding: Spirit.Shadows,
    Aspect.Might: Spirit.Earth,
    Aspect.Regrowth: Spirit.Green,
    Aspect.Tangles: Spirit.Green,
    Aspect.Enticing: Spirit.Bringer,
    Aspect.Violence: Spirit.Bringer,
    Aspect.Transforming: Spirit.Wildfire,
    Aspect.SpreadingHostility: Spirit.Keeper,
    Aspect.Sparking: Spirit.Lightning,
    Aspect.Lair: Spirit.Lure,
    Aspect.Deeps: Spirit.Ocean,
    Aspect.Haven: Spirit.River,
    Aspect.Locus: Spirit.Snek,
    Aspect.DarkFire: Spirit.Shadows,
    Aspect.Encircle: Spirit.Fangs,
    Aspect.Unconstrained: Spirit.Fangs,
    Aspect.Intensify: Spirit.Memory,
    Aspect.Mentor: Spirit.Memory,
    Aspect.Stranded: Spirit.Shadows,
    Aspect.Tactician: Spirit.Thunderspeaker,
    Aspect.Warrior: Spirit.Thunderspeaker,
    Aspect.Nourishing: Spirit.Earth
}


class Adversary(Enum):
    BrandenburgPrussia = "The Kingdom of Brandenburg-Prussia"
    England = "The Kingdom of England"
    Sweden = "The Kingdom of Sweden"
    France = "The Kingdom of France (Plantation Colony)"
    HabsburgMonarchy = "The Habsburg Monarchy (Livestock Colony)"
    Russia = "The Tsardom of Russia"
    Scotland = "The Kingdom of Scotland"
    HabsburgMining = "Habsburg Mining Expedition"


class CardType(Enum):
    Unique = "Unique"
    Minor = "Minor"
    Major = "Major"

# Autogenerated


class Powercard(Enum):
    Call_of_the_Dahan_Ways = "Call of the Dahan Ways"
    Call_to_Bloodshed = "Call to Bloodshed"
    Call_to_Isolation = "Call to Isolation"
    Call_to_Migrate = "Call to Migrate"
    Call_to_Tend = "Call to Tend"
    Dark_and_Tangled_Woods = "Dark and Tangled Woods"
    Delusions_of_Danger = "Delusions of Danger"
    Devouring_Ants = "Devouring Ants"
    Drift_Down_into_Slumber = "Drift Down into Slumber"
    Drought = "Drought"
    Elemental_Boon = "Elemental Boon"
    Encompassing_Ward = "Encompassing Ward"
    Enticing_Splendor = "Enticing Splendor"
    Entrancing_Apparitions = "Entrancing Apparitions"
    Gift_of_Constancy = "Gift of Constancy"
    Gift_of_Living_Energy = "Gift of Living Energy"
    Gift_of_Power = "Gift of Power"
    Gnawing_Rootbiters = "Gnawing Rootbiters"
    Land_of_Haunts_and_Embers = "Land of Haunts and Embers"
    Lure_of_the_Unknown = "Lure of the Unknown"
    Natures_Resilience = "Nature's Resilience"
    Pull_Beneath_the_Hungry_Earth = "Pull Beneath the Hungry Earth"
    Purifying_Flame = "Purifying Flame"
    Quicken_the_Earths_Struggles = "Quicken the Earth's Struggles"
    Rain_of_Blood = "Rain of Blood"
    Reaching_Grasp = "Reaching Grasp"
    Rouse_the_Trees_and_Stones = "Rouse the Trees and Stones"
    Sap_the_Strength_of_Multitudes = "Sap the Strength of Multitudes"
    Savage_Mawbeasts = "Savage Mawbeasts"
    Shadows_of_the_Burning_Forest = "Shadows of the Burning Forest"
    Song_of_Sanctity = "Song of Sanctity"
    Steam_Vents = "Steam Vents"
    Uncanny_Melting = "Uncanny Melting"
    Veil_the_Nights_Hunt = "Veil the Night's Hunt"
    Visions_of_Fiery_Doom = "Visions of Fiery Doom"
    Voracious_Growth = "Voracious Growth"
    Accelerated_Rot = "Accelerated Rot"
    Blazing_Renewal = "Blazing Renewal"
    Cleansing_Floods = "Cleansing Floods"
    Dissolve_the_Bonds_of_Kinship = "Dissolve the Bonds of Kinship"
    Entwined_Power = "Entwined Power"
    Indomitable_Claim = "Indomitable Claim"
    Infinite_Vitality = "Infinite Vitality"
    Mists_of_Oblivion = "Mists of Oblivion"
    Paralyzing_Fright = "Paralyzing Fright"
    Pillar_of_Living_Flame = "Pillar of Living Flame"
    Poisoned_Land = "Poisoned Land"
    Powerstorm = "Powerstorm"
    Talons_of_Lightning = "Talons of Lightning"
    Terrifying_Nightmares = "Terrifying Nightmares"
    The_Jungle_Hungers = "The Jungle Hungers"
    The_Land_Thrashes_in_Furious_Pain = "The Land Thrashes in Furious Pain"
    The_Trees_and_Stones_Speak_of_War = "The Trees and Stones Speak of War"
    Tsunami = "Tsunami"
    Vengeance_of_the_Dead = "Vengeance of the Dead"
    Vigor_of_the_Breaking_Dawn = "Vigor of the Breaking Dawn"
    Winds_of_Rust_and_Atrophy = "Winds of Rust and Atrophy"
    Wrap_in_Wings_of_Sunlight = "Wrap in Wings of Sunlight"
    Fields_Choked_with_Growth = "Fields Choked with Growth"
    Gift_of_Proliferation = "Gift of Proliferation"
    Overgrow_in_a_Night = "Overgrow in a Night"
    Stem_the_Flow_of_Fresh_Water = "Stem the Flow of Fresh Water"
    Call_on_Midnights_Dream = "Call on Midnight's Dream"
    Dread_Apparitions = "Dread Apparitions"
    Dreams_of_the_Dahan = "Dreams of the Dahan"
    Predatory_Nightmares = "Predatory Nightmares"
    Harbingers_of_the_Lightning = "Harbingers of the Lightning"
    Lightnings_Boon = "Lightning's Boon"
    Raging_Storm = "Raging Storm"
    Shatter_Homesteads = "Shatter Homesteads"
    Call_of_the_Deeps = "Call of the Deeps"
    Grasping_Tide = "Grasping Tide"
    Swallow_the_Land_Dwellers = "Swallow the Land-Dwellers"
    Tidal_Boon = "Tidal Boon"
    Boon_of_Vigor = "Boon of Vigor"
    Flash_Floods = "Flash Floods"
    Rivers_Bounty = "River's Bounty"
    Wash_Away = "Wash Away"
    Concealing_Shadows = "Concealing Shadows"
    Crops_Wither_and_Fade = "Crops Wither and Fade"
    Favors_Called_Due = "Favors Called Due"
    Mantle_of_Dread = "Mantle of Dread"
    Manifestation_of_Power_and_Glory = "Manifestation of Power and Glory"
    Sudden_Ambush = "Sudden Ambush"
    Voice_of_Thunder = "Voice of Thunder"
    Words_of_Warning = "Words of Warning"
    A_Year_of_Perfect_Stillness = "A Year of Perfect Stillness"
    Draw_of_the_Fruitful_Earth = "Draw of the Fruitful Earth"
    Guard_the_Healing_Land = "Guard the Healing Land"
    Rituals_of_Destruction = "Rituals of Destruction"
    Absorb_Corruption = "Absorb Corruption"
    Animated_Wrackroot = "Animated Wrackroot"
    Call_to_Ferocity = "Call to Ferocity"
    Call_to_Trade = "Call to Trade"
    Confounding_Mists = "Confounding Mists"
    Cycles_of_Time_and_Tide = "Cycles of Time and Tide"
    Disorienting_Landscape = "Disorienting Landscape"
    Elusive_Ambushes = "Elusive Ambushes"
    Fire_in_the_Sky = "Fire in the Sky"
    Fleshrot_Fever = "Fleshrot Fever"
    Golds_Allure = "Gold's Allure"
    Guardian_Serpents = "Guardian Serpents"
    Here_There_Be_Monsters = "Here There Be Monsters"
    Infested_Aquifers = "Infested Aquifers"
    Inflame_the_Fires_of_Life = "Inflame the Fires of Life"
    Pact_of_the_Joined_Hunt = "Pact of the Joined Hunt"
    Poisoned_Dew = "Poisoned Dew"
    Portents_of_Disaster = "Portents of Disaster"
    Promises_of_Protection = "Promises of Protection"
    Prowling_Panthers = "Prowling Panthers"
    Razor_Sharp_Undergrowth = "Razor-Sharp Undergrowth"
    Renewing_Rain = "Renewing Rain"
    Rites_of_the_Lands_Rejection = "Rites of the Land's Rejection"
    Scour_the_Land = "Scour the Land"
    Sky_Stretches_to_Shore = "Sky Stretches to Shore"
    Spur_On_with_Words_of_Fire = "Spur On with Words of Fire"
    Swarming_Wasps = "Swarming Wasps"
    Teeming_Rivers = "Teeming Rivers"
    Tormenting_Rotflies = "Tormenting Rotflies"
    Twilight_Fog_Brings_Madness = "Twilight Fog Brings Madness"
    Bloodwrack_Plague = "Bloodwrack Plague"
    Cast_Down_into_the_Briny_Deep = "Cast Down into the Briny Deep"
    Death_Falls_Gently_From_Open_Blossoms = "Death Falls Gently From Open Blossoms"
    Fire_and_Flood = "Fire and Flood"
    Flow_Like_Water_Reach_Like_Air = "Flow Like Water, Reach Like Air"
    Grant_Hatred_a_Ravenous_Form = "Grant Hatred a Ravenous Form"
    Insatiable_Hunger_of_the_Swarm = "Insatiable Hunger of the Swarm"
    Instruments_of_Their_Own_Ruin = "Instruments of Their Own Ruin"
    Manifest_Incarnation = "Manifest Incarnation"
    Pent_Up_Calamity = "Pent-Up Calamity"
    Pyroclastic_Flow = "Pyroclastic Flow"
    Savage_Transformation = "Savage Transformation"
    Sea_Monsters = "Sea Monsters"
    Smothering_Infestation = "Smothering Infestation"
    Strangling_Firevine = "Strangling Firevine"
    Sweep_into_the_Sea = "Sweep into the Sea"
    Tigers_Hunting = "Tigers Hunting"
    Twisted_Flowers_Murmur_Ultimatums = "Twisted Flowers Murmur Ultimatums"
    Unlock_the_Gates_of_Deepest_Power = "Unlock the Gates of Deepest Power"
    Unrelenting_Growth = "Unrelenting Growth"
    Volcanic_Eruption = "Volcanic Eruption"
    Boon_of_Growing_Power = "Boon of Growing Power"
    Regrow_from_Roots = "Regrow from Roots"
    Sacrosanct_Wilderness = "Sacrosanct Wilderness"
    Towering_Wrath = "Towering Wrath"
    Prey_on_the_Builders = "Prey on the Builders"
    Teeth_Gleam_from_Darkness = "Teeth Gleam from Darkness"
    Terrifying_Chase = "Terrifying Chase"
    Too_Near_the_Jungle = "Too Near the Jungle"
    Asphyxiating_Smoke = "Asphyxiating Smoke"
    Flames_Fury = "Flame's Fury"
    Flash_Fires = "Flash-Fires"
    Threatening_Flames = "Threatening Flames"
    Absorb_Essence = "Absorb Essence"
    Elemental_Aegis = "Elemental Aegis"
    Gift_of_Flowing_Power = "Gift of Flowing Power"
    Gift_of_the_Primordial_Deeps = "Gift of the Primordial Deeps"
    Bats_Scout_For_Raids_By_Darkness = "Bats Scout For Raids By Darkness"
    Birds_Cry_Warning = "Birds Cry Warning"
    Blood_Draws_Predators = "Blood Draws Predators"
    Call_to_Guard = "Call to Guard"
    Carapaced_Land = "Carapaced Land"
    Desiccating_Winds = "Desiccating Winds"
    Dire_Metamorphosis = "Dire Metamorphosis"
    Domesticated_Animals_Go_Berserk = "Domesticated Animals Go Berserk"
    Dry_Wood_Explodes_in_Smoldering_Splinters = "Dry Wood Explodes in Smoldering Splinters"
    Entrap_the_Forces_of_Corruption = "Entrap the Forces of Corruption"
    Favor_of_the_Sun_and_Star_Lit_Dark = "Favor of the Sun and Star-Lit Dark"
    Flow_Downriver_Blow_Downwind = "Flow Downriver, Blow Downwind"
    Gift_of_Natures_Connection = "Gift of Nature's Connection"
    Gift_of_Twinned_Days = "Gift of Twinned Days"
    Haunted_By_Primal_Memories = "Haunted By Primal Memories"
    Hazards_Spread_Across_the_Island = "Hazards Spread Across the Island"
    Like_Calls_to_Like = "Like Calls to Like"
    Mesmerized_Tranquility = "Mesmerized Tranquility"
    Renewing_Boon = "Renewing Boon"
    Scream_Disease_Into_the_Wind = "Scream Disease Into the Wind"
    Sear_Anger_Into_the_Wild_Lands = "Sear Anger Into the Wild Lands"
    Set_Them_on_an_Ever_Twisting_Trail = "Set Them on an Ever-Twisting Trail"
    Skies_Herald_the_Season_of_Return = "Skies Herald the Season of Return"
    Strong_And_Constant_Currents = "Strong And Constant Currents"
    Sucking_Ooze = "Sucking Ooze"
    Sunsets_Fire_Flows_Across_the_Land = "Sunset's Fire Flows Across the Land"
    Territorial_Strife = "Territorial Strife"
    Terror_Turns_to_Madness = "Terror Turns to Madness"
    The_Shore_Seethes_With_Hatred = "The Shore Seethes With Hatred"
    Thriving_Chokefungus = "Thriving Chokefungus"
    Treacherous_Waterways = "Treacherous Waterways"
    Unquenchable_Flames = "Unquenchable Flames"
    Weep_for_What_Is_Lost = "Weep for What Is Lost"
    Angry_Bears = "Angry Bears"
    Bargains_of_Power_and_Protection = "Bargains of Power and Protection"
    Draw_Towards_a_Consuming_Void = "Draw Towards a Consuming Void"
    Dream_of_the_Untouched_Land = "Dream of the Untouched Land"
    Focus_the_Lands_Anguish = "Focus the Land's Anguish"
    Forests_of_Living_Obsidian = "Forests of Living Obsidian"
    Infestation_of_Venomous_Spiders = "Infestation of Venomous Spiders"
    Irresistible_Call = "Irresistible Call"
    Melt_Earth_Into_Quicksand = "Melt Earth Into Quicksand"
    Settle_Into_Hunting_Grounds = "Settle Into Hunting-Grounds"
    Sleep_and_Never_Waken = "Sleep and Never Waken"
    Spill_Bitterness_Into_the_Earth = "Spill Bitterness Into the Earth"
    Storm_Swath = "Storm-Swath"
    The_Wounded_Wild_Turns_on_its_Assailants = "The Wounded Wild Turns on its Assailants"
    Thickets_Erupt_with_Every_Touch_of_Breeze = "Thickets Erupt with Every Touch of Breeze"
    Transform_to_a_Murderous_Darkness = "Transform to a Murderous Darkness"
    Trees_Radiate_Celestial_Brilliance = "Trees Radiate Celestial Brilliance"
    Unleash_a_Torrent_of_the_Selfs_Own_Essence = "Unleash a Torrent of the Self's Own Essence"
    Utter_a_Curse_of_Dread_and_Bone = "Utter a Curse of Dread and Bone"
    Vanish_Softly_Away_Forgotten_by_All = "Vanish Softly Away, Forgotten by All"
    Voice_of_Command = "Voice of Command"
    Walls_of_Rock_and_Thorn = "Walls of Rock and Thorn"
    Weave_Together_the_Fabric_of_Place = "Weave Together the Fabric of Place"
    Absolute_Stasis = "Absolute Stasis"
    Blur_the_Arc_of_Years = "Blur the Arc of Years"
    Pour_Time_Sideways = "Pour Time Sideways"
    The_Past_Returns_Again = "The Past Returns Again"
    Impersonate_Authority = "Impersonate Authority"
    Incite_the_Mob = "Incite the Mob"
    Overenthusiastic_Arson = "Overenthusiastic Arson"
    Unexpected_Tigers = "Unexpected Tigers"
    Gift_of_the_Untamed_Wild = "Gift of the Untamed Wild"
    Perils_of_the_Deepest_Island = "Perils of the Deepest Island"
    Softly_Beckon_Ever_Inward = "Softly Beckon Ever Inward"
    Swallowed_by_the_Wilderness = "Swallowed by the Wilderness"
    A_Dreadful_Tide_of_Scurrying_Flesh = "A Dreadful Tide of Scurrying Flesh"
    Boon_of_Swarming_Bedevilment = "Boon of Swarming Bedevilment"
    Ever_Multiplying_Swarm = "Ever-Multiplying Swarm"
    Guide_the_Way_on_Feathered_Wings = "Guide the Way on Feathered Wings"
    Pursue_with_Scratches_Pecks_and_Stings = "Pursue with Scratches, Pecks, and Stings"
    Boon_of_Ancient_Memories = "Boon of Ancient Memories"
    Elemental_Teachings = "Elemental Teachings"
    Share_Secrets_of_Survival = "Share Secrets of Survival"
    Study_the_Invaders_Fears = "Study the Invaders' Fears"
    Dissolving_Vapors = "Dissolving Vapors"
    Flowing_and_Silent_Forms_Dart_By = "Flowing and Silent Forms Dart By"
    The_Fog_Closes_In = "The Fog Closes In"
    Unnerving_Pall = "Unnerving Pall"
    Boon_of_Reimagining = "Boon of Reimagining"
    Gather_the_Scattered_Light_of_Stars = "Gather the Scattered Light of Stars"
    Peace_of_the_Nighttime_Sky = "Peace of the Nighttime Sky"
    Shape_the_Self_Anew = "Shape the Self Anew"
    Jagged_Shards_Push_from_the_Earth = "Jagged Shards Push from the Earth"
    Plows_Shatter_on_Rocky_Ground = "Plows Shatter on Rocky Ground"
    Scarred_and_Stony_Land = "Scarred and Stony Land"
    Stubborn_Solidity = "Stubborn Solidity"
    Fetid_Breath_Spreads_Infection = "Fetid Breath Spreads Infection"
    Fiery_Vengeance = "Fiery Vengeance"
    Plaguebearers = "Plaguebearers"
    Strike_Low_with_Sudden_Fevers = "Strike Low with Sudden Fevers"
    Exaltation_of_Molten_Stone = "Exaltation of Molten Stone"
    Lava_Flows = "Lava Flows"
    Pyroclastic_Bombardment = "Pyroclastic Bombardment"
    Rain_of_Ash = "Rain of Ash"
    Dark_Skies_Loose_a_Stinging_Rain = "Dark Skies Loose a Stinging Rain"
    Foundations_Sink_into_Mud = "Foundations Sink into Mud"
    Gift_of_Abundance = "Gift of Abundance"
    Unbearable_Deluge = "Unbearable Deluge"
    A_Circuitous_and_Wending_Journey = "A Circuitous and Wending Journey"
    Aid_from_the_Spirit_Speakers = "Aid from the Spirit-Speakers"
    Offer_Passage_Between_Worlds = "Offer Passage Between Worlds"
    Paths_Tied_by_Nature = "Paths Tied by Nature"
    Travelers_Boon = "Traveler's Boon"
    Ways_of_Shore_and_Heartland = "Ways of Shore and Heartland"
    Ferocious_Rampage = "Ferocious Rampage"
    Gift_of_Furious_Might = "Gift of Furious Might"
    Herd_Towards_the_Lurking_Maw = "Herd Towards the Lurking Maw"
    Mark_Territory_with_Scars_and_Teeth = "Mark Territory with Scars and Teeth"
    Boon_of_Watchful_Guarding = "Boon of Watchful Guarding"
    Eerie_Noises_and_Moving_Trees = "Eerie Noises and Moving Trees"
    Mysterious_Abductions = "Mysterious Abductions"
    Whispered_Guidance_Through_the_Night = "Whispered Guidance Through the Night"
    Exaltation_of_Tangled_Growth = "Exaltation of Tangled Growth"
    Foul_Vapors_and_Fetid_Muck = "Foul Vapors and Fetid Muck"
    Intractable_Thickets_and_Thorns = "Intractable Thickets and Thorns"
    Open_Shifting_Waterways = "Open Shifting Waterways"
    Call_on_Herders_for_Aid = "Call on Herders for Aid"
    Gift_of_Searing_Heat = "Gift of Searing Heat"
    Stinging_Sandstorm = "Stinging Sandstorm"
    Sweltering_Exhaustion = "Sweltering Exhaustion"
    Gift_of_the_Sunlit_Air = "Gift of the Sunlit Air"
    Gift_of_Wind_Sped_Steps = "Gift of Wind-Sped Steps"
    Scatter_to_the_Winds = "Scatter to the Winds"
    Tempest_of_Leaves_and_Branches = "Tempest of Leaves and Branches"
    Roiling_Bog_and_Snagging_Thorn = "Roiling Bog and Snagging Thorn"
    Bargain_of_Coursing_Paths = "Bargain of Coursing Paths"
    Bombard_with_Boulders_and_Stinging_Seeds = "Bombard with Boulders and Stinging Seeds"
    Exaltation_of_the_Incandescent_Sky = "Exaltation of the Incandescent Sky"
    Flocking_Red_Talons = "Flocking Red-Talons"
    Fragments_of_Yesteryear = "Fragments of Yesteryear"
    Inspire_the_Release_of_Stolen_Lands = "Inspire the Release of Stolen Lands"
    Plague_Ships_Sail_to_Distant_Ports = "Plague Ships Sail to Distant Ports"
    Ravaged_Undergrowth_Slithers_Back_to_Life = "Ravaged Undergrowth Slithers Back to Life"
    Rumbling_Earthquakes = "Rumbling Earthquakes"
    Solidify_Echoes_of_Majesty_Past = "Solidify Echoes of Majesty Past"
    Transformative_Sacrifice = "Transformative Sacrifice"
    Unearth_a_Beast_of_Wrathful_Stone = "Unearth a Beast of Wrathful Stone"
    Belligerent_and_Aggressive_Crops = "Belligerent and Aggressive Crops"
    Emerge_from_the_Dread_Night_Wind = "Emerge from the Dread Night Wind"
    Reach_from_the_Infinite_Darkness = "Reach from the Infinite Darkness"
    Swallowed_by_the_Endless_Dark = "Swallowed by the Endless Dark"
    Terror_of_the_Hunted = "Terror of the Hunted"
    Exaltation_of_Echoed_Steps = "Exaltation of Echoed Steps"
    Gift_of_Seismic_Energy = "Gift of Seismic Energy"
    Inspire_a_Winding_Dance = "Inspire a Winding Dance"
    Radiating_Tremors = "Radiating Tremors"
    Resounding_Footfalls_Sow_Dismay = "Resounding Footfalls Sow Dismay"
    Rumblings_Portend_a_Greater_Quake = "Rumblings Portend a Greater Quake"
    Blazing_Intimidation = "Blazing Intimidation"
    Exaltation_of_Grasping_Roots = "Exaltation of Grasping Roots"
    Surging_Lahar = "Surging Lahar"
    Terrifying_Rampage = "Terrifying Rampage"
    Call_to_Vigilance = "Call to Vigilance"
    Coordinated_Raid = "Coordinated Raid"
    Favors_of_Story_and_Season = "Favors of Story and Season"
    Surrounded_by_the_Dahan = "Surrounded by the Dahan"
    Smite_the_Land_with_Fulmination = "Smite the Land with Fulmination"
    Blinding_Glare = "Blinding Glare"
    Focus_the_Suns_Rays = "Focus the Sun's Rays"
    Unbearable_Gaze = "Unbearable Gaze"
    Wither_Bodies_Scar_Stones = "Wither Bodies, Scar Stones"
    Blooming_of_the_Rocks_and_Trees = "Blooming of the Rocks and Trees"
    Boon_of_Resilient_Power = "Boon of Resilient Power"
    Entwine_the_Fates_of_All = "Entwine the Fates of All"
    Radiant_and_Hallowed_Grove = "Radiant and Hallowed Grove"
    Exhale_Confusion_and_Delirium = "Exhale Confusion and Delirium"
    Frightful_Keening = "Frightful Keening"
    Turmoils_Touch = "Turmoil's Touch"
    Twist_Perceptions = "Twist Perceptions"
    Blood_Water_and_Bloodlust = "Blood Water and Bloodlust"
    Boon_of_Corrupted_Blood = "Boon of Corrupted Blood"
    Draw_to_the_Waters_Edge = "Draw to the Water's Edge"
    Wrack_with_Pain_and_Grief = "Wrack with Pain and Grief"

    @property
    def expansion(self) -> ContentSource:
        return card_to_expansion[self]

    @property
    def card_type(self) -> CardType:
        return card_to_cardtype[self]

    @property
    def spirit(self) -> Spirit | None:
        if self.card_type is CardType.Unique:
            return unique_to_spirit[self]
        return None


card_to_cardtype = {
    Powercard.Call_of_the_Dahan_Ways: CardType.Minor,
    Powercard.Call_to_Bloodshed: CardType.Minor,
    Powercard.Call_to_Isolation: CardType.Minor,
    Powercard.Call_to_Migrate: CardType.Minor,
    Powercard.Call_to_Tend: CardType.Minor,
    Powercard.Dark_and_Tangled_Woods: CardType.Minor,
    Powercard.Delusions_of_Danger: CardType.Minor,
    Powercard.Devouring_Ants: CardType.Minor,
    Powercard.Drift_Down_into_Slumber: CardType.Minor,
    Powercard.Drought: CardType.Minor,
    Powercard.Elemental_Boon: CardType.Minor,
    Powercard.Encompassing_Ward: CardType.Minor,
    Powercard.Enticing_Splendor: CardType.Minor,
    Powercard.Entrancing_Apparitions: CardType.Minor,
    Powercard.Gift_of_Constancy: CardType.Minor,
    Powercard.Gift_of_Living_Energy: CardType.Minor,
    Powercard.Gift_of_Power: CardType.Minor,
    Powercard.Gnawing_Rootbiters: CardType.Minor,
    Powercard.Land_of_Haunts_and_Embers: CardType.Minor,
    Powercard.Lure_of_the_Unknown: CardType.Minor,
    Powercard.Natures_Resilience: CardType.Minor,
    Powercard.Pull_Beneath_the_Hungry_Earth: CardType.Minor,
    Powercard.Purifying_Flame: CardType.Minor,
    Powercard.Quicken_the_Earths_Struggles: CardType.Minor,
    Powercard.Rain_of_Blood: CardType.Minor,
    Powercard.Reaching_Grasp: CardType.Minor,
    Powercard.Rouse_the_Trees_and_Stones: CardType.Minor,
    Powercard.Sap_the_Strength_of_Multitudes: CardType.Minor,
    Powercard.Savage_Mawbeasts: CardType.Minor,
    Powercard.Shadows_of_the_Burning_Forest: CardType.Minor,
    Powercard.Song_of_Sanctity: CardType.Minor,
    Powercard.Steam_Vents: CardType.Minor,
    Powercard.Uncanny_Melting: CardType.Minor,
    Powercard.Veil_the_Nights_Hunt: CardType.Minor,
    Powercard.Visions_of_Fiery_Doom: CardType.Minor,
    Powercard.Voracious_Growth: CardType.Minor,
    Powercard.Accelerated_Rot: CardType.Major,
    Powercard.Blazing_Renewal: CardType.Major,
    Powercard.Cleansing_Floods: CardType.Major,
    Powercard.Dissolve_the_Bonds_of_Kinship: CardType.Major,
    Powercard.Entwined_Power: CardType.Major,
    Powercard.Indomitable_Claim: CardType.Major,
    Powercard.Infinite_Vitality: CardType.Major,
    Powercard.Mists_of_Oblivion: CardType.Major,
    Powercard.Paralyzing_Fright: CardType.Major,
    Powercard.Pillar_of_Living_Flame: CardType.Major,
    Powercard.Poisoned_Land: CardType.Major,
    Powercard.Powerstorm: CardType.Major,
    Powercard.Talons_of_Lightning: CardType.Major,
    Powercard.Terrifying_Nightmares: CardType.Major,
    Powercard.The_Jungle_Hungers: CardType.Major,
    Powercard.The_Land_Thrashes_in_Furious_Pain: CardType.Major,
    Powercard.The_Trees_and_Stones_Speak_of_War: CardType.Major,
    Powercard.Tsunami: CardType.Major,
    Powercard.Vengeance_of_the_Dead: CardType.Major,
    Powercard.Vigor_of_the_Breaking_Dawn: CardType.Major,
    Powercard.Winds_of_Rust_and_Atrophy: CardType.Major,
    Powercard.Wrap_in_Wings_of_Sunlight: CardType.Major,
    Powercard.Fields_Choked_with_Growth: CardType.Unique,
    Powercard.Gift_of_Proliferation: CardType.Unique,
    Powercard.Overgrow_in_a_Night: CardType.Unique,
    Powercard.Stem_the_Flow_of_Fresh_Water: CardType.Unique,
    Powercard.Call_on_Midnights_Dream: CardType.Unique,
    Powercard.Dread_Apparitions: CardType.Unique,
    Powercard.Dreams_of_the_Dahan: CardType.Unique,
    Powercard.Predatory_Nightmares: CardType.Unique,
    Powercard.Harbingers_of_the_Lightning: CardType.Unique,
    Powercard.Lightnings_Boon: CardType.Unique,
    Powercard.Raging_Storm: CardType.Unique,
    Powercard.Shatter_Homesteads: CardType.Unique,
    Powercard.Call_of_the_Deeps: CardType.Unique,
    Powercard.Grasping_Tide: CardType.Unique,
    Powercard.Swallow_the_Land_Dwellers: CardType.Unique,
    Powercard.Tidal_Boon: CardType.Unique,
    Powercard.Boon_of_Vigor: CardType.Unique,
    Powercard.Flash_Floods: CardType.Unique,
    Powercard.Rivers_Bounty: CardType.Unique,
    Powercard.Wash_Away: CardType.Unique,
    Powercard.Concealing_Shadows: CardType.Unique,
    Powercard.Crops_Wither_and_Fade: CardType.Unique,
    Powercard.Favors_Called_Due: CardType.Unique,
    Powercard.Mantle_of_Dread: CardType.Unique,
    Powercard.Manifestation_of_Power_and_Glory: CardType.Unique,
    Powercard.Sudden_Ambush: CardType.Unique,
    Powercard.Voice_of_Thunder: CardType.Unique,
    Powercard.Words_of_Warning: CardType.Unique,
    Powercard.A_Year_of_Perfect_Stillness: CardType.Unique,
    Powercard.Draw_of_the_Fruitful_Earth: CardType.Unique,
    Powercard.Guard_the_Healing_Land: CardType.Unique,
    Powercard.Rituals_of_Destruction: CardType.Unique,
    Powercard.Absorb_Corruption: CardType.Minor,
    Powercard.Animated_Wrackroot: CardType.Minor,
    Powercard.Call_to_Ferocity: CardType.Minor,
    Powercard.Call_to_Trade: CardType.Minor,
    Powercard.Confounding_Mists: CardType.Minor,
    Powercard.Cycles_of_Time_and_Tide: CardType.Minor,
    Powercard.Disorienting_Landscape: CardType.Minor,
    Powercard.Elusive_Ambushes: CardType.Minor,
    Powercard.Fire_in_the_Sky: CardType.Minor,
    Powercard.Fleshrot_Fever: CardType.Minor,
    Powercard.Golds_Allure: CardType.Minor,
    Powercard.Guardian_Serpents: CardType.Minor,
    Powercard.Here_There_Be_Monsters: CardType.Minor,
    Powercard.Infested_Aquifers: CardType.Minor,
    Powercard.Inflame_the_Fires_of_Life: CardType.Minor,
    Powercard.Pact_of_the_Joined_Hunt: CardType.Minor,
    Powercard.Poisoned_Dew: CardType.Minor,
    Powercard.Portents_of_Disaster: CardType.Minor,
    Powercard.Promises_of_Protection: CardType.Minor,
    Powercard.Prowling_Panthers: CardType.Minor,
    Powercard.Razor_Sharp_Undergrowth: CardType.Minor,
    Powercard.Renewing_Rain: CardType.Minor,
    Powercard.Rites_of_the_Lands_Rejection: CardType.Minor,
    Powercard.Scour_the_Land: CardType.Minor,
    Powercard.Sky_Stretches_to_Shore: CardType.Minor,
    Powercard.Spur_On_with_Words_of_Fire: CardType.Minor,
    Powercard.Swarming_Wasps: CardType.Minor,
    Powercard.Teeming_Rivers: CardType.Minor,
    Powercard.Tormenting_Rotflies: CardType.Minor,
    Powercard.Twilight_Fog_Brings_Madness: CardType.Minor,
    Powercard.Bloodwrack_Plague: CardType.Major,
    Powercard.Cast_Down_into_the_Briny_Deep: CardType.Major,
    Powercard.Death_Falls_Gently_From_Open_Blossoms: CardType.Major,
    Powercard.Fire_and_Flood: CardType.Major,
    Powercard.Flow_Like_Water_Reach_Like_Air: CardType.Major,
    Powercard.Grant_Hatred_a_Ravenous_Form: CardType.Major,
    Powercard.Insatiable_Hunger_of_the_Swarm: CardType.Major,
    Powercard.Instruments_of_Their_Own_Ruin: CardType.Major,
    Powercard.Manifest_Incarnation: CardType.Major,
    Powercard.Pent_Up_Calamity: CardType.Major,
    Powercard.Pyroclastic_Flow: CardType.Major,
    Powercard.Savage_Transformation: CardType.Major,
    Powercard.Sea_Monsters: CardType.Major,
    Powercard.Smothering_Infestation: CardType.Major,
    Powercard.Strangling_Firevine: CardType.Major,
    Powercard.Sweep_into_the_Sea: CardType.Major,
    Powercard.Tigers_Hunting: CardType.Major,
    Powercard.Twisted_Flowers_Murmur_Ultimatums: CardType.Major,
    Powercard.Unlock_the_Gates_of_Deepest_Power: CardType.Major,
    Powercard.Unrelenting_Growth: CardType.Major,
    Powercard.Volcanic_Eruption: CardType.Major,
    Powercard.Boon_of_Growing_Power: CardType.Unique,
    Powercard.Regrow_from_Roots: CardType.Unique,
    Powercard.Sacrosanct_Wilderness: CardType.Unique,
    Powercard.Towering_Wrath: CardType.Unique,
    Powercard.Prey_on_the_Builders: CardType.Unique,
    Powercard.Teeth_Gleam_from_Darkness: CardType.Unique,
    Powercard.Terrifying_Chase: CardType.Unique,
    Powercard.Too_Near_the_Jungle: CardType.Unique,
    Powercard.Asphyxiating_Smoke: CardType.Unique,
    Powercard.Flames_Fury: CardType.Unique,
    Powercard.Flash_Fires: CardType.Unique,
    Powercard.Threatening_Flames: CardType.Unique,
    Powercard.Absorb_Essence: CardType.Unique,
    Powercard.Elemental_Aegis: CardType.Unique,
    Powercard.Gift_of_Flowing_Power: CardType.Unique,
    Powercard.Gift_of_the_Primordial_Deeps: CardType.Unique,
    Powercard.Bats_Scout_For_Raids_By_Darkness: CardType.Minor,
    Powercard.Birds_Cry_Warning: CardType.Minor,
    Powercard.Blood_Draws_Predators: CardType.Minor,
    Powercard.Call_to_Guard: CardType.Minor,
    Powercard.Carapaced_Land: CardType.Minor,
    Powercard.Desiccating_Winds: CardType.Minor,
    Powercard.Dire_Metamorphosis: CardType.Minor,
    Powercard.Domesticated_Animals_Go_Berserk: CardType.Minor,
    Powercard.Dry_Wood_Explodes_in_Smoldering_Splinters: CardType.Minor,
    Powercard.Entrap_the_Forces_of_Corruption: CardType.Minor,
    Powercard.Favor_of_the_Sun_and_Star_Lit_Dark: CardType.Minor,
    Powercard.Flow_Downriver_Blow_Downwind: CardType.Minor,
    Powercard.Gift_of_Natures_Connection: CardType.Minor,
    Powercard.Gift_of_Twinned_Days: CardType.Minor,
    Powercard.Haunted_By_Primal_Memories: CardType.Minor,
    Powercard.Hazards_Spread_Across_the_Island: CardType.Minor,
    Powercard.Like_Calls_to_Like: CardType.Minor,
    Powercard.Mesmerized_Tranquility: CardType.Minor,
    Powercard.Renewing_Boon: CardType.Minor,
    Powercard.Scream_Disease_Into_the_Wind: CardType.Minor,
    Powercard.Sear_Anger_Into_the_Wild_Lands: CardType.Minor,
    Powercard.Set_Them_on_an_Ever_Twisting_Trail: CardType.Minor,
    Powercard.Skies_Herald_the_Season_of_Return: CardType.Minor,
    Powercard.Strong_And_Constant_Currents: CardType.Minor,
    Powercard.Sucking_Ooze: CardType.Minor,
    Powercard.Sunsets_Fire_Flows_Across_the_Land: CardType.Minor,
    Powercard.Territorial_Strife: CardType.Minor,
    Powercard.Terror_Turns_to_Madness: CardType.Minor,
    Powercard.The_Shore_Seethes_With_Hatred: CardType.Minor,
    Powercard.Thriving_Chokefungus: CardType.Minor,
    Powercard.Treacherous_Waterways: CardType.Minor,
    Powercard.Unquenchable_Flames: CardType.Minor,
    Powercard.Weep_for_What_Is_Lost: CardType.Minor,
    Powercard.Angry_Bears: CardType.Major,
    Powercard.Bargains_of_Power_and_Protection: CardType.Major,
    Powercard.Draw_Towards_a_Consuming_Void: CardType.Major,
    Powercard.Dream_of_the_Untouched_Land: CardType.Major,
    Powercard.Focus_the_Lands_Anguish: CardType.Major,
    Powercard.Forests_of_Living_Obsidian: CardType.Major,
    Powercard.Infestation_of_Venomous_Spiders: CardType.Major,
    Powercard.Irresistible_Call: CardType.Major,
    Powercard.Melt_Earth_Into_Quicksand: CardType.Major,
    Powercard.Settle_Into_Hunting_Grounds: CardType.Major,
    Powercard.Sleep_and_Never_Waken: CardType.Major,
    Powercard.Spill_Bitterness_Into_the_Earth: CardType.Major,
    Powercard.Storm_Swath: CardType.Major,
    Powercard.The_Wounded_Wild_Turns_on_its_Assailants: CardType.Major,
    Powercard.Thickets_Erupt_with_Every_Touch_of_Breeze: CardType.Major,
    Powercard.Transform_to_a_Murderous_Darkness: CardType.Major,
    Powercard.Trees_Radiate_Celestial_Brilliance: CardType.Major,
    Powercard.Unleash_a_Torrent_of_the_Selfs_Own_Essence: CardType.Major,
    Powercard.Utter_a_Curse_of_Dread_and_Bone: CardType.Major,
    Powercard.Vanish_Softly_Away_Forgotten_by_All: CardType.Major,
    Powercard.Voice_of_Command: CardType.Major,
    Powercard.Walls_of_Rock_and_Thorn: CardType.Major,
    Powercard.Weave_Together_the_Fabric_of_Place: CardType.Major,
    Powercard.Absolute_Stasis: CardType.Unique,
    Powercard.Blur_the_Arc_of_Years: CardType.Unique,
    Powercard.Pour_Time_Sideways: CardType.Unique,
    Powercard.The_Past_Returns_Again: CardType.Unique,
    Powercard.Impersonate_Authority: CardType.Unique,
    Powercard.Incite_the_Mob: CardType.Unique,
    Powercard.Overenthusiastic_Arson: CardType.Unique,
    Powercard.Unexpected_Tigers: CardType.Unique,
    Powercard.Gift_of_the_Untamed_Wild: CardType.Unique,
    Powercard.Perils_of_the_Deepest_Island: CardType.Unique,
    Powercard.Softly_Beckon_Ever_Inward: CardType.Unique,
    Powercard.Swallowed_by_the_Wilderness: CardType.Unique,
    Powercard.A_Dreadful_Tide_of_Scurrying_Flesh: CardType.Unique,
    Powercard.Boon_of_Swarming_Bedevilment: CardType.Unique,
    Powercard.Ever_Multiplying_Swarm: CardType.Unique,
    Powercard.Guide_the_Way_on_Feathered_Wings: CardType.Unique,
    Powercard.Pursue_with_Scratches_Pecks_and_Stings: CardType.Unique,
    Powercard.Boon_of_Ancient_Memories: CardType.Unique,
    Powercard.Elemental_Teachings: CardType.Unique,
    Powercard.Share_Secrets_of_Survival: CardType.Unique,
    Powercard.Study_the_Invaders_Fears: CardType.Unique,
    Powercard.Dissolving_Vapors: CardType.Unique,
    Powercard.Flowing_and_Silent_Forms_Dart_By: CardType.Unique,
    Powercard.The_Fog_Closes_In: CardType.Unique,
    Powercard.Unnerving_Pall: CardType.Unique,
    Powercard.Boon_of_Reimagining: CardType.Unique,
    Powercard.Gather_the_Scattered_Light_of_Stars: CardType.Unique,
    Powercard.Peace_of_the_Nighttime_Sky: CardType.Unique,
    Powercard.Shape_the_Self_Anew: CardType.Unique,
    Powercard.Jagged_Shards_Push_from_the_Earth: CardType.Unique,
    Powercard.Plows_Shatter_on_Rocky_Ground: CardType.Unique,
    Powercard.Scarred_and_Stony_Land: CardType.Unique,
    Powercard.Stubborn_Solidity: CardType.Unique,
    Powercard.Fetid_Breath_Spreads_Infection: CardType.Unique,
    Powercard.Fiery_Vengeance: CardType.Unique,
    Powercard.Plaguebearers: CardType.Unique,
    Powercard.Strike_Low_with_Sudden_Fevers: CardType.Unique,
    Powercard.Exaltation_of_Molten_Stone: CardType.Unique,
    Powercard.Lava_Flows: CardType.Unique,
    Powercard.Pyroclastic_Bombardment: CardType.Unique,
    Powercard.Rain_of_Ash: CardType.Unique,
    Powercard.Dark_Skies_Loose_a_Stinging_Rain: CardType.Unique,
    Powercard.Foundations_Sink_into_Mud: CardType.Unique,
    Powercard.Gift_of_Abundance: CardType.Unique,
    Powercard.Unbearable_Deluge: CardType.Unique,
    Powercard.A_Circuitous_and_Wending_Journey: CardType.Unique,
    Powercard.Aid_from_the_Spirit_Speakers: CardType.Unique,
    Powercard.Offer_Passage_Between_Worlds: CardType.Unique,
    Powercard.Paths_Tied_by_Nature: CardType.Unique,
    Powercard.Travelers_Boon: CardType.Unique,
    Powercard.Ways_of_Shore_and_Heartland: CardType.Unique,
    Powercard.Ferocious_Rampage: CardType.Unique,
    Powercard.Gift_of_Furious_Might: CardType.Unique,
    Powercard.Herd_Towards_the_Lurking_Maw: CardType.Unique,
    Powercard.Mark_Territory_with_Scars_and_Teeth: CardType.Unique,
    Powercard.Boon_of_Watchful_Guarding: CardType.Unique,
    Powercard.Eerie_Noises_and_Moving_Trees: CardType.Unique,
    Powercard.Mysterious_Abductions: CardType.Unique,
    Powercard.Whispered_Guidance_Through_the_Night: CardType.Unique,
    Powercard.Exaltation_of_Tangled_Growth: CardType.Unique,
    Powercard.Foul_Vapors_and_Fetid_Muck: CardType.Unique,
    Powercard.Intractable_Thickets_and_Thorns: CardType.Unique,
    Powercard.Open_Shifting_Waterways: CardType.Unique,
    Powercard.Call_on_Herders_for_Aid: CardType.Unique,
    Powercard.Gift_of_Searing_Heat: CardType.Unique,
    Powercard.Stinging_Sandstorm: CardType.Unique,
    Powercard.Sweltering_Exhaustion: CardType.Unique,
    Powercard.Gift_of_the_Sunlit_Air: CardType.Unique,
    Powercard.Gift_of_Wind_Sped_Steps: CardType.Unique,
    Powercard.Scatter_to_the_Winds: CardType.Unique,
    Powercard.Tempest_of_Leaves_and_Branches: CardType.Unique,
    Powercard.Roiling_Bog_and_Snagging_Thorn: CardType.Minor,
    Powercard.Bargain_of_Coursing_Paths: CardType.Major,
    Powercard.Bombard_with_Boulders_and_Stinging_Seeds: CardType.Major,
    Powercard.Exaltation_of_the_Incandescent_Sky: CardType.Major,
    Powercard.Flocking_Red_Talons: CardType.Major,
    Powercard.Fragments_of_Yesteryear: CardType.Major,
    Powercard.Inspire_the_Release_of_Stolen_Lands: CardType.Major,
    Powercard.Plague_Ships_Sail_to_Distant_Ports: CardType.Major,
    Powercard.Ravaged_Undergrowth_Slithers_Back_to_Life: CardType.Major,
    Powercard.Rumbling_Earthquakes: CardType.Major,
    Powercard.Solidify_Echoes_of_Majesty_Past: CardType.Major,
    Powercard.Transformative_Sacrifice: CardType.Major,
    Powercard.Unearth_a_Beast_of_Wrathful_Stone: CardType.Major,
    Powercard.Belligerent_and_Aggressive_Crops: CardType.Unique,
    Powercard.Emerge_from_the_Dread_Night_Wind: CardType.Unique,
    Powercard.Reach_from_the_Infinite_Darkness: CardType.Unique,
    Powercard.Swallowed_by_the_Endless_Dark: CardType.Unique,
    Powercard.Terror_of_the_Hunted: CardType.Unique,
    Powercard.Exaltation_of_Echoed_Steps: CardType.Unique,
    Powercard.Gift_of_Seismic_Energy: CardType.Unique,
    Powercard.Inspire_a_Winding_Dance: CardType.Unique,
    Powercard.Radiating_Tremors: CardType.Unique,
    Powercard.Resounding_Footfalls_Sow_Dismay: CardType.Unique,
    Powercard.Rumblings_Portend_a_Greater_Quake: CardType.Unique,
    Powercard.Blazing_Intimidation: CardType.Unique,
    Powercard.Exaltation_of_Grasping_Roots: CardType.Unique,
    Powercard.Surging_Lahar: CardType.Unique,
    Powercard.Terrifying_Rampage: CardType.Unique,
    Powercard.Call_to_Vigilance: CardType.Unique,
    Powercard.Coordinated_Raid: CardType.Unique,
    Powercard.Favors_of_Story_and_Season: CardType.Unique,
    Powercard.Surrounded_by_the_Dahan: CardType.Unique,
    Powercard.Smite_the_Land_with_Fulmination: CardType.Unique,
    Powercard.Blinding_Glare: CardType.Unique,
    Powercard.Focus_the_Suns_Rays: CardType.Unique,
    Powercard.Unbearable_Gaze: CardType.Unique,
    Powercard.Wither_Bodies_Scar_Stones: CardType.Unique,
    Powercard.Blooming_of_the_Rocks_and_Trees: CardType.Unique,
    Powercard.Boon_of_Resilient_Power: CardType.Unique,
    Powercard.Entwine_the_Fates_of_All: CardType.Unique,
    Powercard.Radiant_and_Hallowed_Grove: CardType.Unique,
    Powercard.Exhale_Confusion_and_Delirium: CardType.Unique,
    Powercard.Frightful_Keening: CardType.Unique,
    Powercard.Turmoils_Touch: CardType.Unique,
    Powercard.Twist_Perceptions: CardType.Unique,
    Powercard.Blood_Water_and_Bloodlust: CardType.Unique,
    Powercard.Boon_of_Corrupted_Blood: CardType.Unique,
    Powercard.Draw_to_the_Waters_Edge: CardType.Unique,
    Powercard.Wrack_with_Pain_and_Grief: CardType.Unique,
}


unique_to_spirit = {
    Powercard.Fields_Choked_with_Growth: Spirit.Green,
    Powercard.Gift_of_Proliferation: Spirit.Green,
    Powercard.Overgrow_in_a_Night: Spirit.Green,
    Powercard.Stem_the_Flow_of_Fresh_Water: Spirit.Green,
    Powercard.Call_on_Midnights_Dream: Spirit.Bringer,
    Powercard.Dread_Apparitions: Spirit.Bringer,
    Powercard.Dreams_of_the_Dahan: Spirit.Bringer,
    Powercard.Predatory_Nightmares: Spirit.Bringer,
    Powercard.Harbingers_of_the_Lightning: Spirit.Lightning,
    Powercard.Lightnings_Boon: Spirit.Lightning,
    Powercard.Raging_Storm: Spirit.Lightning,
    Powercard.Shatter_Homesteads: Spirit.Lightning,
    Powercard.Call_of_the_Deeps: Spirit.Ocean,
    Powercard.Grasping_Tide: Spirit.Ocean,
    Powercard.Swallow_the_Land_Dwellers: Spirit.Ocean,
    Powercard.Tidal_Boon: Spirit.Ocean,
    Powercard.Boon_of_Vigor: Spirit.River,
    Powercard.Flash_Floods: Spirit.River,
    Powercard.Rivers_Bounty: Spirit.River,
    Powercard.Wash_Away: Spirit.River,
    Powercard.Concealing_Shadows: Spirit.Shadows,
    Powercard.Crops_Wither_and_Fade: Spirit.Shadows,
    Powercard.Favors_Called_Due: Spirit.Shadows,
    Powercard.Mantle_of_Dread: Spirit.Shadows,
    Powercard.Manifestation_of_Power_and_Glory: Spirit.Thunderspeaker,
    Powercard.Sudden_Ambush: Spirit.Thunderspeaker,
    Powercard.Voice_of_Thunder: Spirit.Thunderspeaker,
    Powercard.Words_of_Warning: Spirit.Thunderspeaker,
    Powercard.A_Year_of_Perfect_Stillness: Spirit.Earth,
    Powercard.Draw_of_the_Fruitful_Earth: Spirit.Earth,
    Powercard.Guard_the_Healing_Land: Spirit.Earth,
    Powercard.Rituals_of_Destruction: Spirit.Earth,
    Powercard.Boon_of_Growing_Power: Spirit.Keeper,
    Powercard.Regrow_from_Roots: Spirit.Keeper,
    Powercard.Sacrosanct_Wilderness: Spirit.Keeper,
    Powercard.Towering_Wrath: Spirit.Keeper,
    Powercard.Prey_on_the_Builders: Spirit.Fangs,
    Powercard.Teeth_Gleam_from_Darkness: Spirit.Fangs,
    Powercard.Terrifying_Chase: Spirit.Fangs,
    Powercard.Too_Near_the_Jungle: Spirit.Fangs,
    Powercard.Asphyxiating_Smoke: Spirit.Wildfire,
    Powercard.Flames_Fury: Spirit.Wildfire,
    Powercard.Flash_Fires: Spirit.Wildfire,
    Powercard.Threatening_Flames: Spirit.Wildfire,
    Powercard.Absorb_Essence: Spirit.Snek,
    Powercard.Elemental_Aegis: Spirit.Snek,
    Powercard.Gift_of_Flowing_Power: Spirit.Snek,
    Powercard.Gift_of_the_Primordial_Deeps: Spirit.Snek,
    Powercard.Absolute_Stasis: Spirit.Fractured,
    Powercard.Blur_the_Arc_of_Years: Spirit.Fractured,
    Powercard.Pour_Time_Sideways: Spirit.Fractured,
    Powercard.The_Past_Returns_Again: Spirit.Fractured,
    Powercard.Impersonate_Authority: Spirit.Trickster,
    Powercard.Incite_the_Mob: Spirit.Trickster,
    Powercard.Overenthusiastic_Arson: Spirit.Trickster,
    Powercard.Unexpected_Tigers: Spirit.Trickster,
    Powercard.Gift_of_the_Untamed_Wild: Spirit.Lure,
    Powercard.Perils_of_the_Deepest_Island: Spirit.Lure,
    Powercard.Softly_Beckon_Ever_Inward: Spirit.Lure,
    Powercard.Swallowed_by_the_Wilderness: Spirit.Lure,
    Powercard.A_Dreadful_Tide_of_Scurrying_Flesh: Spirit.MM,
    Powercard.Boon_of_Swarming_Bedevilment: Spirit.MM,
    Powercard.Ever_Multiplying_Swarm: Spirit.MM,
    Powercard.Guide_the_Way_on_Feathered_Wings: Spirit.MM,
    Powercard.Pursue_with_Scratches_Pecks_and_Stings: Spirit.MM,
    Powercard.Boon_of_Ancient_Memories: Spirit.Memory,
    Powercard.Elemental_Teachings: Spirit.Memory,
    Powercard.Share_Secrets_of_Survival: Spirit.Memory,
    Powercard.Study_the_Invaders_Fears: Spirit.Memory,
    Powercard.Dissolving_Vapors: Spirit.Shroud,
    Powercard.Flowing_and_Silent_Forms_Dart_By: Spirit.Shroud,
    Powercard.The_Fog_Closes_In: Spirit.Shroud,
    Powercard.Unnerving_Pall: Spirit.Shroud,
    Powercard.Boon_of_Reimagining: Spirit.Starlight,
    Powercard.Gather_the_Scattered_Light_of_Stars: Spirit.Starlight,
    Powercard.Peace_of_the_Nighttime_Sky: Spirit.Starlight,
    Powercard.Shape_the_Self_Anew: Spirit.Starlight,
    Powercard.Jagged_Shards_Push_from_the_Earth: Spirit.Stone,
    Powercard.Plows_Shatter_on_Rocky_Ground: Spirit.Stone,
    Powercard.Scarred_and_Stony_Land: Spirit.Stone,
    Powercard.Stubborn_Solidity: Spirit.Stone,
    Powercard.Fetid_Breath_Spreads_Infection: Spirit.Vengeance,
    Powercard.Fiery_Vengeance: Spirit.Vengeance,
    Powercard.Plaguebearers: Spirit.Vengeance,
    Powercard.Strike_Low_with_Sudden_Fevers: Spirit.Vengeance,
    Powercard.Exaltation_of_Molten_Stone: Spirit.Volcano,
    Powercard.Lava_Flows: Spirit.Volcano,
    Powercard.Pyroclastic_Bombardment: Spirit.Volcano,
    Powercard.Rain_of_Ash: Spirit.Volcano,
    Powercard.Dark_Skies_Loose_a_Stinging_Rain: Spirit.Downpour,
    Powercard.Foundations_Sink_into_Mud: Spirit.Downpour,
    Powercard.Gift_of_Abundance: Spirit.Downpour,
    Powercard.Unbearable_Deluge: Spirit.Downpour,
    Powercard.A_Circuitous_and_Wending_Journey: Spirit.Finder,
    Powercard.Aid_from_the_Spirit_Speakers: Spirit.Finder,
    Powercard.Offer_Passage_Between_Worlds: Spirit.Finder,
    Powercard.Paths_Tied_by_Nature: Spirit.Finder,
    Powercard.Travelers_Boon: Spirit.Finder,
    Powercard.Ways_of_Shore_and_Heartland: Spirit.Finder,
    Powercard.Ferocious_Rampage: Spirit.Teeth,
    Powercard.Gift_of_Furious_Might: Spirit.Teeth,
    Powercard.Herd_Towards_the_Lurking_Maw: Spirit.Teeth,
    Powercard.Mark_Territory_with_Scars_and_Teeth: Spirit.Teeth,
    Powercard.Boon_of_Watchful_Guarding: Spirit.Eyes,
    Powercard.Eerie_Noises_and_Moving_Trees: Spirit.Eyes,
    Powercard.Mysterious_Abductions: Spirit.Eyes,
    Powercard.Whispered_Guidance_Through_the_Night: Spirit.Eyes,
    Powercard.Exaltation_of_Tangled_Growth: Spirit.Otter,
    Powercard.Foul_Vapors_and_Fetid_Muck: Spirit.Otter,
    Powercard.Intractable_Thickets_and_Thorns: Spirit.Otter,
    Powercard.Open_Shifting_Waterways: Spirit.Otter,
    Powercard.Call_on_Herders_for_Aid: Spirit.Heat,
    Powercard.Gift_of_Searing_Heat: Spirit.Heat,
    Powercard.Stinging_Sandstorm: Spirit.Heat,
    Powercard.Sweltering_Exhaustion: Spirit.Heat,
    Powercard.Gift_of_the_Sunlit_Air: Spirit.Whirlwind,
    Powercard.Gift_of_Wind_Sped_Steps: Spirit.Whirlwind,
    Powercard.Scatter_to_the_Winds: Spirit.Whirlwind,
    Powercard.Tempest_of_Leaves_and_Branches: Spirit.Whirlwind,
    Powercard.Belligerent_and_Aggressive_Crops: Spirit.Green,
    Powercard.Emerge_from_the_Dread_Night_Wind: Spirit.BODDYS,
    Powercard.Reach_from_the_Infinite_Darkness: Spirit.BODDYS,
    Powercard.Swallowed_by_the_Endless_Dark: Spirit.BODDYS,
    Powercard.Terror_of_the_Hunted: Spirit.BODDYS,
    Powercard.Exaltation_of_Echoed_Steps: Spirit.Earthquakes,
    Powercard.Gift_of_Seismic_Energy: Spirit.Earthquakes,
    Powercard.Inspire_a_Winding_Dance: Spirit.Earthquakes,
    Powercard.Radiating_Tremors: Spirit.Earthquakes,
    Powercard.Resounding_Footfalls_Sow_Dismay: Spirit.Earthquakes,
    Powercard.Rumblings_Portend_a_Greater_Quake: Spirit.Earthquakes,
    Powercard.Blazing_Intimidation: Spirit.Behemoth,
    Powercard.Exaltation_of_Grasping_Roots: Spirit.Behemoth,
    Powercard.Surging_Lahar: Spirit.Behemoth,
    Powercard.Terrifying_Rampage: Spirit.Behemoth,
    Powercard.Call_to_Vigilance: Spirit.HearthVigil,
    Powercard.Coordinated_Raid: Spirit.HearthVigil,
    Powercard.Favors_of_Story_and_Season: Spirit.HearthVigil,
    Powercard.Surrounded_by_the_Dahan: Spirit.HearthVigil,
    Powercard.Smite_the_Land_with_Fulmination: Spirit.Lightning,
    Powercard.Blinding_Glare: Spirit.Gaze,
    Powercard.Focus_the_Suns_Rays: Spirit.Gaze,
    Powercard.Unbearable_Gaze: Spirit.Gaze,
    Powercard.Wither_Bodies_Scar_Stones: Spirit.Gaze,
    Powercard.Blooming_of_the_Rocks_and_Trees: Spirit.Roots,
    Powercard.Boon_of_Resilient_Power: Spirit.Roots,
    Powercard.Entwine_the_Fates_of_All: Spirit.Roots,
    Powercard.Radiant_and_Hallowed_Grove: Spirit.Roots,
    Powercard.Exhale_Confusion_and_Delirium: Spirit.Voice,
    Powercard.Frightful_Keening: Spirit.Voice,
    Powercard.Turmoils_Touch: Spirit.Voice,
    Powercard.Twist_Perceptions: Spirit.Voice,
    Powercard.Blood_Water_and_Bloodlust: Spirit.WWB,
    Powercard.Boon_of_Corrupted_Blood: Spirit.WWB,
    Powercard.Draw_to_the_Waters_Edge: Spirit.WWB,
    Powercard.Wrack_with_Pain_and_Grief: Spirit.WWB,
}


card_to_expansion = {
    Powercard.Call_of_the_Dahan_Ways: ContentSource.BASE,
    Powercard.Call_to_Bloodshed: ContentSource.BASE,
    Powercard.Call_to_Isolation: ContentSource.BASE,
    Powercard.Call_to_Migrate: ContentSource.BASE,
    Powercard.Call_to_Tend: ContentSource.BASE,
    Powercard.Dark_and_Tangled_Woods: ContentSource.BASE,
    Powercard.Delusions_of_Danger: ContentSource.BASE,
    Powercard.Devouring_Ants: ContentSource.BASE,
    Powercard.Drift_Down_into_Slumber: ContentSource.BASE,
    Powercard.Drought: ContentSource.BASE,
    Powercard.Elemental_Boon: ContentSource.BASE,
    Powercard.Encompassing_Ward: ContentSource.BASE,
    Powercard.Enticing_Splendor: ContentSource.BASE,
    Powercard.Entrancing_Apparitions: ContentSource.BASE,
    Powercard.Gift_of_Constancy: ContentSource.BASE,
    Powercard.Gift_of_Living_Energy: ContentSource.BASE,
    Powercard.Gift_of_Power: ContentSource.BASE,
    Powercard.Gnawing_Rootbiters: ContentSource.BASE,
    Powercard.Land_of_Haunts_and_Embers: ContentSource.BASE,
    Powercard.Lure_of_the_Unknown: ContentSource.BASE,
    Powercard.Natures_Resilience: ContentSource.BASE,
    Powercard.Pull_Beneath_the_Hungry_Earth: ContentSource.BASE,
    Powercard.Purifying_Flame: ContentSource.BASE,
    Powercard.Quicken_the_Earths_Struggles: ContentSource.BASE,
    Powercard.Rain_of_Blood: ContentSource.BASE,
    Powercard.Reaching_Grasp: ContentSource.BASE,
    Powercard.Rouse_the_Trees_and_Stones: ContentSource.BASE,
    Powercard.Sap_the_Strength_of_Multitudes: ContentSource.BASE,
    Powercard.Savage_Mawbeasts: ContentSource.BASE,
    Powercard.Shadows_of_the_Burning_Forest: ContentSource.BASE,
    Powercard.Song_of_Sanctity: ContentSource.BASE,
    Powercard.Steam_Vents: ContentSource.BASE,
    Powercard.Uncanny_Melting: ContentSource.BASE,
    Powercard.Veil_the_Nights_Hunt: ContentSource.BASE,
    Powercard.Visions_of_Fiery_Doom: ContentSource.BASE,
    Powercard.Voracious_Growth: ContentSource.BASE,
    Powercard.Accelerated_Rot: ContentSource.BASE,
    Powercard.Blazing_Renewal: ContentSource.BASE,
    Powercard.Cleansing_Floods: ContentSource.BASE,
    Powercard.Dissolve_the_Bonds_of_Kinship: ContentSource.BASE,
    Powercard.Entwined_Power: ContentSource.BASE,
    Powercard.Indomitable_Claim: ContentSource.BASE,
    Powercard.Infinite_Vitality: ContentSource.BASE,
    Powercard.Mists_of_Oblivion: ContentSource.BASE,
    Powercard.Paralyzing_Fright: ContentSource.BASE,
    Powercard.Pillar_of_Living_Flame: ContentSource.BASE,
    Powercard.Poisoned_Land: ContentSource.BASE,
    Powercard.Powerstorm: ContentSource.BASE,
    Powercard.Talons_of_Lightning: ContentSource.BASE,
    Powercard.Terrifying_Nightmares: ContentSource.BASE,
    Powercard.The_Jungle_Hungers: ContentSource.BASE,
    Powercard.The_Land_Thrashes_in_Furious_Pain: ContentSource.BASE,
    Powercard.The_Trees_and_Stones_Speak_of_War: ContentSource.BASE,
    Powercard.Tsunami: ContentSource.BASE,
    Powercard.Vengeance_of_the_Dead: ContentSource.BASE,
    Powercard.Vigor_of_the_Breaking_Dawn: ContentSource.BASE,
    Powercard.Winds_of_Rust_and_Atrophy: ContentSource.BASE,
    Powercard.Wrap_in_Wings_of_Sunlight: ContentSource.BASE,
    Powercard.Fields_Choked_with_Growth: ContentSource.BASE,
    Powercard.Gift_of_Proliferation: ContentSource.BASE,
    Powercard.Overgrow_in_a_Night: ContentSource.BASE,
    Powercard.Stem_the_Flow_of_Fresh_Water: ContentSource.BASE,
    Powercard.Call_on_Midnights_Dream: ContentSource.BASE,
    Powercard.Dread_Apparitions: ContentSource.BASE,
    Powercard.Dreams_of_the_Dahan: ContentSource.BASE,
    Powercard.Predatory_Nightmares: ContentSource.BASE,
    Powercard.Harbingers_of_the_Lightning: ContentSource.BASE,
    Powercard.Lightnings_Boon: ContentSource.BASE,
    Powercard.Raging_Storm: ContentSource.BASE,
    Powercard.Shatter_Homesteads: ContentSource.BASE,
    Powercard.Call_of_the_Deeps: ContentSource.BASE,
    Powercard.Grasping_Tide: ContentSource.BASE,
    Powercard.Swallow_the_Land_Dwellers: ContentSource.BASE,
    Powercard.Tidal_Boon: ContentSource.BASE,
    Powercard.Boon_of_Vigor: ContentSource.BASE,
    Powercard.Flash_Floods: ContentSource.BASE,
    Powercard.Rivers_Bounty: ContentSource.BASE,
    Powercard.Wash_Away: ContentSource.BASE,
    Powercard.Concealing_Shadows: ContentSource.BASE,
    Powercard.Crops_Wither_and_Fade: ContentSource.BASE,
    Powercard.Favors_Called_Due: ContentSource.BASE,
    Powercard.Mantle_of_Dread: ContentSource.BASE,
    Powercard.Manifestation_of_Power_and_Glory: ContentSource.BASE,
    Powercard.Sudden_Ambush: ContentSource.BASE,
    Powercard.Voice_of_Thunder: ContentSource.BASE,
    Powercard.Words_of_Warning: ContentSource.BASE,
    Powercard.A_Year_of_Perfect_Stillness: ContentSource.BASE,
    Powercard.Draw_of_the_Fruitful_Earth: ContentSource.BASE,
    Powercard.Guard_the_Healing_Land: ContentSource.BASE,
    Powercard.Rituals_of_Destruction: ContentSource.BASE,
    Powercard.Absorb_Corruption: ContentSource.BC,
    Powercard.Animated_Wrackroot: ContentSource.BC,
    Powercard.Call_to_Ferocity: ContentSource.BC,
    Powercard.Call_to_Trade: ContentSource.BC,
    Powercard.Confounding_Mists: ContentSource.BC,
    Powercard.Cycles_of_Time_and_Tide: ContentSource.BC,
    Powercard.Disorienting_Landscape: ContentSource.BC,
    Powercard.Elusive_Ambushes: ContentSource.BC,
    Powercard.Fire_in_the_Sky: ContentSource.BC,
    Powercard.Fleshrot_Fever: ContentSource.BC,
    Powercard.Golds_Allure: ContentSource.BC,
    Powercard.Guardian_Serpents: ContentSource.BC,
    Powercard.Here_There_Be_Monsters: ContentSource.BC,
    Powercard.Infested_Aquifers: ContentSource.BC,
    Powercard.Inflame_the_Fires_of_Life: ContentSource.BC,
    Powercard.Pact_of_the_Joined_Hunt: ContentSource.BC,
    Powercard.Poisoned_Dew: ContentSource.BC,
    Powercard.Portents_of_Disaster: ContentSource.BC,
    Powercard.Promises_of_Protection: ContentSource.BC,
    Powercard.Prowling_Panthers: ContentSource.BC,
    Powercard.Razor_Sharp_Undergrowth: ContentSource.BC,
    Powercard.Renewing_Rain: ContentSource.BC,
    Powercard.Rites_of_the_Lands_Rejection: ContentSource.BC,
    Powercard.Scour_the_Land: ContentSource.BC,
    Powercard.Sky_Stretches_to_Shore: ContentSource.BC,
    Powercard.Spur_On_with_Words_of_Fire: ContentSource.BC,
    Powercard.Swarming_Wasps: ContentSource.BC,
    Powercard.Teeming_Rivers: ContentSource.BC,
    Powercard.Tormenting_Rotflies: ContentSource.BC,
    Powercard.Twilight_Fog_Brings_Madness: ContentSource.BC,
    Powercard.Bloodwrack_Plague: ContentSource.BC,
    Powercard.Cast_Down_into_the_Briny_Deep: ContentSource.BC,
    Powercard.Death_Falls_Gently_From_Open_Blossoms: ContentSource.BC,
    Powercard.Fire_and_Flood: ContentSource.BC,
    Powercard.Flow_Like_Water_Reach_Like_Air: ContentSource.BC,
    Powercard.Grant_Hatred_a_Ravenous_Form: ContentSource.BC,
    Powercard.Insatiable_Hunger_of_the_Swarm: ContentSource.BC,
    Powercard.Instruments_of_Their_Own_Ruin: ContentSource.BC,
    Powercard.Manifest_Incarnation: ContentSource.BC,
    Powercard.Pent_Up_Calamity: ContentSource.BC,
    Powercard.Pyroclastic_Flow: ContentSource.BC,
    Powercard.Savage_Transformation: ContentSource.BC,
    Powercard.Sea_Monsters: ContentSource.BC,
    Powercard.Smothering_Infestation: ContentSource.BC,
    Powercard.Strangling_Firevine: ContentSource.BC,
    Powercard.Sweep_into_the_Sea: ContentSource.BC,
    Powercard.Tigers_Hunting: ContentSource.BC,
    Powercard.Twisted_Flowers_Murmur_Ultimatums: ContentSource.BC,
    Powercard.Unlock_the_Gates_of_Deepest_Power: ContentSource.BC,
    Powercard.Unrelenting_Growth: ContentSource.BC,
    Powercard.Volcanic_Eruption: ContentSource.BC,
    Powercard.Boon_of_Growing_Power: ContentSource.BC,
    Powercard.Regrow_from_Roots: ContentSource.BC,
    Powercard.Sacrosanct_Wilderness: ContentSource.BC,
    Powercard.Towering_Wrath: ContentSource.BC,
    Powercard.Prey_on_the_Builders: ContentSource.BC,
    Powercard.Teeth_Gleam_from_Darkness: ContentSource.BC,
    Powercard.Terrifying_Chase: ContentSource.BC,
    Powercard.Too_Near_the_Jungle: ContentSource.BC,
    Powercard.Asphyxiating_Smoke: ContentSource.PP1,
    Powercard.Flames_Fury: ContentSource.PP1,
    Powercard.Flash_Fires: ContentSource.PP1,
    Powercard.Threatening_Flames: ContentSource.PP1,
    Powercard.Absorb_Essence: ContentSource.PP1,
    Powercard.Elemental_Aegis: ContentSource.PP1,
    Powercard.Gift_of_Flowing_Power: ContentSource.PP1,
    Powercard.Gift_of_the_Primordial_Deeps: ContentSource.PP1,
    Powercard.Bats_Scout_For_Raids_By_Darkness: ContentSource.JE,
    Powercard.Birds_Cry_Warning: ContentSource.JE,
    Powercard.Blood_Draws_Predators: ContentSource.JE,
    Powercard.Call_to_Guard: ContentSource.JE,
    Powercard.Carapaced_Land: ContentSource.JE,
    Powercard.Desiccating_Winds: ContentSource.JE,
    Powercard.Dire_Metamorphosis: ContentSource.JE,
    Powercard.Domesticated_Animals_Go_Berserk: ContentSource.JE,
    Powercard.Dry_Wood_Explodes_in_Smoldering_Splinters: ContentSource.JE,
    Powercard.Entrap_the_Forces_of_Corruption: ContentSource.JE,
    Powercard.Favor_of_the_Sun_and_Star_Lit_Dark: ContentSource.JE,
    Powercard.Flow_Downriver_Blow_Downwind: ContentSource.JE,
    Powercard.Gift_of_Natures_Connection: ContentSource.JE,
    Powercard.Gift_of_Twinned_Days: ContentSource.JE,
    Powercard.Haunted_By_Primal_Memories: ContentSource.JE,
    Powercard.Hazards_Spread_Across_the_Island: ContentSource.JE,
    Powercard.Like_Calls_to_Like: ContentSource.JE,
    Powercard.Mesmerized_Tranquility: ContentSource.JE,
    Powercard.Renewing_Boon: ContentSource.JE,
    Powercard.Scream_Disease_Into_the_Wind: ContentSource.JE,
    Powercard.Sear_Anger_Into_the_Wild_Lands: ContentSource.JE,
    Powercard.Set_Them_on_an_Ever_Twisting_Trail: ContentSource.JE,
    Powercard.Skies_Herald_the_Season_of_Return: ContentSource.JE,
    Powercard.Strong_And_Constant_Currents: ContentSource.JE,
    Powercard.Sucking_Ooze: ContentSource.JE,
    Powercard.Sunsets_Fire_Flows_Across_the_Land: ContentSource.JE,
    Powercard.Territorial_Strife: ContentSource.JE,
    Powercard.Terror_Turns_to_Madness: ContentSource.JE,
    Powercard.The_Shore_Seethes_With_Hatred: ContentSource.JE,
    Powercard.Thriving_Chokefungus: ContentSource.JE,
    Powercard.Treacherous_Waterways: ContentSource.JE,
    Powercard.Unquenchable_Flames: ContentSource.JE,
    Powercard.Weep_for_What_Is_Lost: ContentSource.JE,
    Powercard.Angry_Bears: ContentSource.JE,
    Powercard.Bargains_of_Power_and_Protection: ContentSource.JE,
    Powercard.Draw_Towards_a_Consuming_Void: ContentSource.JE,
    Powercard.Dream_of_the_Untouched_Land: ContentSource.JE,
    Powercard.Focus_the_Lands_Anguish: ContentSource.JE,
    Powercard.Forests_of_Living_Obsidian: ContentSource.JE,
    Powercard.Infestation_of_Venomous_Spiders: ContentSource.JE,
    Powercard.Irresistible_Call: ContentSource.JE,
    Powercard.Melt_Earth_Into_Quicksand: ContentSource.JE,
    Powercard.Settle_Into_Hunting_Grounds: ContentSource.JE,
    Powercard.Sleep_and_Never_Waken: ContentSource.JE,
    Powercard.Spill_Bitterness_Into_the_Earth: ContentSource.JE,
    Powercard.Storm_Swath: ContentSource.JE,
    Powercard.The_Wounded_Wild_Turns_on_its_Assailants: ContentSource.JE,
    Powercard.Thickets_Erupt_with_Every_Touch_of_Breeze: ContentSource.JE,
    Powercard.Transform_to_a_Murderous_Darkness: ContentSource.JE,
    Powercard.Trees_Radiate_Celestial_Brilliance: ContentSource.JE,
    Powercard.Unleash_a_Torrent_of_the_Selfs_Own_Essence: ContentSource.JE,
    Powercard.Utter_a_Curse_of_Dread_and_Bone: ContentSource.JE,
    Powercard.Vanish_Softly_Away_Forgotten_by_All: ContentSource.JE,
    Powercard.Voice_of_Command: ContentSource.JE,
    Powercard.Walls_of_Rock_and_Thorn: ContentSource.JE,
    Powercard.Weave_Together_the_Fabric_of_Place: ContentSource.JE,
    Powercard.Absolute_Stasis: ContentSource.JE,
    Powercard.Blur_the_Arc_of_Years: ContentSource.JE,
    Powercard.Pour_Time_Sideways: ContentSource.JE,
    Powercard.The_Past_Returns_Again: ContentSource.JE,
    Powercard.Impersonate_Authority: ContentSource.JE,
    Powercard.Incite_the_Mob: ContentSource.JE,
    Powercard.Overenthusiastic_Arson: ContentSource.JE,
    Powercard.Unexpected_Tigers: ContentSource.JE,
    Powercard.Gift_of_the_Untamed_Wild: ContentSource.JE,
    Powercard.Perils_of_the_Deepest_Island: ContentSource.JE,
    Powercard.Softly_Beckon_Ever_Inward: ContentSource.JE,
    Powercard.Swallowed_by_the_Wilderness: ContentSource.JE,
    Powercard.A_Dreadful_Tide_of_Scurrying_Flesh: ContentSource.JE,
    Powercard.Boon_of_Swarming_Bedevilment: ContentSource.JE,
    Powercard.Ever_Multiplying_Swarm: ContentSource.JE,
    Powercard.Guide_the_Way_on_Feathered_Wings: ContentSource.JE,
    Powercard.Pursue_with_Scratches_Pecks_and_Stings: ContentSource.JE,
    Powercard.Boon_of_Ancient_Memories: ContentSource.JE,
    Powercard.Elemental_Teachings: ContentSource.JE,
    Powercard.Share_Secrets_of_Survival: ContentSource.JE,
    Powercard.Study_the_Invaders_Fears: ContentSource.JE,
    Powercard.Dissolving_Vapors: ContentSource.JE,
    Powercard.Flowing_and_Silent_Forms_Dart_By: ContentSource.JE,
    Powercard.The_Fog_Closes_In: ContentSource.JE,
    Powercard.Unnerving_Pall: ContentSource.JE,
    Powercard.Boon_of_Reimagining: ContentSource.JE,
    Powercard.Gather_the_Scattered_Light_of_Stars: ContentSource.JE,
    Powercard.Peace_of_the_Nighttime_Sky: ContentSource.JE,
    Powercard.Shape_the_Self_Anew: ContentSource.JE,
    Powercard.Jagged_Shards_Push_from_the_Earth: ContentSource.JE,
    Powercard.Plows_Shatter_on_Rocky_Ground: ContentSource.JE,
    Powercard.Scarred_and_Stony_Land: ContentSource.JE,
    Powercard.Stubborn_Solidity: ContentSource.JE,
    Powercard.Fetid_Breath_Spreads_Infection: ContentSource.JE,
    Powercard.Fiery_Vengeance: ContentSource.JE,
    Powercard.Plaguebearers: ContentSource.JE,
    Powercard.Strike_Low_with_Sudden_Fevers: ContentSource.JE,
    Powercard.Exaltation_of_Molten_Stone: ContentSource.JE,
    Powercard.Lava_Flows: ContentSource.JE,
    Powercard.Pyroclastic_Bombardment: ContentSource.JE,
    Powercard.Rain_of_Ash: ContentSource.JE,
    Powercard.Dark_Skies_Loose_a_Stinging_Rain: ContentSource.PP2,
    Powercard.Foundations_Sink_into_Mud: ContentSource.PP2,
    Powercard.Gift_of_Abundance: ContentSource.PP2,
    Powercard.Unbearable_Deluge: ContentSource.PP2,
    Powercard.A_Circuitous_and_Wending_Journey: ContentSource.PP2,
    Powercard.Aid_from_the_Spirit_Speakers: ContentSource.PP2,
    Powercard.Offer_Passage_Between_Worlds: ContentSource.PP2,
    Powercard.Paths_Tied_by_Nature: ContentSource.PP2,
    Powercard.Travelers_Boon: ContentSource.PP2,
    Powercard.Ways_of_Shore_and_Heartland: ContentSource.PP2,
    Powercard.Ferocious_Rampage: ContentSource.HORIZONS,
    Powercard.Gift_of_Furious_Might: ContentSource.HORIZONS,
    Powercard.Herd_Towards_the_Lurking_Maw: ContentSource.HORIZONS,
    Powercard.Mark_Territory_with_Scars_and_Teeth: ContentSource.HORIZONS,
    Powercard.Boon_of_Watchful_Guarding: ContentSource.HORIZONS,
    Powercard.Eerie_Noises_and_Moving_Trees: ContentSource.HORIZONS,
    Powercard.Mysterious_Abductions: ContentSource.HORIZONS,
    Powercard.Whispered_Guidance_Through_the_Night: ContentSource.HORIZONS,
    Powercard.Exaltation_of_Tangled_Growth: ContentSource.HORIZONS,
    Powercard.Foul_Vapors_and_Fetid_Muck: ContentSource.HORIZONS,
    Powercard.Intractable_Thickets_and_Thorns: ContentSource.HORIZONS,
    Powercard.Open_Shifting_Waterways: ContentSource.HORIZONS,
    Powercard.Call_on_Herders_for_Aid: ContentSource.HORIZONS,
    Powercard.Gift_of_Searing_Heat: ContentSource.HORIZONS,
    Powercard.Stinging_Sandstorm: ContentSource.HORIZONS,
    Powercard.Sweltering_Exhaustion: ContentSource.HORIZONS,
    Powercard.Gift_of_the_Sunlit_Air: ContentSource.HORIZONS,
    Powercard.Gift_of_Wind_Sped_Steps: ContentSource.HORIZONS,
    Powercard.Scatter_to_the_Winds: ContentSource.HORIZONS,
    Powercard.Tempest_of_Leaves_and_Branches: ContentSource.HORIZONS,
    Powercard.Roiling_Bog_and_Snagging_Thorn: ContentSource.NI,
    Powercard.Bargain_of_Coursing_Paths: ContentSource.NI,
    Powercard.Bombard_with_Boulders_and_Stinging_Seeds: ContentSource.NI,
    Powercard.Exaltation_of_the_Incandescent_Sky: ContentSource.NI,
    Powercard.Flocking_Red_Talons: ContentSource.NI,
    Powercard.Fragments_of_Yesteryear: ContentSource.NI,
    Powercard.Inspire_the_Release_of_Stolen_Lands: ContentSource.NI,
    Powercard.Plague_Ships_Sail_to_Distant_Ports: ContentSource.NI,
    Powercard.Ravaged_Undergrowth_Slithers_Back_to_Life: ContentSource.NI,
    Powercard.Rumbling_Earthquakes: ContentSource.NI,
    Powercard.Solidify_Echoes_of_Majesty_Past: ContentSource.NI,
    Powercard.Transformative_Sacrifice: ContentSource.NI,
    Powercard.Unearth_a_Beast_of_Wrathful_Stone: ContentSource.NI,
    Powercard.Belligerent_and_Aggressive_Crops: ContentSource.NI,
    Powercard.Emerge_from_the_Dread_Night_Wind: ContentSource.NI,
    Powercard.Reach_from_the_Infinite_Darkness: ContentSource.NI,
    Powercard.Swallowed_by_the_Endless_Dark: ContentSource.NI,
    Powercard.Terror_of_the_Hunted: ContentSource.NI,
    Powercard.Exaltation_of_Echoed_Steps: ContentSource.NI,
    Powercard.Gift_of_Seismic_Energy: ContentSource.NI,
    Powercard.Inspire_a_Winding_Dance: ContentSource.NI,
    Powercard.Radiating_Tremors: ContentSource.NI,
    Powercard.Resounding_Footfalls_Sow_Dismay: ContentSource.NI,
    Powercard.Rumblings_Portend_a_Greater_Quake: ContentSource.NI,
    Powercard.Blazing_Intimidation: ContentSource.NI,
    Powercard.Exaltation_of_Grasping_Roots: ContentSource.NI,
    Powercard.Surging_Lahar: ContentSource.NI,
    Powercard.Terrifying_Rampage: ContentSource.NI,
    Powercard.Call_to_Vigilance: ContentSource.NI,
    Powercard.Coordinated_Raid: ContentSource.NI,
    Powercard.Favors_of_Story_and_Season: ContentSource.NI,
    Powercard.Surrounded_by_the_Dahan: ContentSource.NI,
    Powercard.Smite_the_Land_with_Fulmination: ContentSource.NI,
    Powercard.Blinding_Glare: ContentSource.NI,
    Powercard.Focus_the_Suns_Rays: ContentSource.NI,
    Powercard.Unbearable_Gaze: ContentSource.NI,
    Powercard.Wither_Bodies_Scar_Stones: ContentSource.NI,
    Powercard.Blooming_of_the_Rocks_and_Trees: ContentSource.NI,
    Powercard.Boon_of_Resilient_Power: ContentSource.NI,
    Powercard.Entwine_the_Fates_of_All: ContentSource.NI,
    Powercard.Radiant_and_Hallowed_Grove: ContentSource.NI,
    Powercard.Exhale_Confusion_and_Delirium: ContentSource.NI,
    Powercard.Frightful_Keening: ContentSource.NI,
    Powercard.Turmoils_Touch: ContentSource.NI,
    Powercard.Twist_Perceptions: ContentSource.NI,
    Powercard.Blood_Water_and_Bloodlust: ContentSource.NI,
    Powercard.Boon_of_Corrupted_Blood: ContentSource.NI,
    Powercard.Draw_to_the_Waters_Edge: ContentSource.NI,
    Powercard.Wrack_with_Pain_and_Grief: ContentSource.NI,
}
