#Employee Attendance Tracker
#Write a Python program to record employee attendance and calculate the attendance percentage for each employee.

def attendance():
    month=input("Enter the month: ")
    if month.lower() ==["january" or "march" or "may" or "july" or "august" or "october" or "december"]:
        days=31
    elif month =="february":
        days=28
    elif month.lower() ==["april" or "june" or "september" or "november"]:
        days=30
    else:
        return "Invalid month name"
    
    list=[]

    for i in range(1,days+1):
        status=input(f"Enter attendance for day {i} (P/A): ")
        list.append(status.upper())

    present=list.count("P")
    attendance_percentage=(present/days)*100
    return attendance_percentage


print(f"Attendance Percentage: {attendance()}%")