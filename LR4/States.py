from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class StationState(QMainWindow):
    def __init__(self, parent=None, nodes_list=[], title=''):
        super(StationState, self).__init__(parent)

        self.nodes_list = nodes_list
        self.setWindowTitle(title)
        self.setFixedSize(QSize(400, 300))

        self.text = QTextBrowser(self)
        self.text.resize(400, 300)
        self.text.setAcceptRichText(True)
        self.text.setOpenExternalLinks(True)

        for node in self.nodes_list:
            self.text.append(f'{node.name} - Goods: {node.storage.print_goods()}')


class WaysState(QMainWindow):
    def __init__(self, parent=None, nodes_list=[], edges_list={}, title=''):
        super(WaysState, self).__init__(parent)

        self.nodes_list = nodes_list
        self.edges_list = edges_list
        self.setWindowTitle(title)
        self.setFixedSize(QSize(400, 300))

        self.text = QTextBrowser(self)
        self.text.resize(400, 300)
        self.text.setAcceptRichText(True)
        self.text.setOpenExternalLinks(True)

        for node_1 in self.nodes_list:
            for node_2 in self.nodes_list:
                if self.edges_list[node_1].get(node_2):
                    self.text.append(f'{node_1.name} - {node_2.name} - {edges_list[node_1].get(node_2)}')


class RailWayState(QMainWindow):
    def __init__(self, parent=None, nodes_list=[], edges_list={}, trains_list=[], title=''):
        super(RailWayState, self).__init__(parent)

        self.trains_list = trains_list
        self.nodes_list = nodes_list
        self.edges_list = edges_list
        self.setWindowTitle(title)
        self.setFixedSize(QSize(400, 300))

        self.text = QTextBrowser(self)
        self.text.resize(400, 300)
        self.text.setAcceptRichText(True)
        self.text.setOpenExternalLinks(True)

        self.text.append('Станции:')
        for node in self.nodes_list:
            self.text.append(f'{node.name} - Goods: {node.storage.print_goods()}')

        self.text.append('Пути')
        for node_1 in self.nodes_list:
            for node_2 in self.nodes_list:
                if self.edges_list[node_1].get(node_2):
                    self.text.append(f'{node_1.name} - {node_2.name} - {edges_list[node_1].get(node_2)}')

        self.text.append('Поезда')
        for train in self.trains_list:
            self.text.append(
                f'Train index : {self.trains_list.index(train)} -Current point and distance : {train.current_point.name} {train.distance} '
                f'Speed: {train.speed} Goods: {train.print_goods()}')


class TrainsState(QMainWindow):
    def __init__(self, parent=None, trains_list=[], title=''):
        super(TrainsState, self).__init__(parent)

        self.trains_list = trains_list
        self.setWindowTitle(title)
        self.setFixedSize(QSize(400, 300))

        self.text = QTextBrowser(self)
        self.text.resize(400, 300)
        self.text.setAcceptRichText(True)
        self.text.setOpenExternalLinks(True)

        self.text.append('Поезда')
        for train in self.trains_list:
            self.text.append(
                f'Train index : {self.trains_list.index(train)} Current point and distance : {train.current_point.name} {train.distance} '
                f'Speed: {train.speed} Goods: {train.print_goods()}')
