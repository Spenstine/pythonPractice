#! /usr/bin/python
def estimate_pi(): 
    import math
    n = 0
    total = 0
    summation = (2**1.5 / 9801)

    def term(k):
        return (math.factorial(4 * k) * (1103 + 26390 * k))/(math.factorial(k)**4 * 396**(4*k))

    while summation >= 10**(-15):
        summation *= term(n)
        total += summation
        n += 1

    return total
print(1/estimate_pi())