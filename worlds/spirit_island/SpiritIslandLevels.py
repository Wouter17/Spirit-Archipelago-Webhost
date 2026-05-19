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
    Absolute_Stasis = "Absolute Stasis"
    Absorb_Essence = "Absorb Essence"
    Absorb_Corruption = "Absorb Corruption"
    Accelerated_Rot = "Accelerated Rot"
    A_Circuitous_and_Wending_Journey = "A Circuitous and Wending Journey"
    A_Dreadful_Tide_of_Scurrying_Flesh = "A Dreadful Tide of Scurrying Flesh"
    Aid_from_the_Spirit_Speakers = "Aid from the Spirit-Speakers"
    Animated_Wrackroot = "Animated Wrackroot"
    Angry_Bears = "Angry Bears"
    A_Year_of_Perfect_Stillness = "A Year of Perfect Stillness"
    Asphyxiating_Smoke = "Asphyxiating Smoke"
    Bargain_of_Coursing_Paths = "Bargain of Coursing Paths"
    Bargains_of_Power_and_Protection = "Bargains of Power and Protection"
    Bats_Scout_For_Raids_By_Darkness = "Bats Scout For Raids By Darkness"
    Birds_Cry_Warning = "Birds Cry Warning"
    Blazing_Intimidation = "Blazing Intimidation"
    Blazing_Renewal = "Blazing Renewal"
    Blood_Draws_Predators = "Blood Draws Predators"
    Bloodwrack_Plague = "Bloodwrack Plague"
    Blooming_of_the_Rocks_and_Trees = "Blooming of the Rocks and Trees"
    Blur_the_Arc_of_Years = "Blur the Arc of Years"
    Bombard_with_Boulders_and_Stinging_Seeds = "Bombard with Boulders and Stinging Seeds"
    Boon_of_Ancient_Memories = "Boon of Ancient Memories"
    Boon_of_Growing_Power = "Boon of Growing Power"
    Boon_of_Reimagining = "Boon of Reimagining"
    Boon_of_Resilient_Power = "Boon of Resilient Power"
    Boon_of_Swarming_Bedevilment = "Boon of Swarming Bedevilment"
    Boon_of_Vigor = "Boon of Vigor"
    Boon_of_Watchful_Guarding = "Boon of Watchful Guarding"
    Call_of_the_Dahan_Ways = "Call of the Dahan Ways"
    Call_of_the_Deeps = "Call of the Deeps"
    Call_on_Herders_for_Aid = "Call on Herders for Aid"
    Call_on_Midnights_Dreams = "Call on Midnight's Dreams"
    Call_to_Bloodshed = "Call to Bloodshed"
    Call_to_Ferocity = "Call to Ferocity"
    Call_to_Guard = "Call to Guard"
    Call_to_Isolation = "Call to Isolation"
    Call_to_Migrate = "Call to Migrate"
    Call_to_Tend = "Call to Tend"
    Call_to_Trade = "Call to Trade"
    Carapaced_Land = "Carapaced Land"
    Cast_Down_into_the_Briny_Deep = "Cast Down into the Briny Deep"
    Cleansing_Floods = "Cleansing Floods"
    Concealing_Shadows = "Concealing Shadows"
    Confounding_Mists = "Confounding Mists"
    Crops_Wither_and_Fade = "Crops Wither and Fade"
    Cycles_of_Time_and_Tide = "Cycles of Time and Tide"
    Dark_and_Tangled_Woods = "Dark and Tangled Woods"
    Dark_Skies_Loose_A_Stinging_Rain = "Dark Skies Loose A Stinging Rain"
    Death_Falls_Gently_From_Open_Blossoms = "Death Falls Gently From Open Blossoms"
    Delusions_of_Danger = "Delusions of Danger"
    Desiccating_Winds = "Desiccating Winds"
    Devouring_Ants = "Devouring Ants"
    Dire_Metamorphosis = "Dire Metamorphosis"
    Disorienting_Landscape = "Disorienting Landscape"
    Dissolve_the_Bonds_of_Kinship = "Dissolve the Bonds of Kinship"
    Dissolving_Vapors = "Dissolving Vapors"
    Domesticated_Animals_Go_Berserk = "Domesticated Animals Go Berserk"
    Draw_of_the_Fruitful_Earth = "Draw of the Fruitful Earth"
    Draw_Towards_a_Consuming_Void = "Draw Towards a Consuming Void"
    Dread_Apparitions = "Dread Apparitions"
    Dream_of_the_Untouched_Land = "Dream of the Untouched Land"
    Dreams_of_the_Dahan = "Dreams of the Dahan"
    Drift_Down_into_Slumber = "Drift Down into Slumber"
    Drought = "Drought"
    Dry_Wood_Explodes_in_Smoldering_Splinters = "Dry Wood Explodes in Smoldering Splinters"
    Eerie_Noises_and_Moving_Trees = "Eerie Noises and Moving Trees"
    Elemental_Boon = "Elemental Boon"
    Elemental_Teachings = "Elemental Teachings"
    Elusive_Ambushes = "Elusive Ambushes"
    Encompassing_Ward = "Encompassing Ward"
    Entrap_the_Forces_of_Corruption = "Entrap the Forces of Corruption"
    Elemental_Aegis = "Elemental Aegis"
    Enticing_Splendor = "Enticing Splendor"
    Entrancing_Apparitions = "Entrancing Apparitions"
    Entwined_Power = "Entwined Power"
    Entwine_the_Fates_of_All = "Entwine the Fates of All"
    Ever_Multiplying_Swarm = "Ever-Multiplying Swarm"
    Exaltation_of_Echoed_Steps = "Exaltation of Echoed Steps"
    Exaltation_of_Grasping_Roots = "Exaltation of Grasping Roots"
    Exaltation_of_Molten_Stone = "Exaltation of Molten Stone"
    Exaltation_of_Tangled_Growth = "Exaltation of Tangled Growth"
    Exaltation_of_the_Incandescent_Sky = "Exaltation of the Incandescent Sky"
    Exhale_Confusion_and_Delirium = "Exhale Confusion and Delirium"
    Favor_of_the_Sun_and_Star_Lit_Dark = "Favor of the Sun and Star-Lit Dark"
    Favors_Called_Due = "Favors Called Due"
    Ferocious_Rampage = "Ferocious Rampage"
    Fetid_Breath_Spreads_Infection = "Fetid Breath Spreads Infection"
    Flocking_Red_Talons = "Flocking Red-Talons"
    Fields_Choked_with_Growth = "Fields Choked with Growth"
    Fiery_Vengeance = "Fiery Vengeance"
    Fire_and_Flood = "Fire and Flood"
    Fire_in_the_Sky = "Fire in the Sky"
    Flames_Fury = "Flame's Fury"
    Flash_fires = "Flash-fires"
    Flash_Floods = "Flash Floods"
    Fleshrot_Fever = "Fleshrot Fever"
    Flow_Downriver_Blow_Downwind = "Flow Downriver, Blow Downwind"
    Flowing_And_Silent_Forms_Dart_By = "Flowing And Silent Forms Dart By"
    Flow_Like_Water_Reach_Like_Air = "Flow Like Water, Reach Like Air"
    Focus_the_Lands_Anguish = "Focus the Land's Anguish"
    Forests_of_Living_Obsidian = "Forests of Living Obsidian"
    Foundations_Sink_Into_Mud = "Foundations Sink Into Mud"
    Foul_Vapors_and_Fetid_Muck = "Foul Vapors and Fetid Muck"
    Fragments_of_Yesteryear = "Fragments of Yesteryear"
    Frightful_Keening = "Frightful Keening"
    Gather_the_Scattered_Light_of_Stars = "Gather the Scattered Light of Stars"
    Gift_of_Abundance = "Gift of Abundance"
    Gift_of_Constancy = "Gift of Constancy"
    Gift_of_Flowing_Power = "Gift of Flowing Power"
    Gift_of_Furious_Might = "Gift of Furious Might"
    Gift_of_Living_Energy = "Gift of Living Energy"
    Gift_of_Natures_Connection = "Gift of Nature's Connection"
    Gift_of_Power = "Gift of Power"
    Gift_of_Proliferation = "Gift of Proliferation"
    Gift_of_Searing_Heat = "Gift of Searing Heat"
    Gift_of_Seismic_Energy = "Gift of Seismic Energy"
    Gift_of_the_Primordial_Deeps = "Gift of the Primordial Deeps"
    Gift_of_the_Sunlit_Air = "Gift of the Sunlit Air"
    Gift_of_the_Untamed_Wild = "Gift of the Untamed Wild"
    Gift_of_Twinned_Days = "Gift of Twinned Days"
    Gift_of_Wind_Sped_Steps = "Gift of Wind-Sped Steps"
    Gnawing_Rootbiters = "Gnawing Rootbiters"
    Golds_Allure = "Gold's Allure"
    Grant_Hatred_a_Ravenous_Form = "Grant Hatred a Ravenous Form"
    Grasping_Tide = "Grasping Tide"
    Growth_Through_Sacrifice = "Growth Through Sacrifice"
    Guardian_Serpents = "Guardian Serpents"
    Guard_the_Healing_Land = "Guard the Healing Land"
    Guide_the_Way_on_Feathered_Wings = "Guide the Way on Feathered Wings"
    Harbingers_of_the_Lightning = "Harbingers of the Lightning"
    Haunted_By_Primal_Memories = "Haunted By Primal Memories"
    Hazards_Spread_Across_the_Island = "Hazards Spread Across the Island"
    Herd_Towards_the_Lurking_Maw = "Herd Towards the Lurking Maw"
    Here_There_Be_Monsters = "Here There Be Monsters"
    Impersonate_Authority = "Impersonate Authority"
    Incite_the_Mob = "Incite the Mob"
    Inspire_a_Winding_Dance = "Inspire a Winding Dance"
    Indomitable_Claim = "Indomitable Claim"
    Infestation_of_Venomous_Spiders = "Infestation of Venomous Spiders"
    Infested_Aquifers = "Infested Aquifers"
    Infinite_Vitality = "Infinite Vitality"
    Inflame_the_Fires_of_Life = "Inflame the Fires of Life"
    Insatiable_Hunger_of_the_Swarm = "Insatiable Hunger of the Swarm"
    Inspire_the_Release_of_Stolen_Lands = "Inspire the Release of Stolen Lands"
    Instruments_of_Their_Own_Ruin = "Instruments of Their Own Ruin"
    Intractable_Thickets_and_Thorns = "Intractable Thickets and Thorns"
    Irresistible_Call = "Irresistible Call"
    Jagged_Shards_Push_from_the_Earth = "Jagged Shards Push from the Earth"
    Land_of_Haunts_and_Embers = "Land of Haunts and Embers"
    Lava_Flows = "Lava Flows"
    Like_Calls_to_Like = "Like Calls to Like"
    Lightnings_Boon = "Lightning's Boon"
    Lure_of_the_Unknown = "Lure of the Unknown"
    Manifestation_of_Power_and_Glory = "Manifestation of Power and Glory"
    Manifest_Incarnation = "Manifest Incarnation"
    Mantle_of_Dread = "Mantle of Dread"
    Mark_Territory_With_Scars_and_Teeth = "Mark Territory With Scars and Teeth"
    Mesmerized_Tranquility = "Mesmerized Tranquility"
    Melt_Earth_Into_Quicksand = "Melt Earth Into Quicksand"
    Mists_of_Oblivion = "Mists of Oblivion"
    Mysterious_Abductions = "Mysterious Abductions"
    Natures_Resilience = "Nature's Resilience"
    Offer_Passage_Between_Worlds = "Offer Passage Between Worlds"
    Open_Shifting_Waterways = "Open Shifting Waterways"
    Overenthusiastic_Arson = "Overenthusiastic Arson"
    Overgrow_in_a_Night = "Overgrow in a Night"
    Pact_of_the_Joined_Hunt = "Pact of the Joined Hunt"
    Paralyzing_Fright = "Paralyzing Fright"
    Paths_Tied_by_Nature = "Paths Tied by Nature"
    Peace_of_the_Nighttime_Sky = "Peace of the Nighttime Sky"
    Pent_Up_Calamity = "Pent-Up Calamity"
    Perils_of_the_Deepest_Island = "Perils of the Deepest Island"
    Pillar_of_Living_Flame = "Pillar of Living Flame"
    Plaguebearers = "Plaguebearers"
    Plague_Ships_Sail_to_Distant_Ports = "Plague Ships Sail to Distant Ports"
    Plows_Shatter_on_Rocky_Ground = "Plows Shatter on Rocky Ground"
    Poisoned_Dew = "Poisoned Dew"
    Poisoned_Land = "Poisoned Land"
    Portents_of_Disaster = "Portents of Disaster"
    Pour_Time_Sideways = "Pour Time Sideways"
    Powerstorm = "Powerstorm"
    Predatory_Nightmares = "Predatory Nightmares"
    Prey_on_the_Builders = "Prey on the Builders"
    Promises_of_Protection = "Promises of Protection"
    Prowling_Panthers = "Prowling Panthers"
    Pull_Beneath_the_Hungry_Earth = "Pull Beneath the Hungry Earth"
    Purifying_Flame = "Purifying Flame"
    Pursue_with_Scratches_Pecks_and_Stings = "Pursue with Scratches, Pecks, and Stings"
    Pyroclastic_Bombardment = "Pyroclastic Bombardment"
    Pyroclastic_Flow = "Pyroclastic Flow"
    Quicken_the_Earths_Struggles = "Quicken the Earth's Struggles"
    Radiating_Tremors = "Radiating Tremors"
    Radiant_and_Hallowed_Grove = "Radiant and Hallowed Grove"
    Raging_Storm = "Raging Storm"
    Rain_of_Ash = "Rain of Ash"
    Rain_of_Blood = "Rain of Blood"
    Ravaged_Undergrowth_Slithers_Back_to_Life = "Ravaged Undergrowth Slithers Back to Life"
    Razor_Sharp_Undergrowth = "Razor-Sharp Undergrowth"
    Reaching_Grasp = "Reaching Grasp"
    Regrow_From_Roots = "Regrow From Roots"
    Renewing_Boon = "Renewing Boon"
    Renewing_Rain = "Renewing Rain"
    Resounding_Footfalls_Sow_Dismay = "Resounding Footfalls Sow Dismay"
    Rites_of_the_Lands_Rejection = "Rites of the Land's Rejection"
    Rituals_of_Destruction = "Rituals of Destruction"
    Rivers_Bounty = "River's Bounty"
    Roiling_Bog_and_Snagging_Thorn = "Roiling Bog and Snagging Thorn"
    Rouse_the_Trees_and_Stones = "Rouse the Trees and Stones"
    Rumbling_Earthquakes = "Rumbling Earthquakes"
    Rumblings_Portend_a_Greater_Quake = "Rumblings Portend a Greater Quake"
    Sap_the_Strength_of_Multitudes = "Sap the Strength of Multitudes"
    Sacrosanct_Wilderness = "Sacrosanct Wilderness"
    Savage_Mawbeasts = "Savage Mawbeasts"
    Savage_Transformation = "Savage Transformation"
    Scarred_and_Stony_Land = "Scarred and Stony Land"
    Scatter_to_the_Winds = "Scatter to the Winds"
    Scour_the_Land = "Scour the Land"
    Scream_Disease_Into_the_Wind = "Scream Disease Into the Wind"
    Sea_Monsters = "Sea Monsters"
    Sear_Anger_Into_the_Wild_Lands = "Sear Anger Into the Wild Lands"
    Set_Them_on_an_Ever_Twisting_Trail = "Set Them on an Ever-Twisting Trail"
    Settle_Into_Hunting_Grounds = "Settle Into Hunting-Grounds"
    Shadows_of_the_Burning_Forest = "Shadows of the Burning Forest"
    Shape_the_Self_Anew = "Shape the Self Anew"
    Share_Secrets_of_Survival = "Share Secrets of Survival"
    Shatter_Homesteads = "Shatter Homesteads"
    Skies_Herald_the_Season_of_Return = "Skies Herald the Season of Return"
    Sky_Stretches_to_Shore = "Sky Stretches to Shore"
    Sleep_and_Never_Waken = "Sleep and Never Waken"
    Smothering_Infestation = "Smothering Infestation"
    Softly_Beckon_Ever_Inward = "Softly Beckon Ever Inward"
    Solidify_Echoes_of_Majesty_Past = "Solidify Echoes of Majesty Past"
    Song_of_Sanctity = "Song of Sanctity"
    Spill_Bitterness_Into_the_Earth = "Spill Bitterness Into the Earth"
    Spur_On_with_Words_of_Fire = "Spur On with Words of Fire"
    Steam_Vents = "Steam Vents"
    Stem_the_Flow_of_Fresh_Water = "Stem the Flow of Fresh Water"
    Stinging_Sandstorm = "Stinging Sandstorm"
    Storm_Swath = "Storm-Swath"
    Strangling_Firevine = "Strangling Firevine"
    Strike_Low_with_Sudden_Fevers = "Strike Low with Sudden Fevers"
    Strong_And_Constant_Currents = "Strong And Constant Currents"
    Stubborn_Solidity = "Stubborn Solidity"
    Study_the_Invaders_Fears = "Study the Invaders' Fears"
    Sucking_Ooze = "Sucking Ooze"
    Sudden_Ambush = "Sudden Ambush"
    Sunsets_Fire_Flows_Across_the_Land = "Sunset's Fire Flows Across the Land"
    Surging_Lahar = "Surging Lahar"
    Swallowed_by_the_Wilderness = "Swallowed by the Wilderness"
    Swallow_the_Land_Dwellers = "Swallow the Land-Dwellers"
    Swarming_Wasps = "Swarming Wasps"
    Sweep_into_the_Sea = "Sweep into the Sea"
    Sweltering_Exhaustion = "Sweltering Exhaustion"
    Talons_of_Lightning = "Talons of Lightning"
    Teeming_Rivers = "Teeming Rivers"
    Teeth_Gleam_from_Darkness = "Teeth Gleam from Darkness"
    Tempest_of_Leaves_and_Branches = "Tempest of Leaves and Branches"
    Terrifying_Chase = "Terrifying Chase"
    Terrifying_Nightmares = "Terrifying Nightmares"
    Terrifying_Rampage = "Terrifying Rampage"
    Territorial_Strife = "Territorial Strife"
    Terror_Turns_to_Madness = "Terror Turns to Madness"
    The_Fog_Closes_In = "The Fog Closes In"
    The_Jungle_Hungers = "The Jungle Hungers"
    The_Land_Thrashes_in_Furious_Pain = "The Land Thrashes in Furious Pain"
    The_Past_Returns_Again = "The Past Returns Again"
    The_Trees_and_Stones_Speak_of_War = "The Trees and Stones Speak of War"
    The_Shore_Seethes_With_Hatred = "The Shore Seethes With Hatred"
    The_Wounded_Wild_Turns_on_its_Assailants = "The Wounded Wild Turns on its Assailants"
    Thickets_Erupt_with_Every_Touch_of_Breeze = "Thickets Erupt with Every Touch of Breeze"
    Tigers_Hunting = "Tigers Hunting"
    Threatening_Flames = "Threatening Flames"
    Thriving_Chokefungus = "Thriving Chokefungus"
    Tidal_Boon = "Tidal Boon"
    Too_Near_the_Jungle = "Too Near the Jungle"
    Tormenting_Rotflies = "Tormenting Rotflies"
    Towering_Wrath = "Towering Wrath"
    Transformative_Sacrifice = "Transformative Sacrifice"
    Transform_to_a_Murderous_Darkness = "Transform to a Murderous Darkness"
    Travelers_Boon = "Traveler's Boon"
    Treacherous_Waterways = "Treacherous Waterways"
    Trees_Radiate_Celestial_Brilliance = "Trees Radiate Celestial Brilliance"
    Tsunami = "Tsunami"
    Turmoils_Touch = "Turmoil's Touch"
    Twilight_Fog_Brings_Madness = "Twilight Fog Brings Madness"
    Twist_Perceptions = "Twist Perceptions"
    Twisted_Flowers_Murmur_Ultimatums = "Twisted Flowers Murmur Ultimatums"
    Unbearable_Deluge = "Unbearable Deluge"
    Uncanny_Melting = "Uncanny Melting"
    Unearth_a_Beast_of_Wrathful_Stone = "Unearth a Beast of Wrathful Stone"
    Unexpected_Tigers = "Unexpected Tigers"
    Unleash_a_Torrent_of_the_Selfs_Own_Essence = "Unleash a Torrent of the Self's Own Essence"
    Unlock_the_Gates_of_Deepest_Power = "Unlock the Gates of Deepest Power"
    Unnerving_Pall = "Unnerving Pall"
    Unquenchable_Flames = "Unquenchable Flames"
    Unrelenting_Growth = "Unrelenting Growth"
    Vanish_Softly_Away_Forgotten_by_All = "Vanish Softly Away, Forgotten by All"
    Utter_a_Curse_of_Dread_and_Bone = "Utter a Curse of Dread and Bone"
    Voice_of_Command = "Voice of Command"
    Volcanic_Eruption = "Volcanic Eruption"
    Veil_the_Nights_Hunt = "Veil the Night's Hunt"
    Vengeance_of_the_Dead = "Vengeance of the Dead"
    Vigor_of_the_Breaking_Dawn = "Vigor of the Breaking Dawn"
    Visions_of_Fiery_Doom = "Visions of Fiery Doom"
    Voice_of_Thunder = "Voice of Thunder"
    Voracious_Growth = "Voracious Growth"
    Walls_of_Rock_and_Thorn = "Walls of Rock and Thorn"
    Wash_Away = "Wash Away"
    Ways_of_Shore_and_Heartland = "Ways of Shore and Heartland"
    Weave_Together_the_Fabric_of_Place = "Weave Together the Fabric of Place"
    Weep_for_What_Is_Lost = "Weep for What Is Lost"
    Whispered_Guidance_Through_the_Night = "Whispered Guidance Through the Night"
    Winds_of_Rust_and_Atrophy = "Winds of Rust and Atrophy"
    Words_of_Warning = "Words of Warning"
    Wrap_in_Wings_of_Sunlight = "Wrap in Wings of Sunlight"
    Belligerent_and_Aggressive_Crops = "Belligerent and Aggressive Crops"
    Emerge_from_the_Dread_Night_Wind = "Emerge from the Dread Night Wind"
    Reach_from_the_Infinite_Darkness = "Reach from the Infinite Darkness"
    Swallowed_by_the_Endless_Dark = "Swallowed by the Endless Dark"
    Terror_of_the_Hunted = "Terror of the Hunted"
    Call_to_Vigilance = "Call to Vigilance"
    Coordinated_Raid = "Coordinated Raid"
    Favors_of_Story_and_Season = "Favors of Story and Season"
    Surrounded_by_the_Dahan = "Surrounded by the Dahan"
    Smite_the_Land_with_Fulmination = "Smite the Land with Fulmination"
    Blinding_Glare = "Blinding Glare"
    Focus_the_Suns_Rays = "Focus the Sun's Rays"
    Unbearable_Gaze = "Unbearable Gaze"
    Wither_Bodies_Scar_Stones = "Wither Bodies, Scar Stones"
    Blood_Water_and_Bloodlust = "Blood Water and Bloodlust"
    Boon_of_Corrupted_Blood = "Boon of Corrupted Blood"
    Draw_to_the_Waters_Edge = "Draw to the Water's Edge"
    Wrack_with_Pain_and_Grief = "Wrack with Pain and Grief"

    @property
    def card_type(self) -> CardType:
        return card_to_cardtype[self]

    @property
    def spirit(self) -> Spirit | None:
        return unique_to_spirit.get(self)

    @property
    def expansion(self) -> ContentSource:
        return card_to_expansion[self]

card_to_cardtype = {
    Powercard.Absolute_Stasis: CardType.Unique,
    Powercard.Absorb_Essence: CardType.Unique,
    Powercard.Absorb_Corruption: CardType.Minor,
    Powercard.Accelerated_Rot: CardType.Major,
    Powercard.A_Circuitous_and_Wending_Journey: CardType.Unique,
    Powercard.A_Dreadful_Tide_of_Scurrying_Flesh: CardType.Unique,
    Powercard.Aid_from_the_Spirit_Speakers: CardType.Unique,
    Powercard.Animated_Wrackroot: CardType.Minor,
    Powercard.Angry_Bears: CardType.Major,
    Powercard.A_Year_of_Perfect_Stillness: CardType.Unique,
    Powercard.Asphyxiating_Smoke: CardType.Unique,
    Powercard.Bargain_of_Coursing_Paths: CardType.Major,
    Powercard.Bargains_of_Power_and_Protection: CardType.Major,
    Powercard.Bats_Scout_For_Raids_By_Darkness: CardType.Minor,
    Powercard.Birds_Cry_Warning: CardType.Minor,
    Powercard.Blazing_Intimidation: CardType.Unique,
    Powercard.Blazing_Renewal: CardType.Major,
    Powercard.Blood_Draws_Predators: CardType.Minor,
    Powercard.Bloodwrack_Plague: CardType.Major,
    Powercard.Blooming_of_the_Rocks_and_Trees: CardType.Unique,
    Powercard.Blur_the_Arc_of_Years: CardType.Unique,
    Powercard.Bombard_with_Boulders_and_Stinging_Seeds: CardType.Major,
    Powercard.Boon_of_Ancient_Memories: CardType.Unique,
    Powercard.Boon_of_Growing_Power: CardType.Unique,
    Powercard.Boon_of_Reimagining: CardType.Unique,
    Powercard.Boon_of_Resilient_Power: CardType.Unique,
    Powercard.Boon_of_Swarming_Bedevilment: CardType.Unique,
    Powercard.Boon_of_Vigor: CardType.Unique,
    Powercard.Boon_of_Watchful_Guarding: CardType.Unique,
    Powercard.Call_of_the_Dahan_Ways: CardType.Minor,
    Powercard.Call_of_the_Deeps: CardType.Unique,
    Powercard.Call_on_Herders_for_Aid: CardType.Unique,
    Powercard.Call_on_Midnights_Dreams: CardType.Unique,
    Powercard.Call_to_Bloodshed: CardType.Minor,
    Powercard.Call_to_Ferocity: CardType.Minor,
    Powercard.Call_to_Guard: CardType.Minor,
    Powercard.Call_to_Isolation: CardType.Minor,
    Powercard.Call_to_Migrate: CardType.Minor,
    Powercard.Call_to_Tend: CardType.Minor,
    Powercard.Call_to_Trade: CardType.Minor,
    Powercard.Carapaced_Land: CardType.Minor,
    Powercard.Cast_Down_into_the_Briny_Deep: CardType.Major,
    Powercard.Cleansing_Floods: CardType.Major,
    Powercard.Concealing_Shadows: CardType.Unique,
    Powercard.Confounding_Mists: CardType.Minor,
    Powercard.Crops_Wither_and_Fade: CardType.Unique,
    Powercard.Cycles_of_Time_and_Tide: CardType.Minor,
    Powercard.Dark_and_Tangled_Woods: CardType.Minor,
    Powercard.Dark_Skies_Loose_A_Stinging_Rain: CardType.Unique,
    Powercard.Death_Falls_Gently_From_Open_Blossoms: CardType.Major,
    Powercard.Delusions_of_Danger: CardType.Minor,
    Powercard.Desiccating_Winds: CardType.Minor,
    Powercard.Devouring_Ants: CardType.Minor,
    Powercard.Dire_Metamorphosis: CardType.Minor,
    Powercard.Disorienting_Landscape: CardType.Minor,
    Powercard.Dissolve_the_Bonds_of_Kinship: CardType.Major,
    Powercard.Dissolving_Vapors: CardType.Unique,
    Powercard.Domesticated_Animals_Go_Berserk: CardType.Minor,
    Powercard.Draw_of_the_Fruitful_Earth: CardType.Unique,
    Powercard.Draw_Towards_a_Consuming_Void: CardType.Major,
    Powercard.Dread_Apparitions: CardType.Unique,
    Powercard.Dream_of_the_Untouched_Land: CardType.Major,
    Powercard.Dreams_of_the_Dahan: CardType.Unique,
    Powercard.Drift_Down_into_Slumber: CardType.Minor,
    Powercard.Drought: CardType.Minor,
    Powercard.Dry_Wood_Explodes_in_Smoldering_Splinters: CardType.Minor,
    Powercard.Eerie_Noises_and_Moving_Trees: CardType.Unique,
    Powercard.Elemental_Boon: CardType.Minor,
    Powercard.Elemental_Teachings: CardType.Unique,
    Powercard.Elusive_Ambushes: CardType.Minor,
    Powercard.Encompassing_Ward: CardType.Minor,
    Powercard.Entrap_the_Forces_of_Corruption: CardType.Minor,
    Powercard.Elemental_Aegis: CardType.Unique,
    Powercard.Enticing_Splendor: CardType.Minor,
    Powercard.Entrancing_Apparitions: CardType.Minor,
    Powercard.Entwined_Power: CardType.Major,
    Powercard.Entwine_the_Fates_of_All: CardType.Unique,
    Powercard.Ever_Multiplying_Swarm: CardType.Unique,
    Powercard.Exaltation_of_Echoed_Steps: CardType.Unique,
    Powercard.Exaltation_of_Grasping_Roots: CardType.Unique,
    Powercard.Exaltation_of_Molten_Stone: CardType.Unique,
    Powercard.Exaltation_of_Tangled_Growth: CardType.Unique,
    Powercard.Exaltation_of_the_Incandescent_Sky: CardType.Major,
    Powercard.Exhale_Confusion_and_Delirium: CardType.Unique,
    Powercard.Favor_of_the_Sun_and_Star_Lit_Dark: CardType.Minor,
    Powercard.Favors_Called_Due: CardType.Unique,
    Powercard.Ferocious_Rampage: CardType.Unique,
    Powercard.Fetid_Breath_Spreads_Infection: CardType.Unique,
    Powercard.Flocking_Red_Talons: CardType.Major,
    Powercard.Fields_Choked_with_Growth: CardType.Unique,
    Powercard.Fiery_Vengeance: CardType.Unique,
    Powercard.Fire_and_Flood: CardType.Major,
    Powercard.Fire_in_the_Sky: CardType.Minor,
    Powercard.Flames_Fury: CardType.Unique,
    Powercard.Flash_fires: CardType.Unique,
    Powercard.Flash_Floods: CardType.Unique,
    Powercard.Fleshrot_Fever: CardType.Minor,
    Powercard.Flow_Downriver_Blow_Downwind: CardType.Minor,
    Powercard.Flowing_And_Silent_Forms_Dart_By: CardType.Unique,
    Powercard.Flow_Like_Water_Reach_Like_Air: CardType.Major,
    Powercard.Focus_the_Lands_Anguish: CardType.Major,
    Powercard.Forests_of_Living_Obsidian: CardType.Major,
    Powercard.Foundations_Sink_Into_Mud: CardType.Unique,
    Powercard.Foul_Vapors_and_Fetid_Muck: CardType.Unique,
    Powercard.Fragments_of_Yesteryear: CardType.Major,
    Powercard.Frightful_Keening: CardType.Unique,
    Powercard.Gather_the_Scattered_Light_of_Stars: CardType.Unique,
    Powercard.Gift_of_Abundance: CardType.Unique,
    Powercard.Gift_of_Constancy: CardType.Minor,
    Powercard.Gift_of_Flowing_Power: CardType.Unique,
    Powercard.Gift_of_Furious_Might: CardType.Unique,
    Powercard.Gift_of_Living_Energy: CardType.Minor,
    Powercard.Gift_of_Natures_Connection: CardType.Minor,
    Powercard.Gift_of_Power: CardType.Minor,
    Powercard.Gift_of_Proliferation: CardType.Unique,
    Powercard.Gift_of_Searing_Heat: CardType.Unique,
    Powercard.Gift_of_Seismic_Energy: CardType.Unique,
    Powercard.Gift_of_the_Primordial_Deeps: CardType.Unique,
    Powercard.Gift_of_the_Sunlit_Air: CardType.Unique,
    Powercard.Gift_of_the_Untamed_Wild: CardType.Unique,
    Powercard.Gift_of_Twinned_Days: CardType.Minor,
    Powercard.Gift_of_Wind_Sped_Steps: CardType.Unique,
    Powercard.Gnawing_Rootbiters: CardType.Minor,
    Powercard.Golds_Allure: CardType.Minor,
    Powercard.Grant_Hatred_a_Ravenous_Form: CardType.Major,
    Powercard.Grasping_Tide: CardType.Unique,
    Powercard.Growth_Through_Sacrifice: CardType.Minor,
    Powercard.Guardian_Serpents: CardType.Minor,
    Powercard.Guard_the_Healing_Land: CardType.Unique,
    Powercard.Guide_the_Way_on_Feathered_Wings: CardType.Unique,
    Powercard.Harbingers_of_the_Lightning: CardType.Unique,
    Powercard.Haunted_By_Primal_Memories: CardType.Minor,
    Powercard.Hazards_Spread_Across_the_Island: CardType.Minor,
    Powercard.Herd_Towards_the_Lurking_Maw: CardType.Unique,
    Powercard.Here_There_Be_Monsters: CardType.Minor,
    Powercard.Impersonate_Authority: CardType.Unique,
    Powercard.Incite_the_Mob: CardType.Unique,
    Powercard.Inspire_a_Winding_Dance: CardType.Unique,
    Powercard.Indomitable_Claim: CardType.Major,
    Powercard.Infestation_of_Venomous_Spiders: CardType.Major,
    Powercard.Infested_Aquifers: CardType.Minor,
    Powercard.Infinite_Vitality: CardType.Major,
    Powercard.Inflame_the_Fires_of_Life: CardType.Minor,
    Powercard.Insatiable_Hunger_of_the_Swarm: CardType.Major,
    Powercard.Inspire_the_Release_of_Stolen_Lands: CardType.Major,
    Powercard.Instruments_of_Their_Own_Ruin: CardType.Major,
    Powercard.Intractable_Thickets_and_Thorns: CardType.Unique,
    Powercard.Irresistible_Call: CardType.Major,
    Powercard.Jagged_Shards_Push_from_the_Earth: CardType.Unique,
    Powercard.Land_of_Haunts_and_Embers: CardType.Minor,
    Powercard.Lava_Flows: CardType.Unique,
    Powercard.Like_Calls_to_Like: CardType.Minor,
    Powercard.Lightnings_Boon: CardType.Unique,
    Powercard.Lure_of_the_Unknown: CardType.Minor,
    Powercard.Manifestation_of_Power_and_Glory: CardType.Unique,
    Powercard.Manifest_Incarnation: CardType.Major,
    Powercard.Mantle_of_Dread: CardType.Unique,
    Powercard.Mark_Territory_With_Scars_and_Teeth: CardType.Unique,
    Powercard.Mesmerized_Tranquility: CardType.Minor,
    Powercard.Melt_Earth_Into_Quicksand: CardType.Major,
    Powercard.Mists_of_Oblivion: CardType.Major,
    Powercard.Mysterious_Abductions: CardType.Unique,
    Powercard.Natures_Resilience: CardType.Minor,
    Powercard.Offer_Passage_Between_Worlds: CardType.Unique,
    Powercard.Open_Shifting_Waterways: CardType.Unique,
    Powercard.Overenthusiastic_Arson: CardType.Unique,
    Powercard.Overgrow_in_a_Night: CardType.Unique,
    Powercard.Pact_of_the_Joined_Hunt: CardType.Minor,
    Powercard.Paralyzing_Fright: CardType.Major,
    Powercard.Paths_Tied_by_Nature: CardType.Unique,
    Powercard.Peace_of_the_Nighttime_Sky: CardType.Unique,
    Powercard.Pent_Up_Calamity: CardType.Major,
    Powercard.Perils_of_the_Deepest_Island: CardType.Unique,
    Powercard.Pillar_of_Living_Flame: CardType.Major,
    Powercard.Plaguebearers: CardType.Unique,
    Powercard.Plague_Ships_Sail_to_Distant_Ports: CardType.Major,
    Powercard.Plows_Shatter_on_Rocky_Ground: CardType.Unique,
    Powercard.Poisoned_Dew: CardType.Minor,
    Powercard.Poisoned_Land: CardType.Major,
    Powercard.Portents_of_Disaster: CardType.Minor,
    Powercard.Pour_Time_Sideways: CardType.Unique,
    Powercard.Powerstorm: CardType.Major,
    Powercard.Predatory_Nightmares: CardType.Unique,
    Powercard.Prey_on_the_Builders: CardType.Unique,
    Powercard.Promises_of_Protection: CardType.Minor,
    Powercard.Prowling_Panthers: CardType.Minor,
    Powercard.Pull_Beneath_the_Hungry_Earth: CardType.Minor,
    Powercard.Purifying_Flame: CardType.Minor,
    Powercard.Pursue_with_Scratches_Pecks_and_Stings: CardType.Unique,
    Powercard.Pyroclastic_Bombardment: CardType.Unique,
    Powercard.Pyroclastic_Flow: CardType.Major,
    Powercard.Quicken_the_Earths_Struggles: CardType.Minor,
    Powercard.Radiating_Tremors: CardType.Unique,
    Powercard.Radiant_and_Hallowed_Grove: CardType.Unique,
    Powercard.Raging_Storm: CardType.Unique,
    Powercard.Rain_of_Ash: CardType.Unique,
    Powercard.Rain_of_Blood: CardType.Minor,
    Powercard.Ravaged_Undergrowth_Slithers_Back_to_Life: CardType.Major,
    Powercard.Razor_Sharp_Undergrowth: CardType.Minor,
    Powercard.Reaching_Grasp: CardType.Minor,
    Powercard.Regrow_From_Roots: CardType.Unique,
    Powercard.Renewing_Boon: CardType.Minor,
    Powercard.Renewing_Rain: CardType.Minor,
    Powercard.Resounding_Footfalls_Sow_Dismay: CardType.Unique,
    Powercard.Rites_of_the_Lands_Rejection: CardType.Minor,
    Powercard.Rituals_of_Destruction: CardType.Unique,
    Powercard.Rivers_Bounty: CardType.Unique,
    Powercard.Roiling_Bog_and_Snagging_Thorn: CardType.Minor,
    Powercard.Rouse_the_Trees_and_Stones: CardType.Minor,
    Powercard.Rumbling_Earthquakes: CardType.Major,
    Powercard.Rumblings_Portend_a_Greater_Quake: CardType.Unique,
    Powercard.Sap_the_Strength_of_Multitudes: CardType.Minor,
    Powercard.Sacrosanct_Wilderness: CardType.Unique,
    Powercard.Savage_Mawbeasts: CardType.Minor,
    Powercard.Savage_Transformation: CardType.Major,
    Powercard.Scarred_and_Stony_Land: CardType.Unique,
    Powercard.Scatter_to_the_Winds: CardType.Unique,
    Powercard.Scour_the_Land: CardType.Minor,
    Powercard.Scream_Disease_Into_the_Wind: CardType.Minor,
    Powercard.Sea_Monsters: CardType.Major,
    Powercard.Sear_Anger_Into_the_Wild_Lands: CardType.Minor,
    Powercard.Set_Them_on_an_Ever_Twisting_Trail: CardType.Minor,
    Powercard.Settle_Into_Hunting_Grounds: CardType.Major,
    Powercard.Shadows_of_the_Burning_Forest: CardType.Minor,
    Powercard.Shape_the_Self_Anew: CardType.Unique,
    Powercard.Share_Secrets_of_Survival: CardType.Unique,
    Powercard.Shatter_Homesteads: CardType.Unique,
    Powercard.Skies_Herald_the_Season_of_Return: CardType.Minor,
    Powercard.Sky_Stretches_to_Shore: CardType.Minor,
    Powercard.Sleep_and_Never_Waken: CardType.Major,
    Powercard.Smothering_Infestation: CardType.Major,
    Powercard.Softly_Beckon_Ever_Inward: CardType.Unique,
    Powercard.Solidify_Echoes_of_Majesty_Past: CardType.Major,
    Powercard.Song_of_Sanctity: CardType.Minor,
    Powercard.Spill_Bitterness_Into_the_Earth: CardType.Major,
    Powercard.Spur_On_with_Words_of_Fire: CardType.Minor,
    Powercard.Steam_Vents: CardType.Minor,
    Powercard.Stem_the_Flow_of_Fresh_Water: CardType.Unique,
    Powercard.Stinging_Sandstorm: CardType.Unique,
    Powercard.Storm_Swath: CardType.Major,
    Powercard.Strangling_Firevine: CardType.Major,
    Powercard.Strike_Low_with_Sudden_Fevers: CardType.Unique,
    Powercard.Strong_And_Constant_Currents: CardType.Minor,
    Powercard.Stubborn_Solidity: CardType.Unique,
    Powercard.Study_the_Invaders_Fears: CardType.Unique,
    Powercard.Sucking_Ooze: CardType.Minor,
    Powercard.Sudden_Ambush: CardType.Unique,
    Powercard.Sunsets_Fire_Flows_Across_the_Land: CardType.Minor,
    Powercard.Surging_Lahar: CardType.Unique,
    Powercard.Swallowed_by_the_Wilderness: CardType.Unique,
    Powercard.Swallow_the_Land_Dwellers: CardType.Unique,
    Powercard.Swarming_Wasps: CardType.Minor,
    Powercard.Sweep_into_the_Sea: CardType.Major,
    Powercard.Sweltering_Exhaustion: CardType.Unique,
    Powercard.Talons_of_Lightning: CardType.Major,
    Powercard.Teeming_Rivers: CardType.Minor,
    Powercard.Teeth_Gleam_from_Darkness: CardType.Unique,
    Powercard.Tempest_of_Leaves_and_Branches: CardType.Unique,
    Powercard.Terrifying_Chase: CardType.Unique,
    Powercard.Terrifying_Nightmares: CardType.Major,
    Powercard.Terrifying_Rampage: CardType.Unique,
    Powercard.Territorial_Strife: CardType.Minor,
    Powercard.Terror_Turns_to_Madness: CardType.Minor,
    Powercard.The_Fog_Closes_In: CardType.Unique,
    Powercard.The_Jungle_Hungers: CardType.Major,
    Powercard.The_Land_Thrashes_in_Furious_Pain: CardType.Major,
    Powercard.The_Past_Returns_Again: CardType.Unique,
    Powercard.The_Trees_and_Stones_Speak_of_War: CardType.Major,
    Powercard.The_Shore_Seethes_With_Hatred: CardType.Minor,
    Powercard.The_Wounded_Wild_Turns_on_its_Assailants: CardType.Major,
    Powercard.Thickets_Erupt_with_Every_Touch_of_Breeze: CardType.Major,
    Powercard.Tigers_Hunting: CardType.Major,
    Powercard.Threatening_Flames: CardType.Unique,
    Powercard.Thriving_Chokefungus: CardType.Minor,
    Powercard.Tidal_Boon: CardType.Unique,
    Powercard.Too_Near_the_Jungle: CardType.Unique,
    Powercard.Tormenting_Rotflies: CardType.Minor,
    Powercard.Towering_Wrath: CardType.Unique,
    Powercard.Transformative_Sacrifice: CardType.Major,
    Powercard.Transform_to_a_Murderous_Darkness: CardType.Major,
    Powercard.Travelers_Boon: CardType.Unique,
    Powercard.Treacherous_Waterways: CardType.Minor,
    Powercard.Trees_Radiate_Celestial_Brilliance: CardType.Major,
    Powercard.Tsunami: CardType.Major,
    Powercard.Turmoils_Touch: CardType.Unique,
    Powercard.Twilight_Fog_Brings_Madness: CardType.Minor,
    Powercard.Twist_Perceptions: CardType.Unique,
    Powercard.Twisted_Flowers_Murmur_Ultimatums: CardType.Major,
    Powercard.Unbearable_Deluge: CardType.Unique,
    Powercard.Uncanny_Melting: CardType.Minor,
    Powercard.Unearth_a_Beast_of_Wrathful_Stone: CardType.Major,
    Powercard.Unexpected_Tigers: CardType.Unique,
    Powercard.Unleash_a_Torrent_of_the_Selfs_Own_Essence: CardType.Major,
    Powercard.Unlock_the_Gates_of_Deepest_Power: CardType.Major,
    Powercard.Unnerving_Pall: CardType.Unique,
    Powercard.Unquenchable_Flames: CardType.Minor,
    Powercard.Unrelenting_Growth: CardType.Major,
    Powercard.Vanish_Softly_Away_Forgotten_by_All: CardType.Major,
    Powercard.Utter_a_Curse_of_Dread_and_Bone: CardType.Major,
    Powercard.Voice_of_Command: CardType.Major,
    Powercard.Volcanic_Eruption: CardType.Major,
    Powercard.Veil_the_Nights_Hunt: CardType.Minor,
    Powercard.Vengeance_of_the_Dead: CardType.Major,
    Powercard.Vigor_of_the_Breaking_Dawn: CardType.Major,
    Powercard.Visions_of_Fiery_Doom: CardType.Minor,
    Powercard.Voice_of_Thunder: CardType.Unique,
    Powercard.Voracious_Growth: CardType.Minor,
    Powercard.Walls_of_Rock_and_Thorn: CardType.Major,
    Powercard.Wash_Away: CardType.Unique,
    Powercard.Ways_of_Shore_and_Heartland: CardType.Unique,
    Powercard.Weave_Together_the_Fabric_of_Place: CardType.Major,
    Powercard.Weep_for_What_Is_Lost: CardType.Minor,
    Powercard.Whispered_Guidance_Through_the_Night: CardType.Unique,
    Powercard.Winds_of_Rust_and_Atrophy: CardType.Major,
    Powercard.Words_of_Warning: CardType.Unique,
    Powercard.Wrap_in_Wings_of_Sunlight: CardType.Major,
    Powercard.Belligerent_and_Aggressive_Crops: CardType.Unique,
    Powercard.Emerge_from_the_Dread_Night_Wind: CardType.Unique,
    Powercard.Reach_from_the_Infinite_Darkness: CardType.Unique,
    Powercard.Swallowed_by_the_Endless_Dark: CardType.Unique,
    Powercard.Terror_of_the_Hunted: CardType.Unique,
    Powercard.Call_to_Vigilance: CardType.Unique,
    Powercard.Coordinated_Raid: CardType.Unique,
    Powercard.Favors_of_Story_and_Season: CardType.Unique,
    Powercard.Surrounded_by_the_Dahan: CardType.Unique,
    Powercard.Smite_the_Land_with_Fulmination: CardType.Unique,
    Powercard.Blinding_Glare: CardType.Unique,
    Powercard.Focus_the_Suns_Rays: CardType.Unique,
    Powercard.Unbearable_Gaze: CardType.Unique,
    Powercard.Wither_Bodies_Scar_Stones: CardType.Unique,
    Powercard.Blood_Water_and_Bloodlust: CardType.Unique,
    Powercard.Boon_of_Corrupted_Blood: CardType.Unique,
    Powercard.Draw_to_the_Waters_Edge: CardType.Unique,
    Powercard.Wrack_with_Pain_and_Grief: CardType.Unique,
}

unique_to_spirit = {
    Powercard.Absolute_Stasis: Spirit.Fractured,
    Powercard.Absorb_Essence: Spirit.Snek,
    Powercard.A_Circuitous_and_Wending_Journey: Spirit.Finder,
    Powercard.A_Dreadful_Tide_of_Scurrying_Flesh: Spirit.MM,
    Powercard.Aid_from_the_Spirit_Speakers: Spirit.Finder,
    Powercard.A_Year_of_Perfect_Stillness: Spirit.Earth,
    Powercard.Asphyxiating_Smoke: Spirit.Wildfire,
    Powercard.Blazing_Intimidation: Spirit.Behemoth,
    Powercard.Blooming_of_the_Rocks_and_Trees: Spirit.Roots,
    Powercard.Blur_the_Arc_of_Years: Spirit.Fractured,
    Powercard.Boon_of_Ancient_Memories: Spirit.Memory,
    Powercard.Boon_of_Growing_Power: Spirit.Keeper,
    Powercard.Boon_of_Reimagining: Spirit.Starlight,
    Powercard.Boon_of_Resilient_Power: Spirit.Roots,
    Powercard.Boon_of_Swarming_Bedevilment: Spirit.MM,
    Powercard.Boon_of_Vigor: Spirit.River,
    Powercard.Boon_of_Watchful_Guarding: Spirit.Eyes,
    Powercard.Call_of_the_Deeps: Spirit.Ocean,
    Powercard.Call_on_Herders_for_Aid: Spirit.Heat,
    Powercard.Call_on_Midnights_Dreams: Spirit.Bringer,
    Powercard.Concealing_Shadows: Spirit.Shadows,
    Powercard.Crops_Wither_and_Fade: Spirit.Shadows,
    Powercard.Dark_Skies_Loose_A_Stinging_Rain: Spirit.Downpour,
    Powercard.Dissolving_Vapors: Spirit.Shroud,
    Powercard.Draw_of_the_Fruitful_Earth: Spirit.Earth,
    Powercard.Dread_Apparitions: Spirit.Bringer,
    Powercard.Dreams_of_the_Dahan: Spirit.Bringer,
    Powercard.Eerie_Noises_and_Moving_Trees: Spirit.Eyes,
    Powercard.Elemental_Teachings: Spirit.Memory,
    Powercard.Elemental_Aegis: Spirit.Snek,
    Powercard.Entwine_the_Fates_of_All: Spirit.Roots,
    Powercard.Ever_Multiplying_Swarm: Spirit.MM,
    Powercard.Exaltation_of_Echoed_Steps: Spirit.Earthquakes,
    Powercard.Exaltation_of_Grasping_Roots: Spirit.Behemoth,
    Powercard.Exaltation_of_Molten_Stone: Spirit.Volcano,
    Powercard.Exaltation_of_Tangled_Growth: Spirit.Otter,
    Powercard.Exhale_Confusion_and_Delirium: Spirit.Voice,
    Powercard.Favors_Called_Due: Spirit.Shadows,
    Powercard.Ferocious_Rampage: Spirit.Teeth,
    Powercard.Fetid_Breath_Spreads_Infection: Spirit.Vengeance,
    Powercard.Fields_Choked_with_Growth: Spirit.Green,
    Powercard.Fiery_Vengeance: Spirit.Vengeance,
    Powercard.Flames_Fury: Spirit.Wildfire,
    Powercard.Flash_fires: Spirit.Wildfire,
    Powercard.Flash_Floods: Spirit.River,
    Powercard.Flowing_And_Silent_Forms_Dart_By: Spirit.Shroud,
    Powercard.Foundations_Sink_Into_Mud: Spirit.Downpour,
    Powercard.Foul_Vapors_and_Fetid_Muck: Spirit.Otter,
    Powercard.Frightful_Keening: Spirit.Voice,
    Powercard.Gather_the_Scattered_Light_of_Stars: Spirit.Starlight,
    Powercard.Gift_of_Abundance: Spirit.Downpour,
    Powercard.Gift_of_Flowing_Power: Spirit.Snek,
    Powercard.Gift_of_Furious_Might: Spirit.Teeth,
    Powercard.Gift_of_Proliferation: Spirit.Green,
    Powercard.Gift_of_Searing_Heat: Spirit.Heat,
    Powercard.Gift_of_Seismic_Energy: Spirit.Earthquakes,
    Powercard.Gift_of_the_Primordial_Deeps: Spirit.Snek,
    Powercard.Gift_of_the_Sunlit_Air: Spirit.Whirlwind,
    Powercard.Gift_of_the_Untamed_Wild: Spirit.Lure,
    Powercard.Gift_of_Wind_Sped_Steps: Spirit.Whirlwind,
    Powercard.Grasping_Tide: Spirit.Ocean,
    Powercard.Guard_the_Healing_Land: Spirit.Earth,
    Powercard.Guide_the_Way_on_Feathered_Wings: Spirit.MM,
    Powercard.Harbingers_of_the_Lightning: Spirit.Lightning,
    Powercard.Herd_Towards_the_Lurking_Maw: Spirit.Teeth,
    Powercard.Impersonate_Authority: Spirit.Trickster,
    Powercard.Incite_the_Mob: Spirit.Trickster,
    Powercard.Inspire_a_Winding_Dance: Spirit.Earthquakes,
    Powercard.Intractable_Thickets_and_Thorns: Spirit.Otter,
    Powercard.Jagged_Shards_Push_from_the_Earth: Spirit.Stone,
    Powercard.Lava_Flows: Spirit.Volcano,
    Powercard.Lightnings_Boon: Spirit.Lightning,
    Powercard.Manifestation_of_Power_and_Glory: Spirit.Thunderspeaker,
    Powercard.Mantle_of_Dread: Spirit.Shadows,
    Powercard.Mark_Territory_With_Scars_and_Teeth: Spirit.Teeth,
    Powercard.Mysterious_Abductions: Spirit.Eyes,
    Powercard.Offer_Passage_Between_Worlds: Spirit.Finder,
    Powercard.Open_Shifting_Waterways: Spirit.Otter,
    Powercard.Overenthusiastic_Arson: Spirit.Trickster,
    Powercard.Overgrow_in_a_Night: Spirit.Green,
    Powercard.Paths_Tied_by_Nature: Spirit.Finder,
    Powercard.Peace_of_the_Nighttime_Sky: Spirit.Starlight,
    Powercard.Perils_of_the_Deepest_Island: Spirit.Lure,
    Powercard.Plaguebearers: Spirit.Vengeance,
    Powercard.Plows_Shatter_on_Rocky_Ground: Spirit.Stone,
    Powercard.Pour_Time_Sideways: Spirit.Fractured,
    Powercard.Predatory_Nightmares: Spirit.Bringer,
    Powercard.Prey_on_the_Builders: Spirit.Fangs,
    Powercard.Pursue_with_Scratches_Pecks_and_Stings: Spirit.MM,
    Powercard.Pyroclastic_Bombardment: Spirit.Volcano,
    Powercard.Radiating_Tremors: Spirit.Earthquakes,
    Powercard.Radiant_and_Hallowed_Grove: Spirit.Roots,
    Powercard.Raging_Storm: Spirit.Lightning,
    Powercard.Rain_of_Ash: Spirit.Volcano,
    Powercard.Regrow_From_Roots: Spirit.Keeper,
    Powercard.Resounding_Footfalls_Sow_Dismay: Spirit.Earthquakes,
    Powercard.Rituals_of_Destruction: Spirit.Earth,
    Powercard.Rivers_Bounty: Spirit.River,
    Powercard.Rumblings_Portend_a_Greater_Quake: Spirit.Earthquakes,
    Powercard.Sacrosanct_Wilderness: Spirit.Keeper,
    Powercard.Scarred_and_Stony_Land: Spirit.Stone,
    Powercard.Scatter_to_the_Winds: Spirit.Whirlwind,
    Powercard.Shape_the_Self_Anew: Spirit.Starlight,
    Powercard.Share_Secrets_of_Survival: Spirit.Memory,
    Powercard.Shatter_Homesteads: Spirit.Lightning,
    Powercard.Softly_Beckon_Ever_Inward: Spirit.Lure,
    Powercard.Stem_the_Flow_of_Fresh_Water: Spirit.Green,
    Powercard.Stinging_Sandstorm: Spirit.Heat,
    Powercard.Strike_Low_with_Sudden_Fevers: Spirit.Vengeance,
    Powercard.Stubborn_Solidity: Spirit.Stone,
    Powercard.Study_the_Invaders_Fears: Spirit.Memory,
    Powercard.Sudden_Ambush: Spirit.Thunderspeaker,
    Powercard.Surging_Lahar: Spirit.Behemoth,
    Powercard.Swallowed_by_the_Wilderness: Spirit.Lure,
    Powercard.Swallow_the_Land_Dwellers: Spirit.Ocean,
    Powercard.Sweltering_Exhaustion: Spirit.Heat,
    Powercard.Teeth_Gleam_from_Darkness: Spirit.Fangs,
    Powercard.Tempest_of_Leaves_and_Branches: Spirit.Whirlwind,
    Powercard.Terrifying_Chase: Spirit.Fangs,
    Powercard.Terrifying_Rampage: Spirit.Behemoth,
    Powercard.The_Fog_Closes_In: Spirit.Shroud,
    Powercard.The_Past_Returns_Again: Spirit.Fractured,
    Powercard.Threatening_Flames: Spirit.Wildfire,
    Powercard.Tidal_Boon: Spirit.Ocean,
    Powercard.Too_Near_the_Jungle: Spirit.Fangs,
    Powercard.Towering_Wrath: Spirit.Keeper,
    Powercard.Travelers_Boon: Spirit.Finder,
    Powercard.Turmoils_Touch: Spirit.Voice,
    Powercard.Twist_Perceptions: Spirit.Voice,
    Powercard.Unbearable_Deluge: Spirit.Downpour,
    Powercard.Unexpected_Tigers: Spirit.Trickster,
    Powercard.Unnerving_Pall: Spirit.Shroud,
    Powercard.Voice_of_Thunder: Spirit.Thunderspeaker,
    Powercard.Wash_Away: Spirit.River,
    Powercard.Ways_of_Shore_and_Heartland: Spirit.Finder,
    Powercard.Whispered_Guidance_Through_the_Night: Spirit.Eyes,
    Powercard.Words_of_Warning: Spirit.Thunderspeaker,
    Powercard.Belligerent_and_Aggressive_Crops: Spirit.Green,
    Powercard.Emerge_from_the_Dread_Night_Wind: Spirit.BODDYS,
    Powercard.Reach_from_the_Infinite_Darkness: Spirit.BODDYS,
    Powercard.Swallowed_by_the_Endless_Dark: Spirit.BODDYS,
    Powercard.Terror_of_the_Hunted: Spirit.BODDYS,
    Powercard.Call_to_Vigilance: Spirit.HearthVigil,
    Powercard.Coordinated_Raid: Spirit.HearthVigil,
    Powercard.Favors_of_Story_and_Season: Spirit.HearthVigil,
    Powercard.Surrounded_by_the_Dahan: Spirit.HearthVigil,
    Powercard.Smite_the_Land_with_Fulmination: Spirit.Lightning,
    Powercard.Blinding_Glare: Spirit.Gaze,
    Powercard.Focus_the_Suns_Rays: Spirit.Gaze,
    Powercard.Unbearable_Gaze: Spirit.Gaze,
    Powercard.Wither_Bodies_Scar_Stones: Spirit.Gaze,
    Powercard.Blood_Water_and_Bloodlust: Spirit.WWB,
    Powercard.Boon_of_Corrupted_Blood: Spirit.WWB,
    Powercard.Draw_to_the_Waters_Edge: Spirit.WWB,
    Powercard.Wrack_with_Pain_and_Grief: Spirit.WWB,
}

card_to_expansion = {
    Powercard.Absolute_Stasis: ContentSource.JE,
    Powercard.Absorb_Essence: ContentSource.PP1,
    Powercard.Absorb_Corruption: ContentSource.BC,
    Powercard.Accelerated_Rot: ContentSource.BASE,
    Powercard.A_Circuitous_and_Wending_Journey: ContentSource.PP2,
    Powercard.A_Dreadful_Tide_of_Scurrying_Flesh: ContentSource.JE,
    Powercard.Aid_from_the_Spirit_Speakers: ContentSource.PP2,
    Powercard.Animated_Wrackroot: ContentSource.BC,
    Powercard.Angry_Bears: ContentSource.JE,
    Powercard.A_Year_of_Perfect_Stillness: ContentSource.BASE,
    Powercard.Asphyxiating_Smoke: ContentSource.PP1,
    Powercard.Bargain_of_Coursing_Paths: ContentSource.NI,
    Powercard.Bargains_of_Power_and_Protection: ContentSource.JE,
    Powercard.Bats_Scout_For_Raids_By_Darkness: ContentSource.JE,
    Powercard.Birds_Cry_Warning: ContentSource.JE,
    Powercard.Blazing_Intimidation: ContentSource.NI,
    Powercard.Blazing_Renewal: ContentSource.BASE,
    Powercard.Blood_Draws_Predators: ContentSource.JE,
    Powercard.Bloodwrack_Plague: ContentSource.BC,
    Powercard.Blooming_of_the_Rocks_and_Trees: ContentSource.NI,
    Powercard.Blur_the_Arc_of_Years: ContentSource.JE,
    Powercard.Bombard_with_Boulders_and_Stinging_Seeds: ContentSource.NI,
    Powercard.Boon_of_Ancient_Memories: ContentSource.JE,
    Powercard.Boon_of_Growing_Power: ContentSource.BC,
    Powercard.Boon_of_Reimagining: ContentSource.JE,
    Powercard.Boon_of_Resilient_Power: ContentSource.NI,
    Powercard.Boon_of_Swarming_Bedevilment: ContentSource.JE,
    Powercard.Boon_of_Vigor: ContentSource.BASE,
    Powercard.Boon_of_Watchful_Guarding: ContentSource.HORIZONS,
    Powercard.Call_of_the_Dahan_Ways: ContentSource.BASE,
    Powercard.Call_of_the_Deeps: ContentSource.BASE,
    Powercard.Call_on_Herders_for_Aid: ContentSource.HORIZONS,
    Powercard.Call_on_Midnights_Dreams: ContentSource.BASE,
    Powercard.Call_to_Bloodshed: ContentSource.BASE,
    Powercard.Call_to_Ferocity: ContentSource.BC,
    Powercard.Call_to_Guard: ContentSource.JE,
    Powercard.Call_to_Isolation: ContentSource.BASE,
    Powercard.Call_to_Migrate: ContentSource.BASE,
    Powercard.Call_to_Tend: ContentSource.BASE,
    Powercard.Call_to_Trade: ContentSource.BC,
    Powercard.Carapaced_Land: ContentSource.JE,
    Powercard.Cast_Down_into_the_Briny_Deep: ContentSource.BC,
    Powercard.Cleansing_Floods: ContentSource.BASE,
    Powercard.Concealing_Shadows: ContentSource.BASE,
    Powercard.Confounding_Mists: ContentSource.BC,
    Powercard.Crops_Wither_and_Fade: ContentSource.BASE,
    Powercard.Cycles_of_Time_and_Tide: ContentSource.BC,
    Powercard.Dark_and_Tangled_Woods: ContentSource.BASE,
    Powercard.Dark_Skies_Loose_A_Stinging_Rain: ContentSource.PP2,
    Powercard.Death_Falls_Gently_From_Open_Blossoms: ContentSource.BC,
    Powercard.Delusions_of_Danger: ContentSource.BASE,
    Powercard.Desiccating_Winds: ContentSource.JE,
    Powercard.Devouring_Ants: ContentSource.BASE,
    Powercard.Dire_Metamorphosis: ContentSource.JE,
    Powercard.Disorienting_Landscape: ContentSource.BC,
    Powercard.Dissolve_the_Bonds_of_Kinship: ContentSource.BASE,
    Powercard.Dissolving_Vapors: ContentSource.JE,
    Powercard.Domesticated_Animals_Go_Berserk: ContentSource.JE,
    Powercard.Draw_of_the_Fruitful_Earth: ContentSource.BASE,
    Powercard.Draw_Towards_a_Consuming_Void: ContentSource.JE,
    Powercard.Dread_Apparitions: ContentSource.BASE,
    Powercard.Dream_of_the_Untouched_Land: ContentSource.JE,
    Powercard.Dreams_of_the_Dahan: ContentSource.BASE,
    Powercard.Drift_Down_into_Slumber: ContentSource.BASE,
    Powercard.Drought: ContentSource.BASE,
    Powercard.Dry_Wood_Explodes_in_Smoldering_Splinters: ContentSource.JE,
    Powercard.Eerie_Noises_and_Moving_Trees: ContentSource.HORIZONS,
    Powercard.Elemental_Boon: ContentSource.BASE,
    Powercard.Elemental_Teachings: ContentSource.JE,
    Powercard.Elusive_Ambushes: ContentSource.BC,
    Powercard.Encompassing_Ward: ContentSource.BASE,
    Powercard.Entrap_the_Forces_of_Corruption: ContentSource.JE,
    Powercard.Elemental_Aegis: ContentSource.PP1,
    Powercard.Enticing_Splendor: ContentSource.BASE,
    Powercard.Entrancing_Apparitions: ContentSource.BASE,
    Powercard.Entwined_Power: ContentSource.BASE,
    Powercard.Entwine_the_Fates_of_All: ContentSource.NI,
    Powercard.Ever_Multiplying_Swarm: ContentSource.JE,
    Powercard.Exaltation_of_Echoed_Steps: ContentSource.NI,
    Powercard.Exaltation_of_Grasping_Roots: ContentSource.NI,
    Powercard.Exaltation_of_Molten_Stone: ContentSource.JE,
    Powercard.Exaltation_of_Tangled_Growth: ContentSource.HORIZONS,
    Powercard.Exaltation_of_the_Incandescent_Sky: ContentSource.NI,
    Powercard.Exhale_Confusion_and_Delirium: ContentSource.NI,
    Powercard.Favor_of_the_Sun_and_Star_Lit_Dark: ContentSource.JE,
    Powercard.Favors_Called_Due: ContentSource.BASE,
    Powercard.Ferocious_Rampage: ContentSource.HORIZONS,
    Powercard.Fetid_Breath_Spreads_Infection: ContentSource.JE,
    Powercard.Flocking_Red_Talons: ContentSource.NI,
    Powercard.Fields_Choked_with_Growth: ContentSource.BASE,
    Powercard.Fiery_Vengeance: ContentSource.JE,
    Powercard.Fire_and_Flood: ContentSource.BC,
    Powercard.Fire_in_the_Sky: ContentSource.BC,
    Powercard.Flames_Fury: ContentSource.PP1,
    Powercard.Flash_fires: ContentSource.PP1,
    Powercard.Flash_Floods: ContentSource.BASE,
    Powercard.Fleshrot_Fever: ContentSource.BC,
    Powercard.Flow_Downriver_Blow_Downwind: ContentSource.JE,
    Powercard.Flowing_And_Silent_Forms_Dart_By: ContentSource.JE,
    Powercard.Flow_Like_Water_Reach_Like_Air: ContentSource.BC,
    Powercard.Focus_the_Lands_Anguish: ContentSource.JE,
    Powercard.Forests_of_Living_Obsidian: ContentSource.JE,
    Powercard.Foundations_Sink_Into_Mud: ContentSource.PP2,
    Powercard.Foul_Vapors_and_Fetid_Muck: ContentSource.HORIZONS,
    Powercard.Fragments_of_Yesteryear: ContentSource.NI,
    Powercard.Frightful_Keening: ContentSource.NI,
    Powercard.Gather_the_Scattered_Light_of_Stars: ContentSource.JE,
    Powercard.Gift_of_Abundance: ContentSource.PP2,
    Powercard.Gift_of_Constancy: ContentSource.BASE,
    Powercard.Gift_of_Flowing_Power: ContentSource.PP1,
    Powercard.Gift_of_Furious_Might: ContentSource.HORIZONS,
    Powercard.Gift_of_Living_Energy: ContentSource.BASE,
    Powercard.Gift_of_Natures_Connection: ContentSource.JE,
    Powercard.Gift_of_Power: ContentSource.BASE,
    Powercard.Gift_of_Proliferation: ContentSource.BASE,
    Powercard.Gift_of_Searing_Heat: ContentSource.HORIZONS,
    Powercard.Gift_of_Seismic_Energy: ContentSource.NI,
    Powercard.Gift_of_the_Primordial_Deeps: ContentSource.PP1,
    Powercard.Gift_of_the_Sunlit_Air: ContentSource.HORIZONS,
    Powercard.Gift_of_the_Untamed_Wild: ContentSource.JE,
    Powercard.Gift_of_Twinned_Days: ContentSource.JE,
    Powercard.Gift_of_Wind_Sped_Steps: ContentSource.HORIZONS,
    Powercard.Gnawing_Rootbiters: ContentSource.BASE,
    Powercard.Golds_Allure: ContentSource.BC,
    Powercard.Grant_Hatred_a_Ravenous_Form: ContentSource.BC,
    Powercard.Grasping_Tide: ContentSource.BASE,
    Powercard.Growth_Through_Sacrifice: ContentSource.BC,
    Powercard.Guardian_Serpents: ContentSource.BC,
    Powercard.Guard_the_Healing_Land: ContentSource.BASE,
    Powercard.Guide_the_Way_on_Feathered_Wings: ContentSource.JE,
    Powercard.Harbingers_of_the_Lightning: ContentSource.BASE,
    Powercard.Haunted_By_Primal_Memories: ContentSource.JE,
    Powercard.Hazards_Spread_Across_the_Island: ContentSource.JE,
    Powercard.Herd_Towards_the_Lurking_Maw: ContentSource.HORIZONS,
    Powercard.Here_There_Be_Monsters: ContentSource.BC,
    Powercard.Impersonate_Authority: ContentSource.JE,
    Powercard.Incite_the_Mob: ContentSource.JE,
    Powercard.Inspire_a_Winding_Dance: ContentSource.NI,
    Powercard.Indomitable_Claim: ContentSource.BASE,
    Powercard.Infestation_of_Venomous_Spiders: ContentSource.JE,
    Powercard.Infested_Aquifers: ContentSource.BC,
    Powercard.Infinite_Vitality: ContentSource.BASE,
    Powercard.Inflame_the_Fires_of_Life: ContentSource.BC,
    Powercard.Insatiable_Hunger_of_the_Swarm: ContentSource.BC,
    Powercard.Inspire_the_Release_of_Stolen_Lands: ContentSource.NI,
    Powercard.Instruments_of_Their_Own_Ruin: ContentSource.BC,
    Powercard.Intractable_Thickets_and_Thorns: ContentSource.HORIZONS,
    Powercard.Irresistible_Call: ContentSource.JE,
    Powercard.Jagged_Shards_Push_from_the_Earth: ContentSource.JE,
    Powercard.Land_of_Haunts_and_Embers: ContentSource.BASE,
    Powercard.Lava_Flows: ContentSource.JE,
    Powercard.Like_Calls_to_Like: ContentSource.JE,
    Powercard.Lightnings_Boon: ContentSource.BASE,
    Powercard.Lure_of_the_Unknown: ContentSource.BASE,
    Powercard.Manifestation_of_Power_and_Glory: ContentSource.BASE,
    Powercard.Manifest_Incarnation: ContentSource.BC,
    Powercard.Mantle_of_Dread: ContentSource.BASE,
    Powercard.Mark_Territory_With_Scars_and_Teeth: ContentSource.HORIZONS,
    Powercard.Mesmerized_Tranquility: ContentSource.JE,
    Powercard.Melt_Earth_Into_Quicksand: ContentSource.JE,
    Powercard.Mists_of_Oblivion: ContentSource.BASE,
    Powercard.Mysterious_Abductions: ContentSource.HORIZONS,
    Powercard.Natures_Resilience: ContentSource.BASE,
    Powercard.Offer_Passage_Between_Worlds: ContentSource.PP2,
    Powercard.Open_Shifting_Waterways: ContentSource.HORIZONS,
    Powercard.Overenthusiastic_Arson: ContentSource.JE,
    Powercard.Overgrow_in_a_Night: ContentSource.BASE,
    Powercard.Pact_of_the_Joined_Hunt: ContentSource.BC,
    Powercard.Paralyzing_Fright: ContentSource.BASE,
    Powercard.Paths_Tied_by_Nature: ContentSource.PP2,
    Powercard.Peace_of_the_Nighttime_Sky: ContentSource.JE,
    Powercard.Pent_Up_Calamity: ContentSource.BC,
    Powercard.Perils_of_the_Deepest_Island: ContentSource.JE,
    Powercard.Pillar_of_Living_Flame: ContentSource.BASE,
    Powercard.Plaguebearers: ContentSource.JE,
    Powercard.Plague_Ships_Sail_to_Distant_Ports: ContentSource.NI,
    Powercard.Plows_Shatter_on_Rocky_Ground: ContentSource.JE,
    Powercard.Poisoned_Dew: ContentSource.BC,
    Powercard.Poisoned_Land: ContentSource.BASE,
    Powercard.Portents_of_Disaster: ContentSource.BC,
    Powercard.Pour_Time_Sideways: ContentSource.JE,
    Powercard.Powerstorm: ContentSource.BASE,
    Powercard.Predatory_Nightmares: ContentSource.BASE,
    Powercard.Prey_on_the_Builders: ContentSource.BC,
    Powercard.Promises_of_Protection: ContentSource.BC,
    Powercard.Prowling_Panthers: ContentSource.BC,
    Powercard.Pull_Beneath_the_Hungry_Earth: ContentSource.BASE,
    Powercard.Purifying_Flame: ContentSource.BASE,
    Powercard.Pursue_with_Scratches_Pecks_and_Stings: ContentSource.JE,
    Powercard.Pyroclastic_Bombardment: ContentSource.JE,
    Powercard.Pyroclastic_Flow: ContentSource.BC,
    Powercard.Quicken_the_Earths_Struggles: ContentSource.BASE,
    Powercard.Radiating_Tremors: ContentSource.NI,
    Powercard.Radiant_and_Hallowed_Grove: ContentSource.NI,
    Powercard.Raging_Storm: ContentSource.BASE,
    Powercard.Rain_of_Ash: ContentSource.JE,
    Powercard.Rain_of_Blood: ContentSource.BASE,
    Powercard.Ravaged_Undergrowth_Slithers_Back_to_Life: ContentSource.NI,
    Powercard.Razor_Sharp_Undergrowth: ContentSource.BC,
    Powercard.Reaching_Grasp: ContentSource.BASE,
    Powercard.Regrow_From_Roots: ContentSource.BC,
    Powercard.Renewing_Boon: ContentSource.JE,
    Powercard.Renewing_Rain: ContentSource.BC,
    Powercard.Resounding_Footfalls_Sow_Dismay: ContentSource.NI,
    Powercard.Rites_of_the_Lands_Rejection: ContentSource.BC,
    Powercard.Rituals_of_Destruction: ContentSource.BASE,
    Powercard.Rivers_Bounty: ContentSource.BASE,
    Powercard.Roiling_Bog_and_Snagging_Thorn: ContentSource.BC,
    Powercard.Rouse_the_Trees_and_Stones: ContentSource.BASE,
    Powercard.Rumbling_Earthquakes: ContentSource.NI,
    Powercard.Rumblings_Portend_a_Greater_Quake: ContentSource.NI,
    Powercard.Sap_the_Strength_of_Multitudes: ContentSource.BASE,
    Powercard.Sacrosanct_Wilderness: ContentSource.BC,
    Powercard.Savage_Mawbeasts: ContentSource.BASE,
    Powercard.Savage_Transformation: ContentSource.BC,
    Powercard.Scarred_and_Stony_Land: ContentSource.JE,
    Powercard.Scatter_to_the_Winds: ContentSource.HORIZONS,
    Powercard.Scour_the_Land: ContentSource.BC,
    Powercard.Scream_Disease_Into_the_Wind: ContentSource.JE,
    Powercard.Sea_Monsters: ContentSource.BC,
    Powercard.Sear_Anger_Into_the_Wild_Lands: ContentSource.JE,
    Powercard.Set_Them_on_an_Ever_Twisting_Trail: ContentSource.JE,
    Powercard.Settle_Into_Hunting_Grounds: ContentSource.JE,
    Powercard.Shadows_of_the_Burning_Forest: ContentSource.BASE,
    Powercard.Shape_the_Self_Anew: ContentSource.JE,
    Powercard.Share_Secrets_of_Survival: ContentSource.JE,
    Powercard.Shatter_Homesteads: ContentSource.BASE,
    Powercard.Skies_Herald_the_Season_of_Return: ContentSource.JE,
    Powercard.Sky_Stretches_to_Shore: ContentSource.BC,
    Powercard.Sleep_and_Never_Waken: ContentSource.JE,
    Powercard.Smothering_Infestation: ContentSource.BC,
    Powercard.Softly_Beckon_Ever_Inward: ContentSource.JE,
    Powercard.Solidify_Echoes_of_Majesty_Past: ContentSource.NI,
    Powercard.Song_of_Sanctity: ContentSource.BASE,
    Powercard.Spill_Bitterness_Into_the_Earth: ContentSource.JE,
    Powercard.Spur_On_with_Words_of_Fire: ContentSource.BC,
    Powercard.Steam_Vents: ContentSource.BASE,
    Powercard.Stem_the_Flow_of_Fresh_Water: ContentSource.BASE,
    Powercard.Stinging_Sandstorm: ContentSource.HORIZONS,
    Powercard.Storm_Swath: ContentSource.JE,
    Powercard.Strangling_Firevine: ContentSource.BC,
    Powercard.Strike_Low_with_Sudden_Fevers: ContentSource.JE,
    Powercard.Strong_And_Constant_Currents: ContentSource.JE,
    Powercard.Stubborn_Solidity: ContentSource.JE,
    Powercard.Study_the_Invaders_Fears: ContentSource.JE,
    Powercard.Sucking_Ooze: ContentSource.JE,
    Powercard.Sudden_Ambush: ContentSource.BASE,
    Powercard.Sunsets_Fire_Flows_Across_the_Land: ContentSource.JE,
    Powercard.Surging_Lahar: ContentSource.NI,
    Powercard.Swallowed_by_the_Wilderness: ContentSource.JE,
    Powercard.Swallow_the_Land_Dwellers: ContentSource.BASE,
    Powercard.Swarming_Wasps: ContentSource.BC,
    Powercard.Sweep_into_the_Sea: ContentSource.BC,
    Powercard.Sweltering_Exhaustion: ContentSource.HORIZONS,
    Powercard.Talons_of_Lightning: ContentSource.BASE,
    Powercard.Teeming_Rivers: ContentSource.BC,
    Powercard.Teeth_Gleam_from_Darkness: ContentSource.BC,
    Powercard.Tempest_of_Leaves_and_Branches: ContentSource.HORIZONS,
    Powercard.Terrifying_Chase: ContentSource.BC,
    Powercard.Terrifying_Nightmares: ContentSource.BASE,
    Powercard.Terrifying_Rampage: ContentSource.NI,
    Powercard.Territorial_Strife: ContentSource.JE,
    Powercard.Terror_Turns_to_Madness: ContentSource.JE,
    Powercard.The_Fog_Closes_In: ContentSource.JE,
    Powercard.The_Jungle_Hungers: ContentSource.BASE,
    Powercard.The_Land_Thrashes_in_Furious_Pain: ContentSource.BASE,
    Powercard.The_Past_Returns_Again: ContentSource.JE,
    Powercard.The_Trees_and_Stones_Speak_of_War: ContentSource.BASE,
    Powercard.The_Shore_Seethes_With_Hatred: ContentSource.JE,
    Powercard.The_Wounded_Wild_Turns_on_its_Assailants: ContentSource.JE,
    Powercard.Thickets_Erupt_with_Every_Touch_of_Breeze: ContentSource.JE,
    Powercard.Tigers_Hunting: ContentSource.BC,
    Powercard.Threatening_Flames: ContentSource.PP1,
    Powercard.Thriving_Chokefungus: ContentSource.JE,
    Powercard.Tidal_Boon: ContentSource.BASE,
    Powercard.Too_Near_the_Jungle: ContentSource.BC,
    Powercard.Tormenting_Rotflies: ContentSource.BC,
    Powercard.Towering_Wrath: ContentSource.BC,
    Powercard.Transformative_Sacrifice: ContentSource.NI,
    Powercard.Transform_to_a_Murderous_Darkness: ContentSource.JE,
    Powercard.Travelers_Boon: ContentSource.PP2,
    Powercard.Treacherous_Waterways: ContentSource.JE,
    Powercard.Trees_Radiate_Celestial_Brilliance: ContentSource.JE,
    Powercard.Tsunami: ContentSource.BASE,
    Powercard.Turmoils_Touch: ContentSource.NI,
    Powercard.Twilight_Fog_Brings_Madness: ContentSource.BC,
    Powercard.Twist_Perceptions: ContentSource.NI,
    Powercard.Twisted_Flowers_Murmur_Ultimatums: ContentSource.BC,
    Powercard.Unbearable_Deluge: ContentSource.PP2,
    Powercard.Uncanny_Melting: ContentSource.BASE,
    Powercard.Unearth_a_Beast_of_Wrathful_Stone: ContentSource.NI,
    Powercard.Unexpected_Tigers: ContentSource.JE,
    Powercard.Unleash_a_Torrent_of_the_Selfs_Own_Essence: ContentSource.JE,
    Powercard.Unlock_the_Gates_of_Deepest_Power: ContentSource.BC,
    Powercard.Unnerving_Pall: ContentSource.JE,
    Powercard.Unquenchable_Flames: ContentSource.JE,
    Powercard.Unrelenting_Growth: ContentSource.BC,
    Powercard.Vanish_Softly_Away_Forgotten_by_All: ContentSource.JE,
    Powercard.Utter_a_Curse_of_Dread_and_Bone: ContentSource.JE,
    Powercard.Voice_of_Command: ContentSource.JE,
    Powercard.Volcanic_Eruption: ContentSource.BC,
    Powercard.Veil_the_Nights_Hunt: ContentSource.BASE,
    Powercard.Vengeance_of_the_Dead: ContentSource.BASE,
    Powercard.Vigor_of_the_Breaking_Dawn: ContentSource.BASE,
    Powercard.Visions_of_Fiery_Doom: ContentSource.BASE,
    Powercard.Voice_of_Thunder: ContentSource.BASE,
    Powercard.Voracious_Growth: ContentSource.BASE,
    Powercard.Walls_of_Rock_and_Thorn: ContentSource.JE,
    Powercard.Wash_Away: ContentSource.BASE,
    Powercard.Ways_of_Shore_and_Heartland: ContentSource.PP2,
    Powercard.Weave_Together_the_Fabric_of_Place: ContentSource.JE,
    Powercard.Weep_for_What_Is_Lost: ContentSource.JE,
    Powercard.Whispered_Guidance_Through_the_Night: ContentSource.HORIZONS,
    Powercard.Winds_of_Rust_and_Atrophy: ContentSource.BASE,
    Powercard.Words_of_Warning: ContentSource.BASE,
    Powercard.Wrap_in_Wings_of_Sunlight: ContentSource.BASE,
    Powercard.Belligerent_and_Aggressive_Crops: ContentSource.NI,
    Powercard.Emerge_from_the_Dread_Night_Wind: ContentSource.NI,
    Powercard.Reach_from_the_Infinite_Darkness: ContentSource.NI,
    Powercard.Swallowed_by_the_Endless_Dark: ContentSource.NI,
    Powercard.Terror_of_the_Hunted: ContentSource.NI,
    Powercard.Call_to_Vigilance: ContentSource.NI,
    Powercard.Coordinated_Raid: ContentSource.NI,
    Powercard.Favors_of_Story_and_Season: ContentSource.NI,
    Powercard.Surrounded_by_the_Dahan: ContentSource.NI,
    Powercard.Smite_the_Land_with_Fulmination: ContentSource.NI,
    Powercard.Blinding_Glare: ContentSource.NI,
    Powercard.Focus_the_Suns_Rays: ContentSource.NI,
    Powercard.Unbearable_Gaze: ContentSource.NI,
    Powercard.Wither_Bodies_Scar_Stones: ContentSource.NI,
    Powercard.Blood_Water_and_Bloodlust: ContentSource.NI,
    Powercard.Boon_of_Corrupted_Blood: ContentSource.NI,
    Powercard.Draw_to_the_Waters_Edge: ContentSource.NI,
    Powercard.Wrack_with_Pain_and_Grief: ContentSource.NI,
}
