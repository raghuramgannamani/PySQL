
# Program for manipulating Strings

newString = input("Enter your statement : ")
print("You Entered : ",newString)
# Change to upper case string
print(newString.upper())
#newString = newString.upper()
#print(newString)

# Different kinds of functions
print(newString.lower())
print("OUR THIRD WEEK : ","OUR THIRD WEEK".capitalize())
print("our third week : ","OUR THIRD WEEK".title())

print("the number of i's is : ", newString.count('i'))
print("Your string is changed to : ",newString.replace("Yousef","David"))

# Dealing with boolean functions (Commands)
print("Is it alphabatic statement ?","4567 Leeds Street".isalpha())
print("Is it alphabatic statement ?","LeedsStreet".isalpha())
print("Is it alphabatic statement ?","Leeds Street".isalpha())
print("Is it alphanumeric statement ?","4567 Leeds Street".isalnum())
print("Is it alphanumeric statement ?","4567LeedsStreet".isalnum())
print("123".isnumeric())
print("12.56".isnumeric())







