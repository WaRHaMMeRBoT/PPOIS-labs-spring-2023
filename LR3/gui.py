import sys
import threading
import time
from io import StringIO
import signal
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QTimer
import pickle

from classes.impl import Seed, Watering, Weed


class MainWindow(QMainWindow):
    def __init__(self, garden, buffer: StringIO, parent=None):
        super().__init__(parent)
        self.garden = garden
        self.__buffer = buffer
        self.setupUi()
    
    def setupUi(self):
        self.setWindowTitle("Garden")
        self.move(300, 300)
        self.resize(960, 540)

        sd_button = QPushButton('New Seed', self)
        sd_button.setToolTip('Plant a new seed')
        sd_button.move(0, 28 * 0)
        sd_button.clicked.connect(self.on_sd)

        tr_button = QPushButton('New Tree', self)
        tr_button.setToolTip('Plant a new fruit tree')
        tr_button.move(0, 28 * 1)
        tr_button.clicked.connect(self.on_tr)

        fl_button = QPushButton('Fertile', self)
        fl_button.setToolTip('Fertile the garden')
        fl_button.move(0, 28 * 2)       
        fl_button.clicked.connect(self.on_fl)

        cr_button = QPushButton('Cure', self)
        cr_button.setToolTip('Show some love for the garden')
        cr_button.move(0, 28 * 3)
        cr_button.clicked.connect(self.on_cr)

        wt_button = QPushButton('Water', self)
        wt_button.setToolTip('Water the garden')
        wt_button.move(0, 28 * 4)
        wt_button.clicked.connect(self.on_wt)

        wd_button = QPushButton('Weed', self)
        wd_button.setToolTip('Remove unwanted plants')
        wd_button.move(0, 28 * 5)
        wd_button.clicked.connect(self.on_wd)

        rt_button = QPushButton('Remove a tree', self)
        rt_button.setToolTip('Chop down a tree')
        rt_button.move(0, 28 * 6)
        rt_button.clicked.connect(self.on_rt)

        rs_button = QPushButton('Remove a seed', self)
        rs_button.setToolTip('Remove a seed')
        rs_button.move(0, 28 * 7)
        rs_button.clicked.connect(self.on_rs)

        rv_button = QPushButton('Gather', self)
        rv_button.setToolTip('Gather vegetables')
        rv_button.move(0, 28 * 8)
        rv_button.clicked.connect(self.on_rv)

        rw_button = QPushButton('Remove Weed', self)
        rw_button.setToolTip('Remove unwanted plants')
        rw_button.move(0, 28 * 9)
        rw_button.clicked.connect(self.on_rw)

        ex_button = QPushButton('Save and Exit', self)
        ex_button.setToolTip('Exit the app')
        ex_button.move(0, 28 * 10)
        ex_button.clicked.connect(self.on_ex)

        self.text_box = QPlainTextEdit(self)
        self.text_box.move(100, 0)
        self.text_box.setReadOnly(True)
        self.text_box.resize(720, 280)

        self.update_text()
        self.my_timer = QTimer()
        self.my_timer.timeout.connect(self.update_text)
        self.my_timer.start(100)
       
    @pyqtSlot()
    def update_text(self):
        if(len(self.__buffer.getvalue()) != 0):
            self.text_box.appendPlainText(self.__buffer.getvalue())
            self.__buffer.truncate(0)

    @pyqtSlot()
    def on_sd(self):
        self.garden.new_seed()
   
    @pyqtSlot()
    def on_tr(self):
        self.garden.new_fruit_tree()
    
    @pyqtSlot()
    def on_fl(self):
        self.garden.fertile_garden()
    
    @pyqtSlot()
    def on_cr(self):
        self.garden.love_garden()
   
    @pyqtSlot()
    def on_wt(self):
        watering = Watering()
        watering.pour_bed(self.garden.bed)
   
    @pyqtSlot()
    def on_wd(self):
        self.garden.weeding_garden()

    @pyqtSlot()
    def on_rt(self):
        for tree in self.garden.trees:
            if tree is None:
                continue
            self.garden.get_trees().remove(tree)
            break
    
    @pyqtSlot()
    def on_rs(self):
        for plant in self.garden.bed.place:
            if plant is None:
                continue
            if isinstance(plant, Seed):
                self.garden.bed.remove_from_bed(plant)
                break
    @pyqtSlot()
    def on_rv(self):
        for plant in self.garden.bed.place:
            if plant is None:
                continue
            if not isinstance(plant, (Weed, Seed)):
                self.garden.bed.remove_from_bed(plant)
                break
    
    @pyqtSlot()
    def on_rw(self):
        for plant in self.garden.bed.place:
            if plant is None:
                continue
            if isinstance(plant, Weed):
                self.garden.bed.remove_from_bed(plant)
                break

    @pyqtSlot()
    def on_ex(self):
        with open("store.pickle", "wb") as f:
            pickle.dump(self.garden, f)
        self.garden.is_on = False
        self.garden.is_saved = True
        self.close()
        thread_id = threading.get_ident()
        signal.pthread_kill(thread_id, signal.SIGINT)

    def closeEvent(self, event):
        thread_id = threading.get_ident()
        signal.pthread_kill(thread_id, signal.SIGINT)
        event.accept()