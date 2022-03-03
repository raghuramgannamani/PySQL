n = int(input('please enter a number: '))
# set x to 0, so the while loop can stop when 'n' is greater than '0'
x = 0
while n > x:
    if n % 10 == 0:
        print(n)
    n -= 1