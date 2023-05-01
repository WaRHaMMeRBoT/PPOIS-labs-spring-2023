import Commands
import RailRoadFile
import sys
from PyQt6.QtWidgets import QApplication
import App
import Test


def main():
    railroad = [RailRoadFile.RailRoad([], {}, [])]
    railroad[0] = Test.rail
    is_app = input('App or console?').lower()
    if is_app == 'app':
        app = QApplication(sys.argv)

        window = App.MainWindow(railroad)
        window.show()

        app.exec()
    elif is_app == 'console':
        print('input command')
        while True:
            session_ended = Commands.get_command(railroad)
            if session_ended:
                break


if __name__ == '__main__':
    main()