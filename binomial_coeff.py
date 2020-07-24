d = {}

def binomial_coeff(n, k, d):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """
    if (n, k) in d:
        return d[(n, k)]
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff(n-1, k, d) + binomial_coeff(n-1, k-1, d)
    d[(n, k)] = res
    return res

print(binomial_coeff(5, 4, d))

mylist = [1, 3, 3, 1]
def increment(mylist):
    new = [1] * (len(mylist) + 1)
    for i in range(1, len(mylist)):
        new[i] = mylist[i] + mylist[i - 1]
    return new

def binomial_iter(n, k):
    mylist = [1, 1]
    if n == 0:
        return 1
    if k > n or k < 0:
        return 0
    for _ in range(1, n):
        mylist = increment(mylist)
    return mylist[k]
print(binomial_iter(5, 4))