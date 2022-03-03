#All powers of two less than n. For example, if n is 100, print 1 2 4 8 16 32 64

n = int(input('please enter a number: ')) #Enter n=100
def PrintPowersOfTwo(NUM):
    i = 0
    while i<NUM:
        if 2**i<NUM:
            print(2**i)
        i+=1
PrintPowersOfTwo(n)