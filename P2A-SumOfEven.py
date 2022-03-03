#The sum of all Even between 2 and 200 (inclusive)

MaxNumber = int(input("Enter the Maxium Number:"))
# Enter MaxNumber as 200 to see the required output
def SumOfEvenNumbers(NUM):
    i=0
    for Number in range(2,NUM+1,2):
        #Here range(2,NUM+1,2) start stop and step
        i=i+Number
    print(f"The sum of even numbers from 2 to {NUM} is: ",(i))
SumOfEvenNumbers(MaxNumber)


#Sum of Even Numbers 2 to 200 expect 100

MaxNumber = int(input("Enter the Maxium Number:"))
def SumOfEvenNumbers(NUM):
    i=0
    for Number in range(2,NUM+1,2):
        if Number==100:
            continue                 # continue will skip 100 when Number =100 and continues to the next number.
        i=i+Number
    print(f"The sum of even numbers from 2 to {NUM} is: ",(i))
SumOfEvenNumbers(MaxNumber)