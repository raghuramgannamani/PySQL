"""
Assign int value to firstNum
Assign int value to secondNum
Assign int value to thirdNum
Print the three numbers
claculate the average of those numbers
"""
def main():
    
    
    # Input
    print("Welcome to our calculator")
    firstNum = int(input("Enter the firstNum value : "))
    secondNum = input("Enter the secondNum value : ")
    thirdNum = int(input("Enter the thirdNum value : "))
    #processing

    average = (firstNum + int(secondNum) + thirdNum)/ 3
    
    # output
    print("You entered")
    print(firstNum)
    print(secondNum)
    print(thirdNum)

    #print("The average is ",average)
    #print("The average is : {0}  for the previous number",average)
    #print("The average is : {0}  for the previous numbers".format(average))
    print("The average is : {0:.2f}  for the previous numbers".format(average))







main()