Number = int(input("How many number of students:"))
def Final(Exam):
    Student=[]
    Python=[]
    DataBase=[]
    for i in range (Exam):
        Students = input("Enter student's Name {0} \t\t:".format(i+1))
        Prog = int(input("Enter {0}'s mark in Python\t:".format(Students)))
        DB = int(input("Enter {0} mark in DB \t\t:".format(Students)))
        Student.append(Students)
        Python.append(Prog)
        DataBase.append(DB)
        print("----------------------------------------------")
        print("St Name     Python Course     DataBase Course")
        print("--------    --------------    ---------------")
    for i in range (len(Student)):
        print(Student[i],"          ",Python[i],"              ",DataBase[i])
    print("----------------------------------------------")
    print("The total mark of python Course is:",(sum(Python)),"and DataBase Course is:",(sum(DataBase)))
    print("The average of python Course is:",(sum(Python)/len(Python)),"and DataBase Course is:",(sum(DataBase)/len(DataBase)))
    print("-------------------The First Report -----------------------")
    print("Students' Marks less than Average in DataBase Course")

    print("-------------------The Second Report -----------------------")
    print("Students' Marks who were supported in Python courses")

    print("-------------------The Third Report -----------------------")
    print("Students' names before sorted in ascending order")
    print(Student)
    print("Students' names after sorting in ascending order")
    print("")
Final(Number)