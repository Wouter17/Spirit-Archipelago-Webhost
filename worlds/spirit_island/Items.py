from collections import defaultdict

from BaseClasses import Item

from .SpiritIslandLevels import Aspect, Element, Powercard, Spirit


class SpiritIslandItem(Item):
    game: str = "Spirit Island"


filler_items = [
    f"(filler) A friendly greeting from {spirit.name}" for spirit in Spirit]

si_base = 0x57696c6c

item_id_to_name: dict[int, str] = {}
item_name_to_id: dict[str, int] = {}

items = ["+1 Energy", "+1 Cardplay", "+1 Blight"] + [(card.value) for card in Powercard] \
    + [sa.full_name for sa in list(Spirit) + list(Aspect)] + [element.value for element in Element] + filler_items

for i, item in enumerate(items):
    idx = i + si_base
    item_id_to_name[idx] = item
    item_name_to_id[item] = idx

item_name_groups: defaultdict[str, set[str]] = defaultdict(set)
for card in Powercard:
    if card.spirit is not None:
        item_name_groups[f"{card.spirit.value} uniques"].add(card.value)
    else:
        item_name_groups[f"{card.expansion.value} cards"].add(card.value)
item_name_groups["spirits"] = {s.full_name for s in Spirit}
item_name_groups["aspects"] = {a.full_name for a in Aspect}
item_name_groups["filler"] = set(filler_items)
item_name_groups["elements"] = {e.value for e in Element}

item_descriptions = dict.fromkeys(filler_items, "an item that does nothing")
item_descriptions |= {element.value: f"Grants one {element.value} for a single turn" for element in Element}
item_descriptions["+1 Energy"] = "One extra energy per turn with each spirit"
item_descriptions["+1 Cardplay"] = "One extra cardplay per turn with each spirit"
item_descriptions["+1 Blight"] = "One extra blight when starting a new game"
