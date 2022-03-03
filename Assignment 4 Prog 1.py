NumOfDays = 5 #Global Variable
def Program(Days): #Function Program and Days Local Variable
    Hours=[] #Empty List
    for i in range (Days):
        HoursWorked = int(input("Enter Hours Worked on Day {0}:".format(i+1)))
        Hours.append(HoursWorked)
    print("---------------------------------------------")
    #Using Max Statement for Most Hours Worked
    print("The Most Hours Worked was on:")
    for i in range (Days):
        if Hours[i]==max(Hours):
            print("Day {0} when you worked".format(i+1), max(Hours),"hours")
    print("---------------------------------------------")
    #Using Sum Calculates the total of List
    print("The total number of hours worked was: ",sum(Hours))
    #Sum/Len gives Average of List
    print("The average number of hours worked each day was: ",(sum(Hours))/len(Hours))
    print("---------------------------------------------")
    #Less than 7
    print("Days you slacked off (i.e worked less than 7 hours):")
    for i in range(len(Hours)):
        if Hours[i]<7:
            print("Day {0}:".format(i+1),Hours[i],"Hours")
Program(NumOfDays) #Function Call

