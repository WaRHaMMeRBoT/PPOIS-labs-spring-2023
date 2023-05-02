import main


def starting_CLI_ATM():
    import main_ATM


def starting_GUI_ATM():
    main.guiATM()


if __name__ == "__main__":
    command = input("Input command: ")
    if command.lower() == "startcliatm":
        starting_CLI_ATM()
    elif command.lower() == "startguiatm":
        starting_GUI_ATM()
