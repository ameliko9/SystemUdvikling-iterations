class Employee:
    def __init__(self, id, firstname, lastname, campus, education):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.campus = campus
        self.education = education

    def get_name(self):
        return self.firstname + " " + self.lastname

    def get_id(self):
        return self.id

    def get_education(self):
        return self.education

    def get_campus(self):
        return self.campus