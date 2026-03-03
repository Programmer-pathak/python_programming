class student:
    school_name = "ABC School"  # Class variable or class attribute
    student_name="Ashish"
    student_age=20
    student_roll=101

data=student() # Creating an object of the class

data.state="Bihar"  # Instance variable or object attribute

 # Modifying class variable using object / if we modify class variable using object it will create a new instance variable with same name only for that object if not it will refer to class variable

print(data.school_name)  # Accessing class variable using object
print(data.student_name)
data.student_name="Ravi"
print(data.student_name)

print(data.state)  # Accessing instance variable using object
abc=student() # Creating another object of the class
abc.state="UP"
print(abc.state)  # Accessing instance variable using object
print(abc.school_name)  # Accessing class variable using object


class Student:
    def display(self): # Method with self parameter
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Course:", self.course)

# Create object
s1 = Student()

# Assign values manually (no constructor used)
s1.name = "Nishal"
s1.rollno = 1022
s1.course = "MCA"

# Call the method using the object
s1.display()
