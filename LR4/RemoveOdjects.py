from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class RemoveWayStation(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None):
        super(RemoveWayStation, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Удаление пути")

        self.lable_station1_name = QLabel(self)
        self.lable_station1_name.setText('Название первой станции: ')
        self.lable_station1_name.resize(150, 40)

        self.station1_name_line = QLineEdit(self)
        self.station1_name_line.move(160, 0)

        self.lable_station2_name = QLabel(self)
        self.lable_station2_name.move(0, 40)
        self.lable_station2_name.setText('Название второй станции: ')
        self.lable_station2_name.resize(150, 40)

        self.station2_name_line = QLineEdit(self)
        self.station2_name_line.move(160, 40)

        self.button = QPushButton('Удалить путь', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit(
            [self.station1_name_line.text(), self.station2_name_line.text()])
        self.station1_name_line.clear()
        self.station2_name_line.clear()
        self.close()


class RemoveStation(QMainWindow):
    submitClicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(RemoveStation, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Удаление станции")

        self.lable_station_name = QLabel(self)
        self.lable_station_name.setText('Название станции: ')

        self.station_name_line = QLineEdit(self)
        self.station_name_line.move(110, 0)

        self.button = QPushButton('Удалить станцию', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit(self.station_name_line.text())
        self.station_name_line.clear()
        self.close()


class RemoveTrain(QMainWindow):
    submitClicked = pyqtSignal(int)

    def __init__(self, parent=None):
        super(RemoveTrain, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Удаление поезда")

        self.lable_train_index = QLabel(self)
        self.lable_train_index.setText('Номер поезда: ')

        self.train_index_line = QLineEdit(self)
        self.train_index_line.move(110, 0)

        self.button = QPushButton('Удалить поезд', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.submitClicked.emit(int(self.train_index_line.text()))
        self.train_index_line.clear()
        self.close()
