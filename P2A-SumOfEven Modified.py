#program to calculate the sum of all even numbers between 2 and 200 except the number 100
#Enter MaxNumber as 200

MaxNumber = int(input("Enter the Maxium Number:"))
def SumOfEvenNumbers(NUM):
    i=0
    for Number in range(2,NUM+1,2):
        if Number==100:
            continue
        i=i+Number
    print(f"The sum of even numbers from 2 to {NUM} is: ",(i))
SumOfEvenNumbers(MaxNumber)