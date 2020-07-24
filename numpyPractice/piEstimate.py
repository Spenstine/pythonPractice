'''
pi = 2 *= (4 * i^2)/(4 * i^2 - 1) for i in range(1, infinity)
'''

def piEstimate(n):
    '''
    n: highest value in range; for accuracy use a
       very large n.
       but for ease, use n btwn 1000 and 1000000
    output: estimation of pi based on n
    '''
    pi = 2
    for i in range(1, n):
        pi *= 4 * i ** 2/(4 * i ** 2 - 1)
    return pi

print(piEstimate(1000000))    