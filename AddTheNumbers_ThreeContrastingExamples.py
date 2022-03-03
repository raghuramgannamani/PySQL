#The purpose of each sample function is to take two numbers and add them together.
#This file will demonstrate three different ways to write functions
#   - Using no parameters and no return value
#   - Using parameters, but no return value
#   - Using both parameters and a return value <--- BEST METHOD

#Use inputs to get two numbers from the user
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

#METHOD ONE - No Parameters, No Return Value
#This method works, but restricts your function to only being used from within THIS program.
#Since it references variables (firstNumber and secondNumber) that are declared in this program, but
#outside the function, it cannot be called except from within this program.

def AddTwoNumbers_1():
    answer = firstNumber + secondNumber #<-- Math is done inside function, but uses variables that are declared outside
    print("The first method's result is:", answer)    #<-- Printing is also done from inside the function

AddTwoNumbers_1() #<-- Call the function

##################################################################################
#METHOD TWO - Using parameters, but no return value
#This method also works, but removes the function's dependency on externally-declared variables by using parameters.
#When the function is called, a value for each defined parameter MUST be included in the function call, appearing as
#values inside the parenthesis of the function call. The values are passed into the function's parameter variables
#(ie. num1 gets assigned the value from firstNumber, num2 gets the value from secondNumber). While inside the function,
#the values are used to do the math. Please note that num1 and firstNumber are two COMPLETELY SEPARATE variables, they
#are not related in any way. The only commonality is that the value is passed from one to the next, when the function
#is called.
#This version of the function is better, but still prints from inside the function, which isn't the best method, since
#it makes the function dependant on a console-based platform (since the print() command is used).

def AddTwoNumbers_2(num1, num2):
    answer = num1 + num2 #<-- Math is done inside function, using the two parameter variables (num1 and num2)
    print("The second method uses parameters, and it's result is:", answer)

AddTwoNumbers_2(firstNumber, secondNumber) #<-- Call the function, and pass it the user-input values as parameters

##################################################################################
#METHOD THREE - Using both parameters and a return value
#This works yet again, but this version of the function is completely self-sufficient, in that it uses no outside
#variables and doesn't have to worry about outputting the answer itself. It's sole job is now to just take two numbers
#(the values are received via the function's parameters), add them together, then return the answer to the function call.
#This allows the programmer the flexibility to collect the numbers to be added in any way they wish, and to output in
#any manner, without involving the function. This "trims down" the function, so it's only purpose is to receive two
#numbers, add them together, and inform us of the sum.
#Two things to note when the return keyword is used:
#   - The returned value gets returned back to the line of code that called it. In effect, it replaces the function call.
#   - Using the return keyword exits the function, so any code written inside the function AFTER the return line will
#     never be executed.

def AddTwoNumbers_3(num1, num2):
    answer = num1 + num2 #<-- Math is done inside function, using the two parameter variables (num1 and num2)
    return answer

result = AddTwoNumbers_3(firstNumber, secondNumber) #<-- Call the function, and pass it the user-input values as parameters
print("The third method uses parameters and a return value. It's result is:", result)