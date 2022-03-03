# This program is about CoffeeShop

# Input

# numOfCups = 5
# priceOfAcup = 2.23
# myName = "Yousef"

print("Welcome to our CoffeeSfop")
print("What's your order")
#print("How many number of Cups ? ")

numOfCups = input("How many number of Cups ? ")
print("You ordered ", numOfCups, " Cups")
priceOfAcup = 2.23

# Processing
totalCost = int(numOfCups) * priceOfAcup

# Output

print("The total Cost is : $",totalCost)
print("The total Cost is : $"+str(totalCost)) # Concatenation
print("My name is :"+" Yousef "+ "I am Living in Halifax")
