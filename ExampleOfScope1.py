varOne=100 # This is a Global variable

def printValues():
    varTwo=500
    varThree=20
    print(varTwo," ",varThree) #Local variables
    print(varOne) # is a GLOBAAL variable
    result = varOne + varTwo
    print(result)
    print(varFour)

varFour = 12 # GLOBAL variable
#print(varOne)
# print(varTwo) Is not going to print the variable varTwo(because it is a local var in that function). 
printValues() # Calling the function
