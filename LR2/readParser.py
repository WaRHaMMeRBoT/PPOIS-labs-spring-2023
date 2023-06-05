from FootbalHandlerSax import *


def read_parser(name_of_file):
    handler = FootballHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(name_of_file)
    return handler