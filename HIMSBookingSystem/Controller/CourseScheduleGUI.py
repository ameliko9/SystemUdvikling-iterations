from PyQt6 import QtWidgets, uic

class CourseScheduleGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(CourseScheduleGUI, self).__init__()
        uic.loadUi("../View/course_schedule.ui", self)

        self.show()