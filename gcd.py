'''
gcd(x, y)
rercusive gcd(y, x%y)
if gcd(ans, 0) , then 
ans == gcd(x, y)
'''

def gcd(m, n):
    if n == 0:
        return m
    else:
        remainder = m % n
        return gcd(n, remainder)

print(gcd(gcd(128, 3), gcd(8, 16)))