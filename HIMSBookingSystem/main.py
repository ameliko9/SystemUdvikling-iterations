import sys

from PyQt6 import QtWidgets

from Controller.LogindGUI import LoginScreenGUI


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = LoginScreenGUI()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedWidth(1200)
    widget.setFixedHeight(600)
    widget.show()
    app.exec()