def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        gcd = b
    else:
        gcd = a
    while True:
        if a % gcd == 0 and b % gcd == 0:
            gcd = gcd
            break
        else:
            gcd -= 1
    return gcd

print(gcdIter(121, 77))
