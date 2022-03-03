#All positive numbers that are divisible by 5 and less than n. For example, if n is 100.

n = int(input('please enter a number: '))
def PrintPositiveNumbers(NUM):
    i = 1
    while i<NUM:
        if i%5==0:
            print(i)
        i+=1
PrintPositiveNumbers(n)