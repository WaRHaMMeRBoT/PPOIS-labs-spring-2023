#Author: Vodohleb04

from PyQt5 import QtCore, QtWidgets
from emitter_wraper import before_done_emitter, after_done_emitter
from ecosystem import EcoSystem
import create_new_world_dialog
import game_main_window_gui
import test_add_creatures_dialog
import configs
import unittest
import copy
import sys
import datetime
from hashlib import md5


LOGFILE = "../log_lr4.txt"


class TestSignals(QtCore.QObject):
    before_ecosystem_update = QtCore.pyqtSignal()
    creature_removed = QtCore.pyqtSignal()
    deadly_worm_signal = QtCore.pyqtSignal()
    apocalypse_signal = QtCore.pyqtSignal()
    after_apocalypse_signal = QtCore.pyqtSignal(EcoSystem)
    after_adding_creatures_signal = QtCore.pyqtSignal()
    set_world_name_signal = QtCore.pyqtSignal(EcoSystem)
    world_loaded_signal = QtCore.pyqtSignal(EcoSystem)
    save_world_called_signal = QtCore.pyqtSignal(str)
    world_saved_signal = QtCore.pyqtSignal(str)
    world_changed_signal = QtCore.pyqtSignal()
    leave_world_signal = QtCore.pyqtSignal(bool)


class TestWindow(game_main_window_gui.CustomMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.test_signals = TestSignals()


class TestUi_MainWindow(game_main_window_gui.Ui_MainWindow):
    def setupUi(self, MainWindow: TestWindow, ecosystem: EcoSystem):
        super().setupUi(MainWindow, ecosystem)

        self._remove_creature = after_done_emitter(MainWindow.test_signals.world_changed_signal)(
            before_done_emitter(MainWindow.test_signals.before_ecosystem_update)(
                after_done_emitter(MainWindow.test_signals.creature_removed)(super()._remove_creature)))
        self._wake_deadly_worm = after_done_emitter(MainWindow.test_signals.world_changed_signal)(
            after_done_emitter(MainWindow.test_signals.deadly_worm_signal)(super()._wake_deadly_worm))
        self._apocalypse = after_done_emitter(MainWindow.test_signals.world_changed_signal)(
            after_done_emitter(MainWindow.test_signals.apocalypse_signal)(super()._apocalypse))
        self._next_period = after_done_emitter(
            MainWindow.test_signals.world_changed_signal)(super()._next_period)

    def _add_creatures_dialog(self, MainWindow: TestWindow, ecosystem: EcoSystem) -> None:
        """Creates dialog to add creatures (CustomAddCreaturesDialog) to selected hectare of forest

        MainWindow - main window of program
        ecosystem - data controller part of program
        """
        self._pause_game()
        add_creatures_dialog_window = test_add_creatures_dialog.TestCustomAddCreaturesDialog(parent=MainWindow)
        add_creatures_dialog_window.accepted.connect(
            lambda: self.statusBar.showMessage(configs.GuiMessages.CREATURES_ADDED.value, configs.MESSAGE_DURATION))
        add_creatures_dialog_window.addCreaturesSignal.updateMapSignal.connect(lambda: self._update(ecosystem))
        add_creatures_dialog_window.addCreaturesSignal.updateMapSignal.connect(
            MainWindow.test_signals.world_changed_signal.emit)
        add_creatures_dialog_window.accepted.connect(lambda: self._continue_game(MainWindow.game_running_flag))
        add_creatures_dialog_window.rejected.connect(lambda: self._continue_game(MainWindow.game_running_flag))
        add_creatures_dialog_window.addCreaturesSignal.before_update_ecosystem.connect(
            MainWindow.test_signals.before_ecosystem_update.emit)
        add_creatures_dialog_window.addCreaturesSignal.updateMapSignal.connect(
            MainWindow.test_signals.after_adding_creatures_signal.emit)
        ui = test_add_creatures_dialog.Ui_addCreaturesDialog()
        ui.setupUi(add_creatures_dialog_window,
                   ecosystem,
                   self.worldMapTable.currentItem().row(),
                   self.worldMapTable.currentItem().column())
        add_creatures_dialog_window.show()
        add_creatures_dialog_window.exec()

    def _make_new_world_dialog(self, MainWindow: TestWindow, ecosystem: EcoSystem) -> None:
        """Creates newWorldDialog to make new world

        MainWindow - main window of program
        ecosystem - data controller part of program
        """
        new_world_dialog = create_new_world_dialog.CustomNewWorldDialog(parent=MainWindow)
        new_world_dialog.newWorldAcceptedSignals.world_is_made_message_signal.connect(self._new_world_done_message)
        new_world_dialog.newWorldAcceptedSignals.world_is_made_signal.connect(self._new_world_done)
        new_world_dialog.newWorldAcceptedSignals.game_is_running_signal.connect(MainWindow.raise_running_game_flag)
        new_world_dialog.newWorldAcceptedSignals.game_is_running_signal.connect(
            lambda: self.showMapAction.setCheckable(True))
        new_world_dialog.newWorldAcceptedSignals.game_is_running_signal.connect(MainWindow.lower_tool_bar_active_flag)
        new_world_dialog.newWorldAcceptedSignals.world_is_made_signal.connect(
            MainWindow.test_signals.set_world_name_signal.emit)
        ui = create_new_world_dialog.Ui_newWorldDialog()
        ui.setupUi(new_world_dialog, ecosystem)
        new_world_dialog.show()
        new_world_dialog.exec()

    def _showLoadFileDialog(self, MainWindow: TestWindow, ecosystem: EcoSystem) -> None:
        MainWindow.test_signals.before_ecosystem_update.emit()
        super()._showLoadFileDialog(MainWindow, ecosystem)
        MainWindow.test_signals.world_loaded_signal.emit(ecosystem)

    def _showSaveFileDialog(self, MainWindow: TestWindow, ecosystem: EcoSystem) -> None:
        if MainWindow.game_running_flag:
            MainWindow.test_signals.save_world_called_signal.emit(ecosystem.filename)
            super()._showSaveFileDialog(MainWindow, ecosystem)
            MainWindow.test_signals.world_saved_signal.emit(ecosystem.filename)

    def _simple_save_of_game(self, MainWindow: TestWindow, ecosystem: EcoSystem) -> None:
        if MainWindow.game_running_flag:
            MainWindow.test_signals.save_world_called_signal.emit(ecosystem.filename)
            super()._simple_save_of_game(MainWindow, ecosystem)
            MainWindow.test_signals.world_saved_signal.emit(ecosystem.filename)

    def _leave_world(self, MainWindow: TestWindow, ecosystem: EcoSystem) -> None:
        game_was_running_flag = MainWindow.game_running_flag
        super()._leave_world(MainWindow, ecosystem)
        MainWindow.test_signals.leave_world_signal.emit(game_was_running_flag)



class TestGuiApp(unittest.TestCase):

    def setUp(self) -> None:
        self.log_file = open("../log_lr4.txt", 'w')
        self.run_start = datetime.datetime.now()
        self.log_file.write(f"|-|Test run started at {self.run_start}|-|\n")
        self.app = QtWidgets.QApplication(sys.argv)
        self.current_ecosystem = EcoSystem()
        self.previous_ecosystem = copy.deepcopy(self.current_ecosystem)
        self.MainWindow = TestWindow()
        self.current_creature = None
        self.ecosystem_changed_flag = False
        self.save_filename = ""
        self.old_save_hash = None
        self.MainWindow.test_signals.world_changed_signal.connect(self.world_changed)
        self.MainWindow.test_signals.before_ecosystem_update.connect(self.save_previous_ecosystem)
        self.MainWindow.test_signals.creature_removed.connect(self.creature_removed_successfully)
        self.MainWindow.test_signals.deadly_worm_signal.connect(self.deadly_worm_done)
        self.MainWindow.test_signals.apocalypse_signal.connect(self.apocalypse)
        self.MainWindow.test_signals.after_adding_creatures_signal.connect(self.add_creatures)
        self.MainWindow.test_signals.set_world_name_signal.connect(self.set_world_name)
        self.MainWindow.test_signals.world_loaded_signal.connect(self.world_loaded)
        self.MainWindow.test_signals.save_world_called_signal.connect(self.count_old_save_file_hash)
        self.MainWindow.test_signals.world_saved_signal.connect(self.compare_save_files_hash)
        self.MainWindow.test_signals.leave_world_signal.connect(self.leave_world)

    def save_previous_ecosystem(self):
        self.previous_ecosystem = copy.deepcopy(self.current_ecosystem)

    def run_test_window(self) -> None:
        ui = TestUi_MainWindow()
        ui.setupUi(self.MainWindow, self.current_ecosystem)
        ui.cellDataListWidget.currentItemChanged.connect(
            lambda: self.set_current_creature(ui.cellDataListWidget))
        self.MainWindow.show()
        self.app.exec_()

    def test_run(self):
        self.assertEqual(self.run_test_window(), None)
        self.log_file.write("app test run successful\n")

    def set_current_creature(self, cellDataListWidget):
        if cellDataListWidget.currentItem():
            self.current_creature = cellDataListWidget.currentItem().text()

    def creature_removed_successfully(self):
        print(self.current_creature)
        self.assertEqual(self.current_ecosystem.count_creatures_amount(),
                         self.previous_ecosystem.count_creatures_amount() - 1)
        self.assertIsNone(self.current_ecosystem.find_creature(self.current_creature))
        self.assertIsNotNone(self.previous_ecosystem.find_creature(self.current_creature))
        self.log_file.write("creature removed done\n")

    def deadly_worm_done(self):
        for hectare_line in self.current_ecosystem.forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    self.assertFalse(creature.is_dead())
        self.log_file.write("deadly worm done\n")

    def apocalypse(self):
        for hectare_line in self.current_ecosystem.forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    self.assertTrue(creature.is_dead())
        self.MainWindow.test_signals.after_apocalypse_signal.emit(self.current_ecosystem)
        self.assertTrue(self.current_ecosystem.is_wasteland())
        self.log_file.write("apocalypse done\n")

    def add_creatures(self):
        self.assertNotEqual(self.current_ecosystem, self.previous_ecosystem)
        self.log_file.write("add_creatures done\n")

    def set_world_name(self, ecosystem: EcoSystem):
        self.assertEqual(ecosystem, self.current_ecosystem)
        self.save_filename = ecosystem.filename
        self.ecosystem_changed_flag = False
        self.log_file.write(f"World is created. Save filename: {self.save_filename}\n")

    def world_loaded(self, ecosystem: EcoSystem):
        self.assertEqual(ecosystem, self.current_ecosystem)
        self.save_filename = ecosystem.filename
        self.ecosystem_changed_flag = False
        self.log_file.write(f"World loaded from file {self.save_filename}\n")

    def count_old_save_file_hash(self, filename):
        from pathlib import Path
        self.log_file.write("===Saving file===\n")
        if Path.is_file(Path(filename)):
            with open(filename, "r") as old_save_file:
                self.old_save_hash = md5(old_save_file.read().encode("UTF-8")).hexdigest()
                self.log_file.write(f"\tHash of file {self.save_filename} before saving: {self.old_save_hash}\n")

    def compare_save_files_hash(self, filename):
        from pathlib import Path
        self.assertTrue(Path.is_file(Path(filename)))
        with open(filename, "r") as new_save_file:
            if self.old_save_hash:
                if self.ecosystem_changed_flag:
                    self.assertNotEqual(self.old_save_hash, md5(new_save_file.read().encode("UTF-8")).hexdigest())
                    self.log_file.write(f"\tHash of file {self.save_filename} after saving:"
                          f" {md5(new_save_file.read().encode('UTF-8')).hexdigest()}\n")
                else:
                    self.assertEqual(self.old_save_hash, md5(new_save_file.read().encode("UTF-8")).hexdigest())
                    self.log_file.write(f"\tHash of file {self.save_filename} after saving: {self.old_save_hash}\n")
        self.ecosystem_changed_flag = False
        self.log_file.write(f"===\tSaving to {filename} ended successfully===\n")

    def world_changed(self):
        self.ecosystem_changed_flag = True

    def leave_world(self, game_was_running_flag: bool):
        self.assertFalse(self.MainWindow.game_running_flag)
        if game_was_running_flag:
            self.log_file.write("World leaved successfully\n")
        else:
            self.log_file.write("Leave world doesn't make any changes, as it was expected. Everything ok\n")

    def tearDown(self):
        run_end = datetime.datetime.now()
        self.log_file.write(f"|=|Test run done at {run_end}."
                            f" Duration: {(run_end - self.run_start).total_seconds()}|=|\n")
        self.log_file.close()


def run_testing_mode():
    unittest.main(__name__, argv=['main'], exit=False)
    print(f"Logfile: {LOGFILE}")

