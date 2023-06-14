import yaml


def sax_parser_of_save()->list:
    buffer = open('save.yaml', 'r')
    output_content = yaml.load(buffer, Loader=yaml.Loader)
    return output_content
