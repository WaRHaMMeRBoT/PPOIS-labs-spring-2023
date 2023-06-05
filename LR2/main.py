import xml.sax
import xml.dom.minidom

from tkinter import *
from tkinter import ttk
from person import *
from FootbalHandlerSax import *
from MainWindow import *
from domXml import *
from readParser import *


if __name__ == "__main__":
    window = MainWindow(read_parser("players.xml").information)
