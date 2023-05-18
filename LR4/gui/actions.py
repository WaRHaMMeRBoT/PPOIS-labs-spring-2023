import pygame

from gui.screen import Screen, stop_func
from gui.button import Button
from gui.input_box import InputBox
from gui.scroll_area import ScrollBox
from gui.text_box import TextBox
from gui.info_box import InfoBox
from gui.card import CardImg
from gui import config, utils


def show_menu_call():
    atm_btn = Button(
        config.WIDTH // 4 - 100, config.HEIGHT // 2 - 100, 200, 200,
        text='ATM', border_radius=5,
        action=atm_open_func
    )
    bank_btn = Button(
        3 * config.WIDTH // 4 - 100, config.HEIGHT // 2 - 100, 200, 200,
        text='BANK', border_radius=5,
        action=bank_open_func
    )

    @Screen()
    def show_menu_screen(*args, **kwargs):
        utils.draw_background(config.screen)

        atm_btn.draw(config.screen)
        bank_btn.draw(config.screen)

    show_menu_screen()


def atm_open_func():
    if not config.ATM.inserted:
        atm_insert_card_call()
    else:
        atm_input_pin_call()


def atm_insert_card_call():
    insert_card_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='INSERT',
        border_radius=5,
        action=atm_choose_card_call
    )
    back_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK',
        border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE])
    def atm_insert_card_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Вас приветствует АльфаБанк, для начала вставьте карту')

        insert_card_btn.draw(config.screen)
        back_btn.draw(config.screen)

        if config.ATM.inserted:
            atm_input_pin_call()
            stop_func()

    atm_insert_card_screen()


def atm_input_pin_call():
    error_info_box = InfoBox('Wrong PIN', background_color=(255, 0, 0), border_radius=5)
    input_box = InputBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    verify_pin_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='VERIFY', border_radius=5,
        action=atm_verify_pin_func
    )
    extract_card_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='EXTRACT CARD', border_radius=5,
        action=config.ATM.extract_card
    )
    back_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE], [input_box.handle_event])
    def atm_input_pin_screen(*args, **kwargs):
        if not config.ATM.inserted:
            stop_func()

        utils.draw_background(config.screen, 'Вас приветствует АльфаБанк, введите PIN - код')

        input_box.update()
        verify_pin_btn.update(pin=input_box.text, error=error_info_box)
        error_info_box.update()

        if error_info_box.active:
            error_info_box.draw(config.screen)

        input_box.draw(config.screen)
        verify_pin_btn.draw(config.screen)
        extract_card_btn.draw(config.screen)
        back_btn.draw(config.screen)

        return kwargs

    atm_input_pin_screen()


def atm_verify_pin_func(pin: str, error: InfoBox):
    if config.ATM.input_pin(pin):
        atm_menu_call()
    else:
        error.trigger()


def atm_choose_card_call():
    positions = [((1 if i % 2 == 0 else 3) * (config.WIDTH - 200) // 4 - 125,
                  10 + i // 2 * 170) for i in range(len(config.CARDS))]

    cards = [CardImg(card, *pos) for card, pos in zip(config.CARDS, positions)]

    scroll_box = ScrollBox(
        100, 150,
        config.WIDTH - 200, min(config.HEIGHT - 200, 10 + (len(config.CARDS) // 2 + len(config.CARDS) % 2) * 170),
        config.WIDTH - 200, 10 + (len(config.CARDS) // 2 + len(config.CARDS) % 2) * 170,
        cards
    )

    @Screen([pygame.K_ESCAPE], [scroll_box.handle_event])
    def atm_choose_card_screen(*args, **kwargs):

        utils.draw_background(config.screen, 'Вас приветствует АльфаБанк, выберите карту')

        scroll_box.update()

        scroll_box.draw(config.screen)

        for card in cards:
            if card.chosen:
                config.ATM.insert_card(card.card.number)
                stop_func()

    atm_choose_card_screen()


def atm_menu_call():
    get_money_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='GET MONEY', border_radius=5,
        action=atm_get_money_call
    )
    put_money_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='PUT MONEY', border_radius=5,
        action=atm_put_money_call
    )
    balance_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BALANCE', border_radius=5,
        action=atm_balance_call
    )
    extract_card_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='EXTRACT CARD', border_radius=5,
        action=config.ATM.extract_card
    )

    @Screen()
    def atm_menu_screen(*args, **kwargs):
        if not config.ATM.inserted:
            stop_func()

        utils.draw_background(config.screen, 'Вас приветствует АльфаБанк')

        balance_btn.draw(config.screen)
        put_money_btn.draw(config.screen)
        get_money_btn.draw(config.screen)
        extract_card_btn.draw(config.screen)

    atm_menu_screen()


def atm_balance_call():
    balance_box = TextBox(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text=str(config.ATM.card_balance()), border_radius=5,
    )
    back_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE])
    def atm_balance_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Вас приветствует АльфаБанк')

        balance_box.draw(config.screen)
        back_btn.draw(config.screen)

    atm_balance_screen()


def atm_put_money_call():
    error_info_box = InfoBox('Wrong SUMM', background_color=(255, 0, 0), border_radius=5)
    input_box = InputBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.69 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    confirm_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='CONFIRM', border_radius=5,
        action=atm_put_money_func
    )
    back_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE], [input_box.handle_event])
    def atm_put_money_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Введите сумму для пополнения')

        input_box.update()
        confirm_btn.update(money=input_box.text, error=error_info_box)
        error_info_box.update()

        if error_info_box.active:
            error_info_box.draw(config.screen)

        input_box.draw(config.screen)
        confirm_btn.draw(config.screen)
        back_btn.draw(config.screen)

    atm_put_money_screen()


def atm_put_money_func(money: str, error: InfoBox):
    if config.ATM.put_money(money):
        stop_func()
    else:
        error.trigger()


def atm_get_money_call():
    error_info_box = InfoBox('Wrong SUMM', background_color=(255, 0, 0), border_radius=5)
    input_box = InputBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.69 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    confirm_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='CONFIRM', border_radius=5,
        action=atm_get_money_func
    )
    back_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE], [input_box.handle_event])
    def atm_get_money_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Введите сумму для снятия')

        input_box.update()
        confirm_btn.update(money=input_box.text, error=error_info_box)
        error_info_box.update()

        if error_info_box.active:
            error_info_box.draw(config.screen)

        input_box.draw(config.screen)
        confirm_btn.draw(config.screen)
        back_btn.draw(config.screen)

    atm_get_money_screen()


def atm_get_money_func(money: str, error: InfoBox):
    if config.ATM.get_money(money):
        stop_func()
    else:
        error.trigger()


def bank_open_func():
    if not config.BANK.logged:
        bank_login_register_call()
    else:
        bank_homepage_call()


def bank_login_register_call():
    register_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.36 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='REGISTER', border_radius=5,
        action=bank_register_call
    )
    login_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.5 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='LOGIN', border_radius=5,
        action=bank_login_call
    )
    back_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.64 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE])
    def bank_login_register_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Войдите или зарегистрируйтесь')

        register_btn.draw(config.screen)
        login_btn.draw(config.screen)
        back_btn.draw(config.screen)

        if config.BANK.logged:
            bank_homepage_call()
            stop_func()

    bank_login_register_screen()


def bank_register_call():
    error_info_box = InfoBox('This login is already used', background_color=(255, 0, 0), border_radius=5)
    login_lable = TextBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.36 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        'LOGIN:', border=0, font_size=27, background_color=None
    )
    login_input_box = InputBox(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.36 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    password_lable = TextBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.5 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        'PASSWORD:', border=0, font_size=27, background_color=None
    )
    password_input_box = InputBox(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.5 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    confirm_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.64 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='CONFIRM', border_radius=5,
        action=bank_register_func
    )
    back_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.64 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE], [login_input_box.handle_event, password_input_box.handle_event])
    def bank_register_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Регистрация')

        login_input_box.update()
        password_input_box.update()
        confirm_btn.update(login=login_input_box.text, password=password_input_box.text, error=error_info_box)
        error_info_box.update()

        if error_info_box.active:
            error_info_box.draw(config.screen)

        login_lable.draw(config.screen)
        password_lable.draw(config.screen)
        login_input_box.draw(config.screen)
        password_input_box.draw(config.screen)
        confirm_btn.draw(config.screen)
        back_btn.draw(config.screen)

    bank_register_screen()


def bank_register_func(login: str, password: str, error: InfoBox):
    if config.BANK.register_acc(login, password):
        stop_func()
    else:
        error.trigger()


def bank_login_call():
    error_info_box = InfoBox('Wrong login or password', background_color=(255, 0, 0), border_radius=5)
    login_lable = TextBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.36 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        'LOGIN:', border=0, font_size=27, background_color=None
    )
    login_input_box = InputBox(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.36 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    password_lable = TextBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.5 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        'PASSWORD:', border=0, font_size=27, background_color=None
    )
    password_input_box = InputBox(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.5 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    verify_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.64 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='VERIFY', border_radius=5,
        action=bank_login_func
    )
    back_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.64 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE], [login_input_box.handle_event, password_input_box.handle_event])
    def bank_login_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Вход в аккаунт')

        login_input_box.update()
        password_input_box.update()
        verify_btn.update(login=login_input_box.text, password=password_input_box.text, error=error_info_box)
        error_info_box.update()

        if error_info_box.active:
            error_info_box.draw(config.screen)

        login_lable.draw(config.screen)
        login_input_box.draw(config.screen)
        password_lable.draw(config.screen)
        password_input_box.draw(config.screen)
        verify_btn.draw(config.screen)
        back_btn.draw(config.screen)

    bank_login_screen()


def bank_login_func(login: str, password: str, error: InfoBox):
    if config.BANK.login(login, password):
        stop_func()
    else:
        error.trigger()


def bank_homepage_call():
    register_card_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.36 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='REGISTER CARD', border_radius=5,
        action=bank_register_card_call
    )
    logout_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.5 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='LOGOUT', border_radius=5,
        action=config.BANK.logout
    )
    back_btn = Button(
        int(0.335 * (config.WIDTH - 100)) + 50, int(0.64 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE])
    def bank_homepage_screen(*args, **kwargs):
        if not config.BANK.logged:
            stop_func()

        utils.draw_background(config.screen, f'Добро пожаловать, {config.BANK.account.login}')

        register_card_btn.draw(config.screen)
        logout_btn.draw(config.screen)
        back_btn.draw(config.screen)

    bank_homepage_screen()


def bank_register_card_call():
    error_info_box = InfoBox('Wrong PIN', background_color=(255, 0, 0), border_radius=5)
    pin_lable = TextBox(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        'ПРИДУМАЙТЕ PIN-код:', border=0, font_size=25, background_color=None
    )
    input_box = InputBox(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.38 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        border_radius=5
    )
    confirm_btn = Button(
        int(0.16 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='CONFIRM', border_radius=5,
        action=bank_register_card_func
    )
    back_btn = Button(
        int(0.52 * (config.WIDTH - 100)) + 50, int(0.52 * (config.HEIGHT - 100)) + 50,
        int(0.33 * (config.WIDTH - 100)), int(0.1 * (config.HEIGHT - 100)),
        text='BACK', border_radius=5,
        action=stop_func
    )

    @Screen([pygame.K_ESCAPE], [input_box.handle_event])
    def bank_register_card_screen(*args, **kwargs):
        utils.draw_background(config.screen, 'Регистрация карты')

        input_box.update()
        confirm_btn.update(pin=input_box.text, error=error_info_box)
        error_info_box.update()

        if error_info_box.active:
            error_info_box.draw(config.screen)

        pin_lable.draw(config.screen)
        input_box.draw(config.screen)
        confirm_btn.draw(config.screen)
        back_btn.draw(config.screen)

    bank_register_card_screen()


def bank_register_card_func(pin: str, error: InfoBox):
    if config.BANK.register_card(pin):
        stop_func()
    else:
        error.trigger()

# Пофиксить скрол
