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


if __name__=="__main__":
    a, b = GeneratePrimesUpTo(2_500_000)
    c, d = IsPrime(435000000000000011)     #Number of secs since the Big Bang   ≃40s to run
    #print_with_changed_separator(a, "\n")
    print(f"En {b} secondes")
    print(c) 
    print(f"En {d} secondes")