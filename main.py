from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QLabel_alterada(QLabel):
    clicked = pyqtSignal()

    def __init(self, parent):
        QLabel.__init__(self, QMouseEvent)

    def mousePressEvent(self, ev):
        self.clicked.emit()


now = datetime.now()  # current date and time
state = 0

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.datetime.raise_()
        self.datetime.setText(now.strftime("%m/%d/%Y, %H:%M:%S"))
        self.show()
        self.bg.clicked.connect(self.dosomestuff)

    def dosomestuff(self):
        global state
        print("click")
        uic.loadUi('detect.ui', self)
        self.datetime.raise_()
        self.datetime.setText(now.strftime("%m/%d/%Y, %H:%M:%S"))
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
