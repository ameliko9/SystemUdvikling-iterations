from PyQt6 import QtWidgets, uic

class EmployeeLoginGUI(QtWidgets.QWidget):
    def __init__(self):
        super(EmployeeLoginGUI, self).__init__()
        uic.loadUi("View/Employee_login.ui", self)

        self.show()