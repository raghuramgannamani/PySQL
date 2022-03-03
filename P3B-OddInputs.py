
# The number of ODD inputs.

NoOfNumbers=int(input("How many inputs you want:"))
Numbers=0
OddCount=0

for i in range(NoOfNumbers):
    Numbers=int(input("Enter your Number: "))
    if Numbers%2!=0:
        OddCount=OddCount+1
print("No of Odd inputs are",OddCount)