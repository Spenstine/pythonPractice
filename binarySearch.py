def isIn(char, aStr):
    aStr = sorted(aStr)
    newStr = str()
    for letter in aStr:
        newStr += letter
    
    mid = int(len(newStr)/2)
    if len(newStr) <= 1:
        return newStr == char
    else:
        if newStr[mid] == char:
            return True
        elif newStr[mid] > char:
            return isIn(char, newStr[:mid])
        else:
            return isIn(char, newStr[mid + 1:])

print(isIn('a', 'ak'))