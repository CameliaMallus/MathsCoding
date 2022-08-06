from math import sqrt, floor
from time import time

def IsPrime(n):
    """Checks if n is prime
    Returns True or False"""
    IsPrime = True
    start = time()
    for j in  range (2, floor(sqrt(n))+1):
        if n%j==0:
            IsPrime = False
            break
    total_time = time()-start
    return IsPrime, total_time

def GeneratePrimesUpTo(n):
    """Generates all prime numbers from 2 to n
    Minimum Value n = 3

    n = 1,000   ≃0.0010s
    n = 10,000   ≃0.016s
    n = 100,000   ≃0.38s
    n = 1,000,000   ≃9.8s
    n = 10,000,000   ≃255s"""
    start = time()
    primes = [2, 3]
    for i in range(4, n+1):
        """local_primes = []
        for k in primes:
            if k>sqrt(i):
                break
            else:
                local_primes.append(k)
        local_primes.append(floor(sqrt(i)))""" #practically unefficient
        for j in  range (2, floor(sqrt(i))+1): #local_primes:
            if i%j==0:
                break
            if j==floor(sqrt(i)):
                primes.append(i)
                break
    total_time = time()-start
    return primes, total_time

def print_with_changed_separator(list, separator):
    for i in list:
        print(i, end=separator)

def GCD(x, y):
    """Returns the Greatest Common Divisor of x and y"""
    for i in reversed(range(1, 1+min(x,y))): #reverse range order
        if x%i==0 and y%i==0:
            return i

if __name__=="__main__":
    a, b = GeneratePrimesUpTo(100_000)
    c, d = IsPrime(100_493)    #IsPrime(435_000_000_000_000_011)     Number of secs since the Big Bang   ≃40s to run
    print_with_changed_separator(a, "\n")
    print(f"In {b} seconds")
    print(c) 
    print(f"In {d} seconds")
    print(GCD(150, 200))