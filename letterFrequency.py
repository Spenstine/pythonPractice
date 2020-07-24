def letterFrequency(word):
    letterDict = {}
    letterList = []
    for letter in word.lower():
        letterDict[letter] = letterDict.get(letter, 0) + 1
    letterDictCopy = letterDict.copy()
    while len(letterDictCopy) > 0:
        highest = max(letterDictCopy.values())
        for key in letterDict:
            if letterDict[key] == highest:
                letterList.append((key, letterDictCopy.pop(key)))
    return letterList

print(letterFrequency('spein'))