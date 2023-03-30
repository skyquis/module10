class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_and_major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_and_major_characters.issuperset(lname) and name_and_major_characters.issuperset(fname)):
            raise ValueError
        if not name_and_major_characters.issuperset(major):
            raise ValueError
        if not isinstance(gpa, float) and gpa not in range(0, 3):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

student1=Student('Doe','John','Finance')
print(student1)
student2=Student('Doe','Jane','Business',3.5)
print(student2)