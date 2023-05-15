from cli2gui import Cli2Gui

from src.pyslang import main, parse_args

generate_gui = Cli2Gui(
    run_function=main,
    auto_enable=True,
    gui="pysimplegui",
)


gui = generate_gui(parse_args)
if __name__ == "__main__":
    gui()
