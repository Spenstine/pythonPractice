def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

#print("ack: ", ack(3, 6))
#highest is (3, 6)

def ackerman_memo(m, n, d):
    if (m,n) in d:
        return d[m,n]
    if m == 0:
        ans = n + 1
        d[0,n] = ans
        return ans 
    if n == 0:
        ans1 = ackerman_memo(m - 1, 1, d)
        d[m,0] = ans1
        return ans1
    ans2 = ackerman_memo(m - 1, ackerman_memo(m, n - 1, d), d)
    d[m,n] = ans2
    return ans2

dictionary = dict()
print("ackerman Memo: ", ackerman_memo(3, 8, dictionary))
print(dictionary)
#highest is (3, 8)