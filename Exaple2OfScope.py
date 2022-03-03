def main():
    var1 = 5 # This var1 is a global variable
    if var1 < 10:
        var2 = 3	 # This var2 is still a global variable
# Call the function, passing a value of 11 as the parameter
    someFunction(11)
# var1 and var2 still exist
    print(var1)
    print(var2)
# param1 and var3 do NOT exist anymore -- these lines will give errors
# because these variables are out of scope.
"""
print(param1)
print(var3)

"""

# Define a function with one parameter
def someFunction(param1): #param1 is a local variable
    var3 = 8    # This var3 is a local variable
    print(param1)
    print(var3)
    return 
main()
