Number = int(input("How many number of students:"))
Student=[]
Python=[]
DataBase=[]
for i in range (Number):
    Students = input("Enter student's Name {0} \t\t:".format(i+1))
    Prog = int(input("Enter {0}'s mark in Python\t:".format(Students)))
    DB = int(input("Enter {0} mark in DB \t\t:".format(Students)))
    Student.append(Students)
    Python.append(Prog)
    DataBase.append(DB)
#Begin Function By defining Fuction Program
def Program(StudentCall,PythonCall,DataCall):
    print("----------------------------------------------")
    print("St Name     Python Course     DataBase Course")
    print("--------    --------------    ---------------")
    #printing Lists in the required format
    for i in range (len(StudentCall)):
        print(StudentCall[i],"          ",PythonCall[i],"              ",DataCall[i])
    print("----------------------------------------------")
    #sum gives total list value
    print("The total mark of python Course is:",(sum(PythonCall)),"and DataBase Course is:",(sum(DataCall)))
    #sum/len gives average of list value
    print("The average of python Course is:",(sum(PythonCall)/len(PythonCall)),"and DataBase Course is:",(sum(DataCall)/len(DataCall)))
    print("-------------------The First Report -----------------------")
    #DataBase Course less than average marks
    print("Students' Marks less than Average in DB Course")
    for i in range (len(DataCall)):
        if DataCall[i]<(sum(DataCall)/len(DataCall)):
            print(StudentCall[i],"got",DataCall[i],"for Database Course")
    print("-------------------The Second Report -----------------------")
    #Python Marks added 5
    print("Students' Marks who were supported in Python courses")
    for i in range (len(PythonCall)):
        if PythonCall[i]<60:
            PythonCall[i]=PythonCall[i]+5
            print(StudentCall[i]," got ",PythonCall[i]," in Python")
    print("-------------------The Third Report -----------------------")
    #Enhanced Part of the program for the assignment.
    for i in range (len(DataCall)):
        if DataCall[i]<60:
            print(StudentCall[i]," failed database course by scoring just ",DataCall[i])
    #Using Sort
    print("Students' names before sorted in ascending order")
    print(StudentCall)
    print("Students' names after sorting in ascending order")
    StudentCall.sort()
    print(StudentCall)
Program(Student,Python,DataBase) #Function Call
