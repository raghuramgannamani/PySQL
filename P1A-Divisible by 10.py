#All positive numbers that are divisible by 10 and less than n. For example, if n is 100, print 10 20 30 40 50 60 70 80 90.
#Divisible by 10
n = int(input('please enter a number: ')) #Global
def PrintPositiveNumbers(NUM): #Function Defined
    i = 1
    while i<NUM: #Local 
        if i%10==0:
            print(i)
        i+=1
PrintPositiveNumbers(n) #Function Call

#All positive numbers that are divisible by 5 and less than n. For example, if n is 100.
#Divisible by 5
n = int(input('please enter a number: '))
def PrintPositiveNumbers(NUM):
    i = 1
    while i<NUM:
        if i%5==0:   #Modified Divisible by 5 
            print(i)
        i+=1
PrintPositiveNumbers(n)