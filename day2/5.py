import math

def isPrime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    return True

for i in range(101,201):
    if isPrime(i):
        print(i)