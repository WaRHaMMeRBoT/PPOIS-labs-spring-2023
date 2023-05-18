import atexit

from src.data import read_data, write_data

import gui.config as config
import gui.actions as actions


def exit_handler():
    if config.ATM.inserted:
        config.ATM.extract_card()
    if config.BANK.logged:
        config.BANK.logout()
    write_data(config.ACCOUNTS, config.CARDS, config.REPOSITORY,
               config.ATM, config.BANK)


def start():
    atexit.register(exit_handler)

    config.ACCOUNTS, config.CARDS, config.REPOSITORY, config.ATM, config.BANK = read_data()

    actions.show_menu_call()

