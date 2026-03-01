#.Employee Salary Calculator
#Write a Python program to calculate the net salary of an employee after adding HRA (House Rent Allowance) and deducting tax.

def calculate_net_salary():
  basic_salary=float(input("Enter basic salary amount: "))
  hra=float(input("Enter HRA amount: "))
  deduction=float(input("Enter tax deduction amount: "))
  net_salary=(basic_salary+hra)-deduction
  return net_salary

print("Actual salary is:-", calculate_net_salary())