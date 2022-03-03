NUM = int(input("Enter the Value of N: ")) #Global Variable Input
def IntFactorial(N): #Function Defined
    Total = 1
    for i in range(2,N+1):
        Total*=i
    return Total
Total = IntFactorial(NUM) #Function Call
print("The Factorial Value of", NUM, "is:", Total)