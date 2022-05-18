import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore

# References: https://pythonspot.com/pyqt5-image/
#             https://stackoverflow.com/questions/1925015/pyqt-always-on-top
#             https://stackoverflow.com/questions/37941039/pyqt-transparent-background-image-partially-black

class Grid_Overlay(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Screenshot'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.grid = "Images/1920x1080_grid.png"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
       # self.setAttribute(QtCore.Qt.WindowStaysOnTopHint, True)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap(self.grid)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
    def set_grid(self, filename):
        self.grid = filename

def overlay(filename):
    app = QApplication([])
    ex = Grid_Overlay()
    ex.set_grid(filename)
    app.exec_()
    app.quit()

def main():
    overlay()
if __name__ == '__main__':
    main()
