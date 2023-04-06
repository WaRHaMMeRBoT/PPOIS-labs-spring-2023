# Author: Vodohleb04
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from mode import Mode
from library import Library, SortBy, SearchRemoveBy
from book import Book
from typing import NoReturn, List, Dict, Any
import enum
import os
import re

from search_dialog_window import Ui_searchDialog
from remove_dialog_window import Ui_removeDialog
from one_str_input_dialog import Ui_oneStrParameterDialog
from str_list_parameter_dialog import Ui_strListParameterDialog
from int_number_parameter_dialog import Ui_intNumberParameterDialog
from add_book_dialog import Ui_addDialog


class ColumnsIndexes(enum.Enum):
    NAME = 0
    AUTHORS = 1
    PUBLISHING_HOUSE = 2
    VOLUMES = 3
    PUBLISHED = 4
    PUBLISHED_VOLUMES = 5


class SortCondition:
    def __init__(self, sort_by: SortBy = SortBy.NAME_SORT, reverse_order=False):
        self._sort_by = sort_by
        self._reverse_order = reverse_order

    @property
    def sort_by(self) -> SortBy:
        return self._sort_by

    @sort_by.setter
    def sort_by(self, new_sort_param: SortBy) -> NoReturn:
        self._sort_by = new_sort_param

    @property
    def reverse_order(self) -> bool:
        return self._reverse_order

    @reverse_order.setter
    def reverse_order(self, new_order: bool) -> NoReturn:
        self._reverse_order = new_order


class Controller:
    _books_on_page: int = 10

    def __init__(self, lib: Library):
        if not isinstance(lib, Library):
            raise TypeError(f"lib must be {type(Library)}. Got {type(lib)} instead")
        self._lib = lib
        self._current_page = 0
        self._sort_condition = SortCondition()
        self._search_type = None
        self._remove_type = None
        self._sort_books_in_lib()

    @property
    def sort_condition(self) -> SortCondition:
        return self._sort_condition

    @property
    def lib(self) -> Library:
        return self._lib

    @property
    def books_on_page(self) -> int:
        return self._books_on_page

    @property
    def page(self) -> int:
        return self._current_page

    def load_next_page(self, ui_main_window) -> NoReturn:
        self.update_table(ui_main_window)
        if self._current_page < (len(self._lib.books) / self._books_on_page) - 1:
            self._current_page += 1
            self.load_current_page(ui_main_window)

    def load_prev_page(self, ui_main_window) -> NoReturn:
        self.update_table(ui_main_window)
        if self._current_page > 0:
            self._current_page -= 1
            self.load_current_page(ui_main_window)

    def load_first_page(self, ui_main_window) -> NoReturn:
        self.update_table(ui_main_window)
        self._current_page = 0
        self.load_current_page(ui_main_window)

    def load_last_page(self, ui_main_window) -> NoReturn:
        self.update_table(ui_main_window)
        if len(self.lib.books) % self._books_on_page == 0:
            self._current_page = len(self.lib.books) // self._books_on_page - 1
        else:
            self._current_page = len(self.lib.books) // self._books_on_page
        self.load_current_page(ui_main_window)

    @staticmethod
    def _set_item_of_table(ui_main_window, row_number: int, column_name: ColumnsIndexes, table_item) -> NoReturn:
        ui_main_window.table.setItem(
            row_number,
            column_name.value,
            QtWidgets.QTableWidgetItem(table_item))

    @staticmethod
    def _fill_table_in_ui_with_books(ui_main_window, books: List[Book], start_index, end_index) -> NoReturn:
        labels = [str(index) for index in range(start_index + 1, end_index + 1) if index <= len(books)]
        ui_main_window.table.setVerticalHeaderLabels(labels)
        row = 0
        ui_main_window.table.setRowCount(len(books[start_index: end_index]))
        for book in books[start_index: end_index]:
            if row >= end_index - start_index:
                break
            Controller._set_item_of_table(ui_main_window, row, ColumnsIndexes.NAME, book.name)
            authors_str = ", ".join(book.authors)
            Controller._set_item_of_table(ui_main_window, row, ColumnsIndexes.AUTHORS, authors_str)
            Controller._set_item_of_table(ui_main_window, row, ColumnsIndexes.PUBLISHING_HOUSE, book.publishing_house)
            Controller._set_item_of_table(ui_main_window, row, ColumnsIndexes.VOLUMES, str(book.volumes))
            Controller._set_item_of_table(ui_main_window, row, ColumnsIndexes.PUBLISHED, str(book.published_amount))
            Controller._set_item_of_table(ui_main_window, row, ColumnsIndexes.PUBLISHED_VOLUMES,
                                          str(book.published_volumes_amount))
            row += 1

    def load_current_page(self, ui_main_window) -> NoReturn:
        self._fill_table_in_ui_with_books(
            ui_main_window,
            self._lib.books,
            start_index=self._current_page * self._books_on_page,
            end_index=(self._current_page + 1) * self._books_on_page)

    @staticmethod
    def _autosave_name() -> str:
        regex = re.compile(r"^autosave([1-9]\d*)\.json$")
        filename_indexes = [int(regex.match(file).group(1)) for file in os.listdir("./saves") if regex.match(file)]
        if not filename_indexes:
            filename_indexes.append(0)
        return f"./saves/autosave{max(filename_indexes) + 1}.json"

    def save_library_as(self, filename) -> NoReturn:
        if not filename:
            error_msg_box = QMessageBox()
            error_msg_box.setWindowTitle("Файл не был выбран")
            error_msg_box.setText("Вы отменили выбор файла либо что-то пошло не так.")
            error_msg_box.setIcon(QMessageBox.Information)
            error_msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            error_msg_box.setDefaultButton(QMessageBox.Ok)
            error_msg_box.adjustSize()
            error_msg_box.exec()
            return
        self._lib.save(filename)

    def save_library(self) -> NoReturn:
        if not self.lib.saved_flag:
            filename = self._lib.save_filename if self._lib.save_filename else Controller._autosave_name()
            self._lib.save(filename)

    def load_library(self, ui_main_window, filename) -> NoReturn:
        if not filename:
            error_msg_box = QMessageBox()
            error_msg_box.setWindowTitle("Файл не был выбран")
            error_msg_box.setText("Вы отменили выбор файла либо что-то пошло не так.")
            error_msg_box.setIcon(QMessageBox.Information)
            error_msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            error_msg_box.setDefaultButton(QMessageBox.Ok)
            error_msg_box.adjustSize()
            error_msg_box.exec()
            return
        self._lib = self._lib.load(filename)
        self._sort_books_in_lib()
        self._current_page = 0
        self.load_current_page(ui_main_window)

    @staticmethod
    def _change_sort_conditions_arguments_correct(**kwargs) -> NoReturn:
        if not len(kwargs) == 1:
            raise ValueError(f"expected 1 key argument, got {len(kwargs)} instead")
        for key in kwargs.keys():
            if key != "reverse_order" and key != "sort_by":
                raise ValueError(f"Unknown positional argument: {key}")
            if key == "sort_by":
                if not isinstance(kwargs[key], SortBy):
                    raise TypeError(f"Unknown type for sort_by arg. Expected {type(SortBy)},"
                                    f" got {type(kwargs[key])} instead")

    @staticmethod
    def _sort_params_can_be_changed(ui_main_window, **kwargs) -> bool:
        kwargs["sort_by"] = kwargs.get("sort_by", "No_Param")
        kwargs["reverse_order"] = kwargs.get("reverse_order", "No_Param")
        if not ui_main_window.sort_by_name_act.isChecked() and \
                not ui_main_window.sort_by_published_amount_act.isChecked() and \
                not ui_main_window.sort_by_publishing_house_act.isChecked() and kwargs["sort_by"] == SortBy.NAME_SORT:
            ui_main_window.sort_by_name_act.setChecked(True)
            return False
        elif not ui_main_window.sort_by_published_amount_act.isChecked() and \
                not ui_main_window.sort_by_name_act.isChecked() and \
                not ui_main_window.sort_by_publishing_house_act.isChecked() and \
                kwargs["sort_by"] == SortBy.PUBLISHED_AMOUNT_SORT:
            ui_main_window.sort_by_published_amount_act.setChecked(True)
            return False
        elif not ui_main_window.sort_by_publishing_house_act.isChecked() and \
                not ui_main_window.sort_by_published_amount_act.isChecked() and \
                not ui_main_window.sort_by_name_act.isChecked() and kwargs["sort_by"] == SortBy.PUBLISHING_HOUSE_SORT:
            ui_main_window.sort_by_publishing_house_act.setChecked(True)
            return False
        if not ui_main_window.direct_sort_act.isChecked() and not ui_main_window.reverse_sort_act.isChecked() and \
                kwargs["reverse_order"] == False:
            ui_main_window.direct_sort_act.setChecked(True)
            return False
        elif not ui_main_window.reverse_sort_act.isChecked() and not ui_main_window.direct_sort_act.isChecked() and \
                kwargs["reverse_order"] == True:
            ui_main_window.reverse_sort_act.setChecked(True)
            return False
        return True

    def _sort_books_in_lib(self) -> NoReturn:
        self._lib.sort_by(self.sort_condition.sort_by, self.sort_condition.reverse_order)

    def _change_sort_params(self, ui_main_window, **kwargs) -> NoReturn:
        for key in kwargs.keys():
            if key == "reverse_order":
                if kwargs[key]:
                    ui_main_window.direct_sort_act.setChecked(False)
                    self._sort_condition.reverse_order = True
                else:
                    ui_main_window.reverse_sort_act.setChecked(False)
                    self._sort_condition.reverse_order = False
            else:
                if kwargs[key] == SortBy.NAME_SORT:
                    self.sort_condition.sort_by = SortBy.NAME_SORT
                    ui_main_window.sort_by_published_amount_act.setChecked(False)
                    ui_main_window.sort_by_publishing_house_act.setChecked(False)
                elif kwargs[key] == SortBy.PUBLISHING_HOUSE_SORT:
                    ui_main_window.sort_by_published_amount_act.setChecked(False)
                    ui_main_window.sort_by_name_act.setChecked(False)
                    self.sort_condition.sort_by = SortBy.PUBLISHING_HOUSE_SORT
                elif kwargs[key] == SortBy.PUBLISHED_AMOUNT_SORT:
                    ui_main_window.sort_by_name_act.setChecked(False)
                    ui_main_window.sort_by_publishing_house_act.setChecked(False)
                    self.sort_condition.sort_by = SortBy.PUBLISHED_AMOUNT_SORT

    def sort_lib(self, ui_main_window, **kwargs) -> NoReturn:
        self._change_sort_conditions_arguments_correct(**kwargs)
        if not self._sort_params_can_be_changed(ui_main_window, **kwargs):
            return
        self._change_sort_params(ui_main_window, **kwargs)
        self._sort_books_in_lib()
        self.load_current_page(ui_main_window)

    @staticmethod
    def _table_input_error(error_code: int, wracked_data: str, element_number: int) -> QMessageBox:
        detailed_text = f"При изменении данных книги под номером {element_number + 1} произошла ошибка: были введены " \
                        f"некорретные данные в столбце \"" \
                        f"{'Тираж' if error_code == ColumnsIndexes.PUBLISHED.value else 'Количество томов'}\". " \
                        f"Ожидалось натуральное число или 0, но было введено \"{wracked_data}\"." \
                        f" Данные из этой строки не были изменены."
        error_msg_box = QMessageBox()
        error_msg_box.setWindowTitle("Ошибка")
        error_msg_box.setText("Вы ввели некорректные данные!")
        error_msg_box.setIcon(QMessageBox.Warning)
        error_msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        error_msg_box.setDefaultButton(QMessageBox.Ok)
        error_msg_box.setDetailedText(detailed_text)
        error_msg_box.adjustSize()
        return error_msg_box

    def read_data_in_ui_main_table(self, ui_main_window) -> NoReturn:
        for i in range(len(self._lib.books[self._current_page * self._books_on_page:
                       (self._current_page + 1) * self._books_on_page])):
            if not re.match(r"^0$|^[1-9]\d*$", ui_main_window.table.item(i, ColumnsIndexes.VOLUMES.value).text()):
                self._table_input_error(ColumnsIndexes.VOLUMES.value,
                                        wracked_data=ui_main_window.table.item(i, ColumnsIndexes.VOLUMES.value).text(),
                                        element_number=i).exec()
                continue
            if not re.match(r"^0$|^[1-9]\d*$", ui_main_window.table.item(i, ColumnsIndexes.PUBLISHED.value).text()):
                self._table_input_error(ColumnsIndexes.PUBLISHED.value,
                                        wracked_data=ui_main_window.table.item(i,
                                                                               ColumnsIndexes.PUBLISHED.value).text(),
                                        element_number=i).exec()
                continue
            book_in_table = Book(
                name=ui_main_window.table.item(i, ColumnsIndexes.NAME.value).text(),
                authors=ui_main_window.table.item(i, ColumnsIndexes.AUTHORS.value).text().split(", "),
                publishing_house=ui_main_window.table.item(i, ColumnsIndexes.PUBLISHING_HOUSE.value).text(),
                volumes=int(ui_main_window.table.item(i, ColumnsIndexes.VOLUMES.value).text()),
                published_amount=int(ui_main_window.table.item(i, ColumnsIndexes.PUBLISHED.value).text()))
            if self._lib.books[self._current_page * self._books_on_page + i] != book_in_table:
                self._lib.books[self._current_page * self._books_on_page + i] = book_in_table
                self._lib.saved_flag = False
        self._sort_books_in_lib()

    def read_data_in_ui_search_table(self, ui_search_window, ui_main_window) -> NoReturn:
        for i in range(len(ui_search_window.found_books)):
            if not re.match(r"^0$|^[1-9]\d*$", ui_search_window.table.item(i, ColumnsIndexes.VOLUMES.value).text()):
                self._table_input_error(
                    ColumnsIndexes.VOLUMES.value,
                    wracked_data=ui_search_window.table.item(i, ColumnsIndexes.VOLUMES.value).text(),
                    element_number=i).exec()
                continue
            if not re.match(r"^0$|^[1-9]\d*$", ui_search_window.table.item(i, ColumnsIndexes.PUBLISHED.value).text()):
                self._table_input_error(
                    ColumnsIndexes.PUBLISHED.value,
                    wracked_data=ui_search_window.table.item(i, ColumnsIndexes.PUBLISHED.value).text(),
                    element_number=i).exec()
                continue
            book_in_table = Book(
                name=ui_search_window.table.item(i, ColumnsIndexes.NAME.value).text(),
                authors=ui_search_window.table.item(i, ColumnsIndexes.AUTHORS.value).text().split(", "),
                publishing_house=ui_search_window.table.item(i, ColumnsIndexes.PUBLISHING_HOUSE.value).text(),
                volumes=int(ui_search_window.table.item(i, ColumnsIndexes.VOLUMES.value).text()),
                published_amount=int(ui_search_window.table.item(i, ColumnsIndexes.PUBLISHED.value).text()))
            if book_in_table != ui_search_window.found_books[i]:
                for j in range(len(self._lib.books)):
                    if self._lib.books[j] is ui_search_window.found_books[i]:
                        self._lib.books[j] = book_in_table
                        self._lib.saved_flag = False
        self._sort_books_in_lib()
        self.load_current_page(ui_main_window)

    def update_table(self, ui_main_window) -> NoReturn:
        self.read_data_in_ui_main_table(ui_main_window)
        self.load_current_page(ui_main_window)

    def find_books_dialog(self, ui_main_window, MainWindow) -> NoReturn:
        searchDialog = QtWidgets.QDialog(parent=MainWindow)
        ui = Ui_searchDialog()
        ui.setupUi(ui_main_window, searchDialog, data_controller=self)
        searchDialog.show()

    def remove_books_dialog(self, ui_main_window, mainWindow) -> NoReturn:
        removeDialog = QtWidgets.QDialog(parent=mainWindow)
        ui = Ui_removeDialog()
        ui.setupUi(ui_main_window, mainWindow, removeDialog, self)
        removeDialog.show()

    @staticmethod
    def _search_remove_error(msg: str, warning: bool) -> QMessageBox:
        title = "Предупреждение" if warning else "Ошибка"
        error_msg_box = QMessageBox()
        error_msg_box.setWindowTitle(title)
        error_msg_box.setText(msg)
        error_msg_box.setIcon(QMessageBox.Warning)
        error_msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        error_msg_box.setDefaultButton(QMessageBox.Ok)
        error_msg_box.adjustSize()
        return error_msg_box

    @staticmethod
    def _make_remove_params_str(kwargs: Dict[str, Any]) -> str:
        res_str = ""
        for key, value in kwargs.items():
            if key == "authors":
                res_str += f"\"авторы\": {', '.join(value)}\n"
            elif key == "publishing_house":
                res_str += f"\"издательство\": {value}\n"
            elif key == "min_volumes_amount":
                res_str += f"\"минимальное количество глав\": {value}\n"
            elif key == "max_volumes_amount":
                res_str += f"\"максимальное количество глав\": {value}\n"
            elif key == "removing_book_name":
                res_str += f"\"название книги\": {value}\n"
            elif key == "min_published_amount":
                res_str += f"\"минимальный тираж\": {value}\n"
            elif key == "max_published_amount":
                res_str += f"\"максимальный тираж\": {value}\n"
            elif key == "min_published_v_amount":
                res_str += f"\"минимальное количество выпущенных глав\": {value}\n"
            elif key == "max_published_v_amount":
                res_str += f"\"максимальное количество выпущенных глав\": {value}\n"
        return res_str

    @staticmethod
    def _after_remove_message(removed_amount, **kwargs) -> NoReturn:
        msg = Controller._make_remove_params_str(kwargs)
        after_remove_message_box = QMessageBox()
        after_remove_message_box.setWindowTitle("Удаление завершено")
        after_remove_message_box.setText(msg + f"\n Было удалено: {removed_amount}")
        after_remove_message_box.setIcon(QMessageBox.Information)
        after_remove_message_box.setStandardButtons(QMessageBox.Ok)
        after_remove_message_box.setDefaultButton(QMessageBox.Ok)
        after_remove_message_box.adjustSize()
        after_remove_message_box.exec()

    def _make_one_str_input_dialog_window(self, ui_dialog, dialog_window, icon_file, parameter_name, mode: Mode) \
            -> NoReturn:
        oneStrParameterDialog = QtWidgets.QDialog(parent=dialog_window)
        ui = Ui_oneStrParameterDialog()
        ui.setupUi(ui_dialog=ui_dialog,
                   oneStrParameterDialog=oneStrParameterDialog,
                   icon_file=icon_file,
                   parameter_name=parameter_name,
                   data_controller=self,
                   mode=mode)
        oneStrParameterDialog.show()

    @staticmethod
    def dialog_input_error(msg: str = "Что-то пошло не так") -> NoReturn:
        error_msg_box = QMessageBox()
        error_msg_box.setWindowTitle("Предупреждение")
        error_msg_box.setText(msg)
        error_msg_box.setIcon(QMessageBox.Warning)
        error_msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        error_msg_box.setDefaultButton(QMessageBox.Ok)
        error_msg_box.adjustSize()
        error_msg_box.exec()

    def one_str_param_complete_search(self, ui_search_dialog, param_to_search, multyparam: bool = False) -> NoReturn:
        if not multyparam:
            if param_to_search == "":
                self.dialog_input_error("Ничего не было подано на ввод")
                return
            ui_search_dialog.found_books = self._lib.search_for_books(self._search_type, book_name=param_to_search)
        if not ui_search_dialog.found_books:
            if multyparam:
                self.dialog_input_error(f"Совпадений с \"{', '.join(param_to_search['authors'])}\" и "
                                        f"\"{param_to_search['publishing_house']}\"не было найдено")
            else:
                self.dialog_input_error(f"Совпадений с \"{param_to_search}\" не было найдено")
        self._fill_table_in_ui_with_books(ui_search_dialog,
                                          books=ui_search_dialog.found_books,
                                          start_index=0,
                                          end_index=len(ui_search_dialog.found_books))
        ui_search_dialog.dialogButtonBox.button(ui_search_dialog.dialogButtonBox.Ok).setEnabled(False)

    def one_str_param_complete_remove(self, ui_main_window, param_to_remove, multyparam: bool = False) -> NoReturn:
        removed_amount = 0
        if not multyparam:
            if param_to_remove == "":
                self.dialog_input_error("Ничего не было подано на ввод")
                return
            removed_amount = self._lib.remove_books(self._remove_type, removing_book_name=param_to_remove)
            self._after_remove_message(removed_amount, removing_book_name=param_to_remove)
        else:
            removed_amount = self._lib.remove_books(self._remove_type,
                                                    publishing_house=param_to_remove["publishing_house"],
                                                    authors=param_to_remove["authors"])
            self._after_remove_message(removed_amount,
                                       publishing_house=param_to_remove["publishing_house"],
                                       authors=param_to_remove["authors"])
        if removed_amount > 0:
            self._lib.saved_flag = False
            self._sort_books_in_lib()
            self.load_current_page(ui_main_window)

    def _make_str_list_input_dialog_window(self, ui_dialog, dialog_window, icon_file, parameter_name, mode: Mode) \
            -> NoReturn:
        strListParameterDialog = QtWidgets.QDialog(parent=dialog_window)
        ui = Ui_strListParameterDialog()
        ui.setupUi(ui_dialog=ui_dialog,
                   strListParameterDialog=strListParameterDialog,
                   icon_file=icon_file,
                   parameter_name=parameter_name,
                   data_controller=self,
                   mode=mode)
        strListParameterDialog.show()

    def list_str_param_complete_search(self, ui_search_dialog, param_to_search, multyparam: bool = False) -> NoReturn:
        if not multyparam:
            if not param_to_search:
                self.dialog_input_error("Ничего не было подано на ввод")
                return
            ui_search_dialog.found_books = self._lib.search_for_books(self._search_type, authors=param_to_search)
        if not ui_search_dialog.found_books:
            if multyparam:
                self.dialog_input_error(f"Совпадений с \"{', '.join(param_to_search['authors'])}\" и "
                                        f"\"{param_to_search['publishing_house']}\"не было найдено")
            else:
                self.dialog_input_error(f"Совпадений с \"{', '.join(param_to_search)}\" не было найдено")
        self._fill_table_in_ui_with_books(ui_search_dialog,
                                          books=ui_search_dialog.found_books,
                                          start_index=0,
                                          end_index=len(ui_search_dialog.found_books))
        ui_search_dialog.dialogButtonBox.button(ui_search_dialog.dialogButtonBox.Ok).setEnabled(False)

    def list_str_param_complete_remove(self, ui_main_window, param_to_remove, multyparam: bool = False) -> NoReturn:
        removed_amount = 0
        if not multyparam:
            if not param_to_remove:
                self.dialog_input_error("Ничего не было подано на ввод")
                return
            removed_amount = self._lib.remove_books(self._remove_type, authors=param_to_remove)
            self._after_remove_message(removed_amount, authors=param_to_remove)
        else:
            removed_amount = self._lib.remove_books(self._remove_type,
                                                    publishing_house=param_to_remove["publishing_house"],
                                                    authors=param_to_remove["authors"])
            self._after_remove_message(removed_amount,
                                       publishing_house=param_to_remove["publishing_house"],
                                       authors=param_to_remove["authors"])
        if removed_amount > 0:
            self._lib.saved_flag = False
            self._sort_books_in_lib()
            self.load_current_page(ui_main_window)

    def _make_int_number_input_dialog_window(self, ui_dialog, dialog_window, icon_file, parameter_name, mode: Mode) \
            -> NoReturn:
        intNumberParameterDialog = QtWidgets.QDialog(parent=dialog_window)
        ui = Ui_intNumberParameterDialog()
        ui.setupUi(ui_dialog=ui_dialog,
                   intNumberParameterDialog=intNumberParameterDialog,
                   icon_file=icon_file,
                   parameter_name=parameter_name,
                   data_controller=self,
                   mode=mode)
        intNumberParameterDialog.show()

    def int_number_param_complete_search(self, ui_search_dialog, parameter, min_value: int, max_value: int) -> NoReturn:
        system_parameter: str = ""
        if parameter == "тираж":
            system_parameter = "published_amount"
        elif parameter == "количество томов":
            system_parameter = "volumes_amount"
        elif parameter == "выпущено томов":
            system_parameter = "published_v_amount"
        ui_search_dialog.found_books = self._lib.search_for_books(self._search_type,
                                                                  **{f"min_{system_parameter}": min_value,
                                                                     f"max_{system_parameter}": max_value})
        if not ui_search_dialog.found_books:
            self.dialog_input_error(f"Совпадений по параметру \"{parameter}\" не найдено\n"
                                    f" (минимальное значение: {min_value}, максимальное значение: {max_value})")
        self._fill_table_in_ui_with_books(ui_search_dialog,
                                          books=ui_search_dialog.found_books,
                                          start_index=0,
                                          end_index=len(ui_search_dialog.found_books))
        ui_search_dialog.dialogButtonBox.button(ui_search_dialog.dialogButtonBox.Ok).setEnabled(False)

    def int_number_param_complete_remove(self, ui_main_window, parameter, min_value: int, max_value: int) -> NoReturn:
        removed_amount = 0
        system_parameter: str = ""
        if parameter == "тираж":
            system_parameter = "published_amount"
        elif parameter == "количество томов":
            system_parameter = "volumes_amount"
        elif parameter == "выпущено томов":
            system_parameter = "published_v_amount"
        removed_amount = self._lib.remove_books(
            self._remove_type,
            **{f"min_{system_parameter}": min_value, f"max_{system_parameter}": max_value})
        self._after_remove_message(removed_amount,
                                   **{f"min_{system_parameter}": min_value, f"max_{system_parameter}": max_value})
        if removed_amount > 0:
            self._lib.saved_flag = False
            self._sort_books_in_lib()
            self.load_current_page(ui_main_window)

    def find_books(self, ui_search_dialog, search_dialog_window) -> NoReturn:
        if not self._search_type:
            ui_search_dialog.startSearch.setEnabled(False)
            self._search_remove_error(warning=False, msg="Не были выбраны критерии поиска!").exec()
        elif self._search_type == SearchRemoveBy.BOOK_NAME:
            self._find_books_by_name(ui_search_dialog, search_dialog_window)
        elif self._search_type == SearchRemoveBy.AUTHORS:
            self._find_books_by_authors(ui_search_dialog, search_dialog_window)
        elif self._search_type == SearchRemoveBy.PUBLISHING_HOUSE_AND_AUTHORS:
            self._find_books_by_publishing_house_and_authors(ui_search_dialog, search_dialog_window)
        elif self._search_type == SearchRemoveBy.PUBLISHED_AMOUNT:
            self._find_books_by_published_amount(ui_search_dialog, search_dialog_window)
        elif self._search_type == SearchRemoveBy.VOLUMES_AMOUNT:
            self._find_books_by_volumes_amount(ui_search_dialog, search_dialog_window)
        elif self._search_type == SearchRemoveBy.PUBLISHED_VOLUMES_AMOUNT:
            self._find_books_by_published_volumes_amount(ui_search_dialog, search_dialog_window)

    def _find_books_by_name(self, ui_search_dialog, search_dialog_window) -> NoReturn:
        self._make_one_str_input_dialog_window(
            ui_search_dialog,
            search_dialog_window,
            icon_file="icons/" \
                      "png-transparent-computer-icons-magnifying-glass-magnifier-magnifying-glass-text-interface-" \
                      "magnifier-thumbnail-removebg-preview.png",
            parameter_name="название книги",
            mode=Mode.SEARCH_MODE)

    def _find_books_by_authors(self, ui_search_dialog, search_dialog_window) -> NoReturn:
        self._make_str_list_input_dialog_window(
            ui_search_dialog,
            search_dialog_window,
            icon_file="icons/" \
                      "png-transparent-computer-icons-magnifying-glass-magnifier-magnifying-glass-text-interface-" \
                      "magnifier-thumbnail-removebg-preview.png",
            parameter_name="авторы",
            mode=Mode.SEARCH_MODE)

    def _find_books_by_publishing_house_and_authors(self, ui_search_dialog, search_dialog_window) -> NoReturn:
        icon_file = "icons/" \
                    "png-transparent-computer-icons-magnifying-glass-magnifier-magnifying-glass-text-interface-" \
                    "magnifier-thumbnail-removebg-preview.png"
        buffer = {"required_amount": 2}
        oneStrParameterDialog = QtWidgets.QDialog(parent=search_dialog_window)
        strListParameterDialog = QtWidgets.QDialog(parent=search_dialog_window)
        oneStrParameterDialog.rejected.connect(strListParameterDialog.close)
        strListParameterDialog.rejected.connect(oneStrParameterDialog.close)
        one_ui = Ui_oneStrParameterDialog()
        one_ui.setupUi(ui_dialog=ui_search_dialog,
                       oneStrParameterDialog=oneStrParameterDialog,
                       icon_file=icon_file,
                       parameter_name="издательство",
                       data_controller=self,
                       mode=Mode.SEARCH_MODE,
                       buffer=buffer)
        list_ui = Ui_strListParameterDialog()
        list_ui.setupUi(ui_dialog=ui_search_dialog,
                        strListParameterDialog=strListParameterDialog,
                        icon_file=icon_file,
                        parameter_name="авторы",
                        data_controller=self,
                        mode=Mode.SEARCH_MODE,
                        buffer=buffer)
        strListParameterDialog.show()
        oneStrParameterDialog.show()

    def _find_books_by_published_amount(self, ui_search_dialog, search_dialog_window) -> NoReturn:
        self._make_int_number_input_dialog_window(
            ui_search_dialog,
            search_dialog_window,
            icon_file="icons/" \
                      "png-transparent-computer-icons-magnifying-glass-magnifier-magnifying-glass-text-interface-" \
                      "magnifier-thumbnail-removebg-preview.png",
            parameter_name="тираж",
            mode=Mode.SEARCH_MODE)

    def _find_books_by_volumes_amount(self, ui_search_dialog, search_dialog_window) -> NoReturn:
        self._make_int_number_input_dialog_window(
            ui_search_dialog,
            search_dialog_window,
            icon_file="icons/" \
                      "png-transparent-computer-icons-magnifying-glass-magnifier-magnifying-glass-text-interface-" \
                      "magnifier-thumbnail-removebg-preview.png",
            parameter_name="количество томов",
            mode=Mode.SEARCH_MODE)

    def _find_books_by_published_volumes_amount(self, ui_search_dialog, search_dialog_window) -> NoReturn:
        self._make_int_number_input_dialog_window(
            ui_search_dialog,
            search_dialog_window,
            icon_file="icons/" \
                      "png-transparent-computer-icons-magnifying-glass-magnifier-magnifying-glass-text-interface-" \
                      "magnifier-thumbnail-removebg-preview.png",
            parameter_name="выпущено томов",
            mode=Mode.SEARCH_MODE)

    def choose_search_type(self, search_type) -> NoReturn:
        self._search_type = search_type

    def choose_remove_type(self, remove_type) -> NoReturn:
        self._remove_type = remove_type

    def remove_books(self, ui_main_window, mainWindow) -> NoReturn:
        if not self._remove_type:
            self._search_remove_error(warning=False, msg="Не были выбраны критерии поиска!").exec()
        elif self._remove_type == SearchRemoveBy.BOOK_NAME:
            self._remove_books_by_name(ui_main_window, mainWindow)
        elif self._remove_type == SearchRemoveBy.AUTHORS:
            self._remove_books_by_authors(ui_main_window, mainWindow)
        elif self._remove_type == SearchRemoveBy.PUBLISHING_HOUSE_AND_AUTHORS:
            self._remove_books_by_publishing_house_and_authors(ui_main_window, mainWindow)
        elif self._remove_type == SearchRemoveBy.PUBLISHED_AMOUNT:
            self._remove_books_by_published_amount(ui_main_window, mainWindow)
        elif self._remove_type == SearchRemoveBy.VOLUMES_AMOUNT:
            self._remove_books_volumes_amount(ui_main_window, mainWindow)
        elif self._remove_type == SearchRemoveBy.PUBLISHED_VOLUMES_AMOUNT:
            self._remove_books_by_published_volumes_amount(ui_main_window, mainWindow)

    def _remove_books_by_name(self, ui_remove_dialog, mainWindow) -> NoReturn:
        self._make_one_str_input_dialog_window(
            ui_remove_dialog,
            mainWindow,
            icon_file="icons/png-transparent-rubbish-bins-waste-paper-baskets-recycling-bin-computer-icons-trash-miscellaneous-recycling-logo-thumbnail-removebg-preview.png",
            parameter_name="название книги",
            mode=Mode.REMOVE_MODE)

    def _remove_books_by_authors(self, ui_remove_dialog, mainWindow) -> NoReturn:
        self._make_str_list_input_dialog_window(
            ui_remove_dialog,
            mainWindow,
            icon_file="icons/png-transparent-rubbish-bins-waste-paper-baskets-recycling-bin-computer-icons-trash-miscellaneous-recycling-logo-thumbnail-removebg-preview.png",
            parameter_name="авторы",
            mode=Mode.REMOVE_MODE)

    def _remove_books_by_publishing_house_and_authors(self, ui_remove_dialog, mainWindow) -> NoReturn:
        icon_file = "icons/png-transparent-rubbish-bins-waste-paper-baskets-recycling-bin-computer-icons-trash-miscellaneous-recycling-logo-thumbnail-removebg-preview.png"
        buffer = {"required_amount": 2}
        oneStrParameterDialog = QtWidgets.QDialog(parent=mainWindow)
        strListParameterDialog = QtWidgets.QDialog(parent=mainWindow)
        oneStrParameterDialog.rejected.connect(strListParameterDialog.close)
        strListParameterDialog.rejected.connect(oneStrParameterDialog.close)
        one_ui = Ui_oneStrParameterDialog()
        one_ui.setupUi(ui_dialog=ui_remove_dialog,
                       oneStrParameterDialog=oneStrParameterDialog,
                       icon_file=icon_file,
                       parameter_name="издательство",
                       data_controller=self,
                       mode=Mode.REMOVE_MODE,
                       buffer=buffer)
        list_ui = Ui_strListParameterDialog()
        list_ui.setupUi(ui_dialog=ui_remove_dialog,
                        strListParameterDialog=strListParameterDialog,
                        icon_file=icon_file,
                        parameter_name="авторы",
                        data_controller=self,
                        mode=Mode.REMOVE_MODE,
                        buffer=buffer)
        strListParameterDialog.show()
        oneStrParameterDialog.show()

    def _remove_books_by_published_amount(self, ui_remove_dialog, mainWindow) -> NoReturn:
        self._make_int_number_input_dialog_window(
            ui_remove_dialog,
            mainWindow,
            icon_file="icons/png-transparent-rubbish-bins-waste-paper-baskets-recycling-bin-computer-icons-trash-miscellaneous-recycling-logo-thumbnail-removebg-preview.png",
            parameter_name="тираж",
            mode=Mode.REMOVE_MODE)

    def _remove_books_volumes_amount(self, ui_remove_dialog, mainWindow) -> NoReturn:
        self._make_int_number_input_dialog_window(
            ui_remove_dialog,
            mainWindow,
            icon_file="icons/png-transparent-rubbish-bins-waste-paper-baskets-recycling-bin-computer-icons-trash-miscellaneous-recycling-logo-thumbnail-removebg-preview.png",
            parameter_name="количество томов",
            mode=Mode.REMOVE_MODE)

    def _remove_books_by_published_volumes_amount(self, ui_remove_dialog, mainWindow) -> NoReturn:
        self._make_int_number_input_dialog_window(
            ui_remove_dialog,
            mainWindow,
            icon_file="icons/png-transparent-rubbish-bins-waste-paper-baskets-recycling-bin-computer-icons-trash-miscellaneous-recycling-logo-thumbnail-removebg-preview.png",
            parameter_name="выпущено томов",
            mode=Mode.REMOVE_MODE)

    def add_book_dialog(self, ui_main_window, mainWindow) -> NoReturn:
        addDialog = QtWidgets.QDialog(parent=mainWindow)
        ui = Ui_addDialog()
        ui.setupUi(ui_main_window, self, addDialog)
        addDialog.show()

    def add_book(self, ui_main_window, book_params: Dict[str, Any]) -> NoReturn:
        self._lib.add_book(book_params)
        add_msg_box = QMessageBox()
        add_msg_box.setWindowTitle("Книга добавлена")
        add_msg_box.setText(str(Book(**book_params)))
        add_msg_box.setIcon(QMessageBox.Information)
        add_msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        add_msg_box.setDefaultButton(QMessageBox.Ok)
        add_msg_box.adjustSize()
        add_msg_box.exec()
        self._lib.saved_flag = False
        self._sort_books_in_lib()
        self.load_current_page(ui_main_window)
