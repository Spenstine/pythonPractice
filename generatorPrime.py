def genPrimes():
    prevList = [2]
    yield prevList[0]
    next = 2
    while True:
        while any(next % item == 0 for item in prevList):
            next += 1
        prevList.append(next)
        yield next
        next += 1