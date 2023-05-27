from PyQt5 import QtCore, QtGui, QtWidgets
from input_name_dialog import Ui_inputNameDialog

class Ui_recordsDialog(object):

    def _connect_input_dialog_accepted(self, level_records, new_name, new_scores):
        if len(level_records.keys()) == 5:
            self._replace_last_element(level_records, new_name, new_scores)
        else:
            level_records[new_name] = new_scores
            index = len(level_records.keys()) - 1
            self.recordsTable.setItem(index, 0, QtWidgets.QTableWidgetItem())
            self.recordsTable.setItem(index, 1, QtWidgets.QTableWidgetItem())
        level_records = dict(sorted(level_records.items(), key=lambda item: item[1], reverse=True))
        i = 0
        for name, record_score in level_records.items():
            self.recordsTable.item(i, 0).setText(name)
            self.recordsTable.item(i, 1).setText(str(record_score))
            i += 1
        self.scoreDialogButtonBox.button(self.scoreDialogButtonBox.StandardButton.Ok).setEnabled(True)

    def setupUi(self, recordsDialog, config, new_record_scores: int = 0):
        if new_record_scores != 0:
            self._make_new_dialog_window(recordsDialog, config.level_records, new_record_scores)

        recordsDialog.setObjectName("recordsDialog")
        recordsDialog.resize(621, 233)
        recordsDialog.setStyleSheet("background-color: rgb(208, 129, 213);")
        self.scoreDialogButtonBox = QtWidgets.QDialogButtonBox(recordsDialog)
        self.scoreDialogButtonBox.setGeometry(QtCore.QRect(450, 190, 171, 32))
        self.scoreDialogButtonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scoreDialogButtonBox.setStyleSheet("background-color: rgb(187, 141, 239);")
        self.scoreDialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.scoreDialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.scoreDialogButtonBox.setObjectName("scoreDialogButtonBox")
        self.scoreDialogButtonBox.button(self.scoreDialogButtonBox.StandardButton.Ok).setEnabled(False)
        if new_record_scores != 0:
            self.scoreDialogButtonBox.accepted.connect(lambda: config.update_level_config())
        self.recordsTable = QtWidgets.QTableWidget(recordsDialog)
        self.recordsTable.setGeometry(QtCore.QRect(0, 0, 621, 181))
        self.recordsTable.setStyleSheet("background-color: rgb(187, 141, 239);")
        self.recordsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.recordsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.recordsTable.setObjectName("recordsTable")
        self.recordsTable.setColumnCount(2)
        self.recordsTable.setRowCount(5)
        self.recordsTable.setEnabled(False)
        item = QtWidgets.QTableWidgetItem()
        self.recordsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordsTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordsTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordsTable.setHorizontalHeaderItem(1, item)
        self.recordsTable.horizontalHeader().setDefaultSectionSize(298)
        self.recordsTable.horizontalHeader().setMinimumSectionSize(198)

        self.retranslateUi(recordsDialog, config.level_records)
        self.scoreDialogButtonBox.accepted.connect(recordsDialog.accept)
        self.scoreDialogButtonBox.rejected.connect(recordsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(recordsDialog)

    def _replace_last_element(self, level_records, new_name: str, new_scores):
        i = 0
        name_to_change = ""
        for name, _ in level_records.items():
            if i == 4:
                name_to_change = name
            i += 1
        del level_records[name_to_change]
        level_records[new_name] = new_scores

    def _make_new_dialog_window(self, recordsDialog, level_records, new_record_scores):
        inputNameDialog = QtWidgets.QDialog(parent=recordsDialog)
        ui_input_dialog = Ui_inputNameDialog()
        ui_input_dialog.setupUi(inputNameDialog)
        inputNameDialog.show()
        ui_input_dialog.inputNameDialogButtonBox.accepted.connect(
            lambda: self._connect_input_dialog_accepted(level_records, ui_input_dialog.new_record,
                                                        new_record_scores))
        inputNameDialog.rejected.connect(
            lambda: self._make_new_dialog_window(recordsDialog, level_records, new_record_scores))

    def retranslateUi(self, recordsDialog, level_records):
        _translate = QtCore.QCoreApplication.translate
        recordsDialog.setWindowTitle(_translate("recordsDialog", f"Records of this level"))
        item = self.recordsTable.verticalHeaderItem(0)
        item.setText(_translate("recordsDialog", "1"))
        item = self.recordsTable.verticalHeaderItem(1)
        item.setText(_translate("recordsDialog", "2"))
        item = self.recordsTable.verticalHeaderItem(2)
        item.setText(_translate("recordsDialog", "3"))
        item = self.recordsTable.verticalHeaderItem(3)
        item.setText(_translate("recordsDialog", "4"))
        item = self.recordsTable.verticalHeaderItem(4)
        item.setText(_translate("recordsDialog", "5"))
        item = self.recordsTable.horizontalHeaderItem(0)
        item.setText(_translate("recordsDialog", "User name"))
        item = self.recordsTable.horizontalHeaderItem(1)
        item.setText(_translate("recordsDialog", "Scores"))
        i = 0
        for player_name, player_score in level_records.items():
            self.recordsTable.setItem(i, 0, QtWidgets.QTableWidgetItem(player_name))
            self.recordsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(player_score)))
            i += 1

def make_record_dialog(config, new_record: int = 0):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    recordsDialog = QtWidgets.QDialog()
    ui = Ui_recordsDialog()
    ui.setupUi(recordsDialog, config, new_record)
    recordsDialog.show()
    app.exec()
