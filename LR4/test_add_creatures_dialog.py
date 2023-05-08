#Author: Vodohleb04

from ecosystem import EcoSystem
from emitter_wraper import before_done_emitter, after_done_emitter
from add_creatures_dialog import Ui_addCreaturesDialog, AddCreaturesSignal
from PyQt5 import QtCore, QtWidgets


class TestCreaturesSignal(AddCreaturesSignal):
    before_update_ecosystem = QtCore.pyqtSignal()


class TestCustomAddCreaturesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        """Creates custom dialog window that can emit signal"""
        self.addCreaturesSignal = TestCreaturesSignal()
        QtWidgets.QWidget.__init__(self, parent)


class Ui_testAddCreaturesDialog(Ui_addCreaturesDialog):
    def setupUi(self, testAddCreaturesDialog: TestCustomAddCreaturesDialog, ecosystem: EcoSystem,
                vertical_hectare_number, horizontal_hectare_number) -> None:
        self._add_creature = before_done_emitter(
            testAddCreaturesDialog.addCreaturesSignal.before_update_ecosystem)(super()._add_creature)
        self._add_creatures_to_ecosystem = after_done_emitter(
            testAddCreaturesDialog.addCreaturesSignal.updateMapSignal)(super()._add_creatures_to_ecosystem)
