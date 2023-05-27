from PyQt5 import QtCore, QtGui, QtWidgets
from config_controller import ConfigController
#187, 141, 239

class Ui_helpDialog(object):
    def setupUi(self, helpDialog, config: ConfigController):
        helpDialog.setObjectName("helpDialog")
        helpDialog.resize(581, 250)
        helpDialog.setStyleSheet("background-color: rgb(202, 178, 230);")
        helpDialog.setSizeGripEnabled(False)
        helpDialog.setModal(False)
        self.okButton = QtWidgets.QPushButton(helpDialog)
        self.okButton.setGeometry(QtCore.QRect(540, 150, 41, 34))
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setStyleSheet("background-color: rgb(187, 141, 239);")
        self.okButton.setObjectName("okButton")
        self.textArea = QtWidgets.QTextBrowser(helpDialog)
        self.textArea.setGeometry(QtCore.QRect(0, 0, 581, 150))
        self.textArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textArea.setObjectName("textArea")
        self.helpComboBox = QtWidgets.QComboBox(helpDialog)
        self.helpComboBox.setGeometry(QtCore.QRect(0, 150, 281, 32))
        self.helpComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpComboBox.setStyleSheet("background-color: rgb(187, 141, 239);")
        self.helpComboBox.setObjectName("helpComboBox")
        self.helpComboBox.addItem("")
        self.helpComboBox.addItem("")
        self.helpComboBox.addItem("")
        self.okButton.clicked.connect(helpDialog.accept)
        self.retranslateUi(helpDialog)
        QtCore.QMetaObject.connectSlotsByName(helpDialog)

        self.helpComboBox.currentIndexChanged.connect(lambda: self.connect_clicked_checkbox(config))

    def retranslateUi(self, helpDialog):
        _translate = QtCore.QCoreApplication.translate
        helpDialog.setWindowTitle(_translate("helpDialog", "Help dialog"))
        self.okButton.setText(_translate("helpDialog", "OK"))
        self.helpComboBox.setItemText(0, _translate("helpDialog", "What do you want to know?"))
        self.helpComboBox.setItemText(1, _translate("helpDialog", "General information about the game"))
        self.helpComboBox.setItemText(2, _translate("helpDialog", "Bricks particular qualities"))

    def connect_clicked_checkbox(self, config: ConfigController):
        if self.helpComboBox.currentIndex() == 0:
            self.textArea.setText(config.help_messages["start_message"])
        elif self.helpComboBox.currentIndex() == 1:
            self.textArea.setText(config.help_messages["general_info"])
        elif self.helpComboBox.currentIndex() == 2:
            self.textArea.setText(config.help_messages["bricks_info"])
        else:
            raise ValueError("Unexpected index")

def make_help_dialog(config: ConfigController):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    helpDialog = QtWidgets.QDialog()
    ui = Ui_helpDialog()
    ui.setupUi(helpDialog, config)
    helpDialog.show()
    app.exec_()