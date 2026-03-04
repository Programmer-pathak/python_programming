class student:
    school_name = "ABC School" 
    student_name="Ashish"
    student_age=20
    student_roll=101

    def __init__(self): # this constructor will not work as expected because we use another constructor below
        print("This is constructor") 

    def __init__(self, name, age, roll):
        self.student_name = name
        self.student_age = age
        self.student_roll = roll


    def display_info(self):
        print(f"School Name: {self.school_name}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Age: {self.student_age}")
        print(f"Student Roll Number: {self.student_roll}")

    @staticmethod
    def greet():
        print("Hello, my name is ")


print(student.school_name)  # Accessing class variable using class name
data=student("rohit",22,102) 

data.display_info()

