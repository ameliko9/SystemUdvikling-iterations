
from PyQt6 import QtWidgets, uic

from Controller.NewEmployeeGUI import NewEmployeeGUI
from Controller.MainWindowDescriptionGUI import MainWindowDescriptionGUI
from Controller.SearchEmployeeGUI import SearchEmployeeGUI


class MainWindowGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindowGUI, self).__init__()
        uic.loadUi('View/MainWindow.ui', self)

        # Keep the space in the GUI when a widget is hidden, so that the window doesn't
        # get garbled

        not_resize = self.stackedWidget.sizePolicy()
        not_resize.setRetainSizeWhenHidden(True)
        self.stackedWidget.setSizePolicy(not_resize)

        # instantiate the widgets for adding and searching employees
        self.new_emp_gui = NewEmployeeGUI()
        self.search_emp_gui = SearchEmployeeGUI()

        # instantiate a widget for "default" window
        self.main_description_gui = MainWindowDescriptionGUI()

        # Now add the defined widgets to the stackedWidget
        self.stackedWidget.addWidget(self.main_description_gui)
        self.stackedWidget.addWidget(self.new_emp_gui)
        self.stackedWidget.addWidget(self.search_emp_gui)

        # Menubar actions
        self.actionAdd_Employee.triggered.connect(self.start_add_employee)
        self.actionSearch_Employee.triggered.connect(self.start_search_employee)

        # combobox actions
        self.comboBox.activated.connect(self.activated)
        self.stackedWidget.setCurrentIndex(0)
        self.show()


    def activated(self, index):
        pass