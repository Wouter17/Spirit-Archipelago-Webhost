from enum import Enum, IntEnum


class ContentSource(Enum):
    BASE = "Base game"
    FF = "Feather and Flame"
    BC = "Branch and Claw"
    JE = "Jagged Earth"
    NI = "Nature Incarnate"
    HORIZONS = "Horizons"


class Spirit(Enum):
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
    Eyes = "Eyes Watch from the Trees"
    Otter = "Fathomless Mud of the Swamp"
    Heat = "Rising Heat of Stone and Sand"
    Whirlwind = "Sun-Bright Whirlwind"
    Behemoth = "Ember-Eyed Behemoth"
    HearthVigil = "Hearth-Vigil"
    Roots = "Towering Roots of the Jungle"
    BODDYS = "Breath of Darkness Down Your Spine"
    Gaze = "Relentless Gaze of the Sun"
    Voice = "Wandering Voice Keens Delirium"
    WWB = "	Wounded Waters Bleeding"
    Earthquakes = "Dances Up Earthquakes"


class Aspect(Enum):
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
    BrandenburgPrussia = "Brandenburg-Prussia"
    England = "England"
    Sweden = "Sweden"
    France = "France (Plantation Colony)"
    HabsburgMonarchy = "Habsburg Monarchy (Livestock Colony)"
    Russia = "Russia"
    Scotland = "Scotland"
    HabsburgMining = "Habsburg Mining Expedition"

class Unique(Enum):
    TODO = "TODO"

class MinorPower(Enum):
    TODO = "TODO"

class MajorPower(Enum):
    TODO = "TODO"