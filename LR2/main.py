from Controller import Controller
from View import MainApp

##Controller("E:\\universityProgs\\Lab2\\data.xml")
if __name__ == '__main__':
    controller = Controller("data.xml")
    MainApp(controller).run()