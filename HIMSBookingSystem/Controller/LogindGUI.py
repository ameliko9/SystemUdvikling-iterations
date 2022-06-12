from PyQt6 import QtWidgets, uic

class LoginScreenGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginScreenGUI, self).__init__()
        uic.loadUi("View/Logind.ui", self)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.logind.clicked.connect(self.logind_function)

    def logind_function(self):
        username = self.usernameField.text()
        password = self.passwordField.text()
        if len(username) == 0 or len(password) == 0:
            print("Please fill out all fields")
        elif (username == "ameliko" and password == "qwerty"):
            print("Login successful")
            # gå til næste vindue eller ui
        print(username, "----", password)


