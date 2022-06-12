from PyQt6 import QtWidgets, uic

from HIMSBookingSystem.Model.course import Course

class CoursesGUI(QtWidgets.QWidget):
    def __init__(self):
        super(CoursesGUI, self).__init__()
        uic.loadUi("View/Courses.ui", self)

        self.show()