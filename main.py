# v1.1
from PyQt5.QtWidgets import QMainWindow,QBoxLayout,QApplication,QAction,QLineEdit,QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl,Qt
from PyQt5 import QtGui

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.show()
        
        self.web = QWebEngineView()
        self.web.load(QUrl('https://search.brave.com/'))
        self.setCentralWidget(self.web)
        
        navigator = QToolBar('Navigator')
        self.addToolBar(navigator)

        home = QAction('Home', self)
        back = QAction('<<',self)
        forward = QAction('>>',self)
        reload = QAction('Reload',self)

        home.setIcon(QtGui.QIcon('assets/home.png'))
        back.setIcon(QtGui.QIcon('assets/back.png'))
        forward.setIcon(QtGui.QIcon('assets/forward.png'))
        reload.setIcon(QtGui.QIcon('assets/reload.png'))

        navigator.addAction(back)
        navigator.addAction(forward)
        navigator.addAction(reload)
        navigator.addAction(home)

        self.web.titleChanged.connect(self.title_update)
        home.triggered.connect(self.action_home)
        back.triggered.connect(self.web.back)
        forward.triggered.connect(self.web.forward)
        reload.triggered.connect(self.web.reload)

    def title_update(self):
        self.setWindowTitle(self.web.page().title())

    def action_home(self):
        self.web.load(QUrl('https://search.brave.com/'))

if __name__ == '__main__':
    import sys
    app = QApplication([])
    app.setApplicationName('Lucid')
    form = App()
    form.setWindowIcon(QtGui.QIcon('Lucid.png'))
    form.setWindowTitle('Lucid Browser')
    sys.exit(app.exec_())
