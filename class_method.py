class Student:
    school_name = "ABC School"  # Class Attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name  # Yeh poori class ka school name badal dega

# Bina object banaye bhi call kar sakte hain
Student.change_school("XYZ High School")

s1 = Student("Rohit")
s2 = Student("Vikas")

print(s1.school_name)  # Output: XYZ High School
print(s2.school_name)  # Output: XYZ High School