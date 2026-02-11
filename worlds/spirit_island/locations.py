from BaseClasses import Location

from .SpiritIslandLevels import Adversary, Aspect, Powercard, Spirit


class SpiritIslandLocation(Location):
    game: str = "Spirit Island"


def defeat_with_string(adversary: Adversary, difficulty: int, spirit: Spirit | Aspect, ed=False) -> str:
    return f"Defeat{'ed' if ed else ''} {adversary.value} with {spirit.full_name} on difficulty {difficulty}"


si_location_name_to_id: dict[str, int] = {}
si_location_id_to_name: dict[int, str] = {}

spirit_with_aspects = list(Spirit) + list(Aspect)

items = [defeat_with_string(adversary, difficulty, spirit) for difficulty in range(0, 7)
         for adversary in Adversary for spirit in spirit_with_aspects] \
    + [f"Play: {card.value}" for card in Powercard]

base_offset = 1
for i, item in enumerate(items):
    idx = i + base_offset
    si_location_name_to_id[item] = idx
    si_location_id_to_name[idx] = item
