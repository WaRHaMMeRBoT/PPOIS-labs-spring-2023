# -*- coding: utf-8 -*-
from typing import NoReturn, List
# Author: Vodohleb04
# Form implementation generated from reading ui file 'addBookDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addDialog(object):

    def setupUi(self, ui_main_window, data_controller, addDialog):
        self._add_button_clicked_counter = 0

        addDialog.setObjectName("addDialog")
        addDialog.resize(753, 373)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/png-transparent-computer-icons-add-logo-desktop-wallpaper-add-thumbnail-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addDialog.setWindowIcon(icon)
        addDialog.setStyleSheet("background-color: rgb(255, 225, 230);")
        self.buttonBox = QtWidgets.QDialogButtonBox(addDialog)
        self.buttonBox.setGeometry(QtCore.QRect(560, 320, 171, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.bookNameLineEdit = QtWidgets.QLineEdit(addDialog)
        self.bookNameLineEdit.setGeometry(QtCore.QRect(20, 20, 711, 32))
        self.bookNameLineEdit.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.bookNameLineEdit.setObjectName("bookNameLineEdit")
        self.authorsComboBox = QtWidgets.QComboBox(addDialog)
        self.authorsComboBox.setGeometry(QtCore.QRect(20, 130, 711, 32))
        self.authorsComboBox.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.authorsComboBox.setEditable(False)
        self.authorsComboBox.setCurrentText("")
        self.authorsComboBox.setDuplicatesEnabled(False)
        self.authorsComboBox.setObjectName("authorsComboBox")
        self.authorLineEdit = QtWidgets.QLineEdit(addDialog)
        self.authorLineEdit.setGeometry(QtCore.QRect(20, 60, 711, 32))
        self.authorLineEdit.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.addButton = QtWidgets.QPushButton(addDialog)
        self.addButton.setGeometry(QtCore.QRect(610, 90, 41, 34))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.addButton.setText("")
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton_2")
        self.addButton.setEnabled(False)
        self.undoButton = QtWidgets.QPushButton(addDialog)
        self.undoButton.setGeometry(QtCore.QRect(690, 90, 41, 34))
        self.undoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.undoButton.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.undoButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/png-transparent-computer-icons-icon-design-undo-arrow-miscellaneous-angle-triangle-thumbnail-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon1)
        self.undoButton.setObjectName("undoButton_2")
        self.undoButton.setEnabled(False)
        self.publishedSpinBox = QtWidgets.QSpinBox(addDialog)
        self.publishedSpinBox.setGeometry(QtCore.QRect(400, 260, 331, 32))
        self.publishedSpinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.publishedSpinBox.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.publishedSpinBox.setWrapping(False)
        self.publishedSpinBox.setSpecialValueText("")
        self.publishedSpinBox.setAccelerated(True)
        self.publishedSpinBox.setMinimum(1)
        self.publishedSpinBox.setMaximum(1000000000)
        self.publishedSpinBox.setObjectName("publishedSpinBox")
        self.publishingHouseLineEdit = QtWidgets.QLineEdit(addDialog)
        self.publishingHouseLineEdit.setGeometry(QtCore.QRect(20, 200, 711, 32))
        self.publishingHouseLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.publishingHouseLineEdit.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.publishingHouseLineEdit.setObjectName("publishingHouseLineEdit")
        self.volumesSpinBox = QtWidgets.QSpinBox(addDialog)
        self.volumesSpinBox.setGeometry(QtCore.QRect(20, 260, 331, 32))
        self.volumesSpinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.volumesSpinBox.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.volumesSpinBox.setAccelerated(True)
        self.volumesSpinBox.setMinimum(1)
        self.volumesSpinBox.setMaximum(1000000000)
        self.volumesSpinBox.setObjectName("volumesSpinBox")

        self.retranslateUi(addDialog)
        self.buttonBox.accepted.connect(addDialog.accept)
        self.buttonBox.rejected.connect(addDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addDialog)

        self.connect_changed_text()
        self.authorsComboBox.currentIndexChanged.connect(lambda: self.undoButton.setEnabled(True))
        self.connect_add_button(data_controller)
        self.connect_undo_button()
        addDialog.accepted.connect(lambda: data_controller.add_book(ui_main_window, book_params={
            "name": self.bookNameLineEdit.text(),
            "authors": self._make_list_from_combo_box(),
            "publishing_house": self.publishingHouseLineEdit.text(),
            "volumes": self.volumesSpinBox.value(),
            "published_amount": self.publishedSpinBox.value()}))

    def retranslateUi(self, addDialog):
        _translate = QtCore.QCoreApplication.translate
        addDialog.setWindowTitle(_translate("addDialog", "Конструктор книги"))
        self.bookNameLineEdit.setPlaceholderText(_translate("addDialog", "Введите название книги..."))
        self.authorLineEdit.setPlaceholderText(_translate("addDialog", "Введите ФИО автора..."))
        self.publishingHouseLineEdit.setPlaceholderText(_translate("addDialog", "Введите название издательства..."))
        self.publishedSpinBox.setSpecialValueText(_translate("addDialog", "Введите тираж"))
        self.volumesSpinBox.setSpecialValueText(_translate("addDialog", "Введите количество томов"))

    @property
    def add_button_clicked_counter(self) -> int:
        return self._add_button_clicked_counter

    @add_button_clicked_counter.setter
    def add_button_clicked_counter(self, new_value) -> NoReturn:
        self._add_button_clicked_counter = new_value

    def author_input_text_changed(self) -> NoReturn:
        if self.authorLineEdit.text():
            self.addButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)

    def input_author_already_added(self, input_text) -> bool:
        for i in range(self._add_button_clicked_counter):
            if input_text == self.authorsComboBox.itemText(i):
                return True
        return False

    def author_add_button(self, data_controller) -> NoReturn:
        input_text = self.authorLineEdit.text()
        if "," in input_text:
            data_controller.dialog_input_error("Запрещено подавать на вход запятые")
        else:
            if self.input_author_already_added(input_text):
                self.authorLineEdit.clear()
                data_controller.dialog_input_error(f"Значение {input_text} уже добавлено")
                return
            self.add_button_clicked_counter += 1
            self.authorsComboBox.addItem("")
            self.authorsComboBox.setItemText(self.add_button_clicked_counter - 1, input_text)
            self.authorLineEdit.clear()

    def author_undo_button(self) -> NoReturn:
        index = self.authorsComboBox.currentIndex()
        self.authorsComboBox.removeItem(index)
        self.add_button_clicked_counter -= 1
        if self.add_button_clicked_counter == 0:
            self.undoButton.setEnabled(False)

    def _make_list_from_combo_box(self) -> List[str]:
        return [self.authorsComboBox.itemText(i) for i in range(self._add_button_clicked_counter)]

    def connect_changed_text(self) -> NoReturn:
        self.authorLineEdit.textChanged.connect(lambda: self.author_input_text_changed())

    def connect_add_button(self, data_controller) -> NoReturn:
        self.addButton.clicked.connect(lambda: self.author_add_button(data_controller))

    def connect_undo_button(self) -> NoReturn:
        self.undoButton.clicked.connect(lambda: self.author_undo_button())
