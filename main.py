from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit


class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.web = QWebEngineView()
        self.web.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.web)
        self.showMaximized()
        navigationbar = QToolBar()  #Negivation Bar For the Browser
        self.addToolBar(navigationbar)
        backButton =QAction('Back',self)  #Back Button
        backButton.triggered.connect(self.web.back)
        navigationbar.addAction(backButton)
        forwaedButton = QAction('Forward',self) #Forward Button
        forwaedButton.triggered.connect(self.web.forward)
        navigationbar.addAction(forwaedButton)
        reloadButton=QAction('Reload',self)  #Reaload Button
        reloadButton.triggered.connect(self.web.reload)
        navigationbar.addAction(reloadButton)
        homeButton = QAction('Home',self)
        homeButton.triggered.connect(self.negivate_home)
        navigationbar.addAction(homeButton)
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigationbar.addWidget(self.url_bar)
        self.web.urlChanged.connect(self.update_url)


    def negivate_home(self):
        self.web.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app= QApplication(sys.argv)
QApplication.setApplicationName("Web")
win = Window()
app.exec_()