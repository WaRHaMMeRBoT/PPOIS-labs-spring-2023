# -*- coding: utf-8 -*-
from typing import NoReturn, List

# Author: Vodohleb04
# Form implementation generated from reading ui file 'strListParameterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from library import SearchRemoveBy
from mode import Mode


class Ui_strListParameterDialog(object):

    @property
    def add_button_clicked_counter(self) -> int:
        return self._add_button_clicked_counter

    @add_button_clicked_counter.setter
    def add_button_clicked_counter(self, new_value) -> NoReturn:
        self._add_button_clicked_counter = new_value

    def _list_str_input_text_changed(self) -> NoReturn:
        if self.lineEdit.text():
            self.addButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)

    def input_text_already_added(self, input_text) -> bool:
        for i in range(self._add_button_clicked_counter):
            if input_text == self.strListInputComboBox.itemText(i):
                return True
        return False

    def _list_str_input_add_button(self, data_controller) -> NoReturn:
        input_text = self.lineEdit.text()
        if "," in input_text:
            data_controller.dialog_input_error("Запрещено подавать на вход запятые")
        else:
            if self.input_text_already_added(input_text):
                self.lineEdit.clear()
                data_controller.dialog_input_error(f"Значение {input_text} уже добавлено")
                return
            self.add_button_clicked_counter += 1
            self.strListInputComboBox.addItem("")
            self.strListInputComboBox.setItemText(
                self.add_button_clicked_counter - 1, input_text)
            self.lineEdit.clear()

    def _list_str_input_undo_button(self) -> NoReturn:
        index = self.strListInputComboBox.currentIndex()
        self.strListInputComboBox.removeItem(index)
        self.add_button_clicked_counter -= 1
        if self.add_button_clicked_counter == 0:
            self.undoButton.setEnabled(False)

    def _make_list_from_combo_box(self) -> List[str]:
        return [self.strListInputComboBox.itemText(i) for i in range(self._add_button_clicked_counter)]

    def setupUi(self, ui_dialog, strListParameterDialog, data_controller, icon_file, parameter_name: str, mode: Mode,
                buffer=None):
        self._multyparam = True if isinstance(buffer, dict) else False
        self._complete_match_search: bool = False
        self._add_button_clicked_counter = 0
        self._mode = mode
        strListParameterDialog.setObjectName("strListParameterDialog")
        strListParameterDialog.resize(423, 172)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_file), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        strListParameterDialog.setWindowIcon(icon)
        strListParameterDialog.setStyleSheet("background-color: rgb(255, 225, 230);")
        self.strListInputComboBox = QtWidgets.QComboBox(strListParameterDialog)
        self.strListInputComboBox.setGeometry(QtCore.QRect(10, 80, 401, 32))
        self.strListInputComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.strListInputComboBox.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.strListInputComboBox.setObjectName("strListInputComboBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(strListParameterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 130, 181, 32))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(strListParameterDialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 401, 32))
        self.lineEdit.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.addButton = QtWidgets.QPushButton(strListParameterDialog)
        self.addButton.setGeometry(QtCore.QRect(290, 40, 41, 34))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.addButton.setText("")
        self.addButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/png-transparent-computer-icons-add-logo-desktop-wallpaper-add-thumbnail-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setObjectName("addButton")
        self.undoButton = QtWidgets.QPushButton(strListParameterDialog)
        self.undoButton.setGeometry(QtCore.QRect(370, 40, 41, 34))
        self.undoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.undoButton.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.undoButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/png-transparent-computer-icons-icon-design-undo-arrow-miscellaneous-angle-triangle-thumbnail-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon2)
        self.undoButton.setObjectName("undoButton")
        self.undoButton.setEnabled(False)
        self.retranslateUi(strListParameterDialog, parameter_name)
        self.buttonBox.accepted.connect(strListParameterDialog.accept)
        self.buttonBox.rejected.connect(strListParameterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(strListParameterDialog)
        self.connect_changed_text()
        self.strListInputComboBox.currentIndexChanged.connect(lambda: self.undoButton.setEnabled(True))
        self.connect_add_button(data_controller)
        self.connect_undo_button()
        if self._multyparam:
            self.connect_multyparam_accept_button(ui_dialog, strListParameterDialog, data_controller, buffer)
        else:
            self.connect_accept_button(ui_dialog, strListParameterDialog, data_controller)

    def retranslateUi(self, strListParameterDialog, parameter_name: str):
        _translate = QtCore.QCoreApplication.translate
        strListParameterDialog.setWindowTitle(_translate("strListParameterDialog", f"Ввод параметра \""
                                                                                   f"{parameter_name}\""))
        self.lineEdit.setPlaceholderText(_translate("strListParameterDialog", "Введите ФИО автора..."))
        self.strListInputComboBox.setPlaceholderText(
            _translate("strListParameterDialog", "Здесь будут добавлены введённые вами данные"))

    def connect_changed_text(self) -> NoReturn:
        self.lineEdit.textChanged.connect(lambda: self._list_str_input_text_changed())

    def connect_add_button(self, data_controller) -> NoReturn:
        self.addButton.clicked.connect(lambda: self._list_str_input_add_button(data_controller))

    def connect_undo_button(self) -> NoReturn:
        self.undoButton.clicked.connect(lambda: self._list_str_input_undo_button())

    def connect_accept_button(self, ui_dialog, listStrParameterDialog, data_controller) -> NoReturn:
        if self._mode == Mode.SEARCH_MODE:
            listStrParameterDialog.accepted.connect(lambda: self._connect_accept_search(ui_dialog, data_controller))
        elif self._mode == Mode.REMOVE_MODE:
            listStrParameterDialog.accepted.connect(
                lambda: self._remove_agreement(ui_dialog, listStrParameterDialog, data_controller))

    def _remove_agreement(self, ui_dialog, listStrParameterDialog, data_controller) -> NoReturn:
        result = QtWidgets.QMessageBox.question(
            listStrParameterDialog,
            "Подтвердите удаление",
            "Вы действительно хотите удалить данные из таблицы?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            data_controller.list_str_param_complete_remove(
                ui_dialog,
                param_to_remove=self._make_list_from_combo_box())


    def connect_multyparam_accept_button(self, ui_dialog, listStrParameterDialog, data_controller, buffer) -> NoReturn:
        listStrParameterDialog.accepted.connect(lambda: self._multyparam_accept_button(ui_dialog,
                                                                                       listStrParameterDialog,
                                                                                       data_controller,
                                                                                       buffer))

    def _connect_accept_search(self, ui_search_dialog, data_controller) -> NoReturn:
        ui_search_dialog.dialogButtonBox.button(ui_search_dialog.dialogButtonBox.Ok).setEnabled(False)
        data_controller.list_str_param_complete_search(
            ui_search_dialog=ui_search_dialog,
            param_to_search=self._make_list_from_combo_box())

    def _multyparam_accept_button(self, ui_dialog, listStrParameterDialog, data_controller, buffer) -> NoReturn:
        if not self._make_list_from_combo_box():
            data_controller.dialog_input_error("Ничего не было подано на ввод")
            listStrParameterDialog.reject()
        else:
            buffer["authors"] = self._make_list_from_combo_box()
            buffer["required_amount"] -= 1
            if buffer["required_amount"] == 0:
                if self._mode == Mode.SEARCH_MODE:
                    self._multyparam_accepted_search(ui_dialog, data_controller, buffer)
                elif self._mode == Mode.REMOVE_MODE:
                    result = QtWidgets.QMessageBox.question(
                        listStrParameterDialog,
                        "Подтвердите удаление",
                        "Вы действительно хотите удалить данные из таблицы?",
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                        QtWidgets.QMessageBox.No)
                    if result == QtWidgets.QMessageBox.Yes:
                        self._multyparam_accepted_remove(ui_dialog, data_controller, buffer)

    @staticmethod
    def _multyparam_accepted_search(ui_search_dialog, data_controller, buffer) -> NoReturn:
        ui_search_dialog.found_books = data_controller.lib.search_for_books(SearchRemoveBy.PUBLISHING_HOUSE_AND_AUTHORS,
                                                                            publishing_house=buffer["publishing_house"],
                                                                            authors=buffer["authors"])
        data_controller.list_str_param_complete_search(ui_search_dialog,
                                                      buffer,
                                                      multyparam=True)
        ui_search_dialog.dialogButtonBox.button(ui_search_dialog.dialogButtonBox.Ok).setEnabled(False)

    @staticmethod
    def _multyparam_accepted_remove(ui_main_window, data_controller, buffer) -> NoReturn:
        data_controller.list_str_param_complete_remove(ui_main_window, buffer, multyparam=True)
