import numpy as np

def getPrime(n):
    '''
    n : integer below which all prime numbers are returned
    '''
    isPrime = np.ones((n,), dtype = bool)
    isPrime[:2] = 0
    maxNum = int(np.sqrt(n)) + 1
    for i in range(2, maxNum):
        isPrime[i * i::i] = 0
    return isPrime.nonzero()

print(getPrime(60))