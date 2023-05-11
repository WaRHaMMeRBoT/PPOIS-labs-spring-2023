def creating_level_map():
    with open("level_map", "r") as level_map:
        level_map_structure = level_map.readlines()
        level_map_structure = [x.strip("\n") for x in level_map_structure]
        return level_map_structure


tile_size = 64
screen_width = 1080
screen_height = len(creating_level_map()) * tile_size