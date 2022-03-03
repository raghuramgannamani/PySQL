def main():
    Student = input("Enter Student Name: ")
    Course = input("Enter Course: ")
    Absences = int(input("No Of Absences:"))
    Attendance = int(input("No Of Attendances: "))
    Total = Absences + Attendance
    print("The Student's name is ",Student)
    print("The Course's name is ",Course)
    print(f"Absences: {Absences} Classes")
    print(f"Attendances: {Attendance} Classes")
    print("Attendance percentage:{0:.2f}".format((Attendance/Total)*100))
main()