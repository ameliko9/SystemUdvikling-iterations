#import sys
#from PyQt5.uic import loadUi
#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
#import sqlite3

import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QMainWindow


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("../View/Logind.ui", self)

        self.show()


#class Kurser(QMainWindow):
   # def __init__(self):
       # super(Kurser, self).__init__()
        #uic.loadUi("../ui/kurser.ui", self)


#class LoginScreen(QMainWindow):
 #   def __init__(self):
  #      super(LoginScreen, self).__init__()
   #     loadUi("../ui/Logind.ui", self)

app = QApplication(sys.argv)
login = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
app.exec()
# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")