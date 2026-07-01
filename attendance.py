#Employee Attendance Tracker
#Write a Python program to record employee attendance and calculate the attendance percentage for each employee.

def attendance():
    month=input("Enter the month: ")
    if month.lower() in ["january", "march", "may", "july", "august", "october", "december"]:
        days=31
    elif month.lower() =="february":
        days=28
    elif month.lower() in ["april", "june", "september", "november"]:
        days=30
    else:
        print("Invalid month name")
        exit()

    attendance_list=[]

    for i in range(1,days+1):
        status=input(f"Enter attendance for day {i} (P/A): ")
        attendance_list.append(status.upper())

    present=attendance_list.count("P")
    attendance_percentage=f"{(present/days)*100:.2f}"
    return attendance_percentage


print(f"Attendance Percentage is :- {attendance()}%")