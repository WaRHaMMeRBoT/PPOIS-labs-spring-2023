# Author: Vodohleb04
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QTextEdit, QAction

from library import Library, SortBy
from book import Book
from controller import Controller
from gui_lab_2 import Ui_MainWindow, MyWindow

if __name__ == "__main__":
    import sys

    books = [
        Book(authors=["Власенко Денис", "Гаврик Владислав"], name="Как сдать экзамены?", publishing_house="BSUIR Times",
             published_amount=30, volumes=2),
        Book(authors=["Аркадий Натанович Стругацкий","Борис Натанович Стругацкий"], name="Пикник на обочине", publishing_house="АСТ",
             published_amount=100000, volumes=1),
        Book(authors=["Войткус Станислав", "Шутов Клоун Смехович"], name="Топовые панчи", publishing_house="КлоунПресс",
             published_amount=12345, volumes=1),
        Book(authors=["Толстой Лев Николаевич"], name="Война и мир", publishing_house="Художественная литература",
             published_amount=1000, volumes=4),
        Book(authors=["Толстой Лев Николаевич"], name="Война и мир",
             published_amount=1000, volumes=4),
        Book(authors=["Іван Мележ"], name="Людзі на балоце", publishing_house="Мастацкая літаратура",
             published_amount=2000, volumes=1),
        Book(authors=["Іван Мележ"], name="Людзі на балоце", publishing_house="Дом друку",
             published_amount=2000, volumes=1),
        Book(authors=["Іван Мележ"], name="Палесская хроніка", publishing_house="Мастацкая літаратура",
             published_amount=2000, volumes=1),
        Book(authors=["Жидкий Артемий Арсеньевич", "Немигина Анна Альтовна", "Пауков Иполит Сергеевич"],
             name="Тактика боевых действия ЧВК Редан в ТЦ", publishing_house="ТгКаналПаук",
             published_amount=625, volumes=5),
        Book(authors=["Виктор Корнеплод", "Артемий Ветродуй", "Анна Землеройка"],
             name="Морковка увеличится в 2 раза. Нужно только...", publishing_house="СадоводПечать",
             published_amount=813, volumes=10),
        Book(authors=["Stephen King"], name="Rita Hayworth and Shawshank Redemption", publishing_house="PrinterPrint",
             published_amount=14312, volumes=1),
        Book(authors=["Stephen King"], name="The Shining", publishing_house="PrintHouseOFAlbert",
             published_amount=8231, volumes=1),
        Book(authors=["Stephen King"], name="1408", publishing_house="Printer House Has Jack Build",
             published_amount=2432, volumes=1),
        Book(authors=["Stephen King"], name="Night Shift", publishing_house="ShifterChiefPr",
             published_amount=1243, volumes=1),
        Book(authors=["The Short-Timers"], name="Gustav Hasford", publishing_house="VietnamWarPrinter",
             published_amount=4500, volumes=1),
        Book(authors=["Кен Кизи"], name="Пролетая над гнездом кукушки", publishing_house="Замежная Літаратура",
             published_amount=5651, volumes=1),
        Book(authors=["Булгаков Михаил Афанасьевич"], name="Белая гвардия", publishing_house="Дом печати",
             published_amount=3653, volumes=1),
        Book(authors=["Достоевский Фёдор Михайлович"], name="Идиот", publishing_house="Дом печати",
             published_amount=3653, volumes=1),
        Book(authors=["Быкаў Васіль Уладзіміравіч"], name="Сотнікаў", publishing_house="Мастацкая літаратура",
             published_amount=2712, volumes=1),
        Book(authors=[], name="Народные сказки", publishing_house="Детство",
             published_amount=5134, volumes=2),
        Book(authors=[], name="Поговорки", publishing_house="Береста",
             published_amount=3114, volumes=2),
        Book(authors=["Бабиджон Дон Донович", "Али Абдаев"], name="Подготовка к ИГЭ па барьба", publishing_house="Ахмад",
             published_amount=534, volumes=5),
        Book(authors=["Алексиевич Светлана Александровна"], name="Цинковые мальчики", publishing_house="БелКнига",
             published_amount=1934, volumes=1),
        Book(authors=["Пшекич Павел", "Войткус Станислав"], name="Тайны польской разведки", publishing_house="Пшпшпшч",
             published_amount=714, volumes=4),
        Book(authors=["Аркадий Натанович Стругацкий","Борис Натанович Стругацкий"],
             name="Трудно быть богом", publishing_house="Печатный дом Джека",
             published_amount=5910, volumes=1),
        Book(authors=["Червинский", "Дукалис"], name="Всё о Ницше и другие непридуманные истории,\n"
                                                     " о которых невозможно молчать", publishing_house="Коммунпечать",
             published_amount=712, volumes=3),
        Book(authors=["В. И. Варшавский", "Д. А. Поспелов"], name="Оркестр играет без дирижёра",
             publishing_house="Голая Правда", published_amount=93, volumes=1),
        Book(),
        Book(authors=["Слабов Славутий"], name="Оформление", publishing_house="Автору ноль лет", published_amount=9133),
        Book(authors=["Клинских Юрий", "Диоген", "Тайлер Жердин"], name="Колхозный панк",
             publishing_house="Андерграунд", volumes=2),
        Book(authors=["Зубенко Михаил Петрович", "Кама Пуля", "Пятигорска старший брат Омар"], name="Мафия изнутри"),
        Book(authors=["Славутий Древний"])
    ]
    lib = Library(books)

    data_controller = Controller(lib)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow(data_controller=data_controller)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
