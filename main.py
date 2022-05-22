# v1
from PyQt5.QtWidgets import QWidget,QBoxLayout,QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import QtGui

class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.web = QWebEngineView()

        self.web.load(QUrl('https://google.com/'))
        self.layout.addWidget(self.web)
        self.setLayout(self.layout)

        self.setWindowTitle('nil')
        self.setWindowIcon(QtGui.QIcon('main.ico'))

app = QApplication([])
form = Main()
form.show()
app.exec_()
