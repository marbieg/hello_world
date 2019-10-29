class Student:
    # __init__ is like a constructor in C++ --> when we are creating a student, we are actually calling this function
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
