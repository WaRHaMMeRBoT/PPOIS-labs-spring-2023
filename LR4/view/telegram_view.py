import logging

from functools import reduce

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This program is not compatible with your current PTB version {TG_VER}"
    )
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


CHOOSING, REPLY = range(2)

reply_markup_keyboard_data = [["Turn", "GameBoard", "Exit"]]
reply_markup = ReplyKeyboardMarkup(reply_markup_keyboard_data, one_time_keyboard=True)


class TelegramView:

    def __init__(self, controller=None) -> None:
        self.controller = controller

        self.__turn = 0

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text(
            "Choose your action",
            reply_markup=reply_markup
        )

        return CHOOSING

    async def gameboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text(
            f"Turn #{self.__turn}\n{[[str(reduce(lambda acc, ch: acc + str(ch), entity.get_entity(), '')) for entity in entity_row] for entity_row in self.controller.base_controller.get_game_board()]}",
            reply_markup=reply_markup
        )

        return CHOOSING

    async def turn(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.controller.play()
        await update.message.reply_text(
            "Make a turn",
            reply_markup=reply_markup
        )
        self.__turn += 1

        return CHOOSING

    async def add_entity(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        data = update.message.text
        self.controller.add_entity(data)
        await update.message.reply_text(
            "Entity was added successfullly",
            reply_markup=reply_markup
        )

        return CHOOSING

    async def exit(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        user = update.message.from_user
        await update.message.reply_text(
            "Bye",
            reply_markup=ReplyKeyboardRemove(),
        )

        return ConversationHandler.END

    def run(self) -> None:
        application = Application.builder().token("6110358258:AAHz4R7vWSEgPwqpgyU0Uru41RyPKPkVXWM").build()

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                CHOOSING: [
                    MessageHandler(
                        filters.Regex("^GameBoard$"), self.gameboard
                    ),
                    MessageHandler(
                        filters.Regex("^Turn$"), self.turn
                    ),
                    MessageHandler(
                        filters.TEXT, self.add_entity
                    ),
                ],
            },
            fallbacks=[MessageHandler(filters.Regex("^Exit$"), self.exit)],
        )

        application.add_handler(conv_handler)

        application.run_polling()
