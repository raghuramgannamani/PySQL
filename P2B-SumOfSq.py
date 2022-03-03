
#The sum of all squares between 1 and 200 (inclusive)
#Enter MaxNumber as 200

MaxNumber = int(input("Enter the Maxium Number:"))
def SumOfEvenNumbers(NUM):
    i=0
    for Number in range(1,NUM+1):
        i=i+(Number*Number)
    print(f"The sum of all squares from 1 to {NUM} is: ",(i))
SumOfEvenNumbers(MaxNumber)