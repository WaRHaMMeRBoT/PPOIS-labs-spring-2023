import yaml

def save_button(data_to_save: list):
    buffer = open("save.yaml", "w")
    yaml.dump([[something for something in element] for element in data_to_save], buffer)

