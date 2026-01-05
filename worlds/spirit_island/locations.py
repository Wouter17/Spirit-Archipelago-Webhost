from BaseClasses import Location

class SpiritIslandLocation(Location):
    game: str = "Spirit Island"


si_location_name_to_id = dict()
si_location_id_to_name = dict()
for level in Overcooked2Level():
    if level.level_id == 36:
        continue  # level 6-6 does not have an item location
    si_location_name_to_id[level.location_name_item] = level.level_id
    si_location_id_to_name[level.level_id] = level.location_name_item
