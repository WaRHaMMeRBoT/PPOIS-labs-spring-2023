def parse():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--nextday", action="store_true")
    parser.add_argument("--desinfect", type=int)
    parser.add_argument("--heal", type=int)
    parser.add_argument("--hydrate", type=int)
    parser.add_argument("--weeding", type=int)
    parser.add_argument("--plant", type=str)
    parser.add_argument("--killplant", type=int)
    parser.add_argument("--init", action="store_true")
    parser.add_argument("--show", action="store_true")

    args = parser.parse_args()

    return args
