#The smallest and largest of the inputs

NoOfNumbers=int(input("Enter how many numbers to enter:"))
number = int(input("enter your number: "))
largest = number
Smallest = number

for number in range(NoOfNumbers-1):
    number = int(input("enter your number: "))
    if (number > largest):
        largest = number
    if (number < Smallest):
        Smallest = number
print("the Smallest Number is",Smallest)
print("The Largest Number is",largest)