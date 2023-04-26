from services.tg_controller import TelegramController
from view.telegram_view import TelegramView


def main():
    conroller = TelegramController()
    conroller.view.run()


if __name__ == "__main__":
    main()
