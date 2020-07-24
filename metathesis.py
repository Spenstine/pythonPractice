def metathesis(anylist):
    """
    output: list of metatheses in the input sequence
    """
    for word in anylist:
        mylist = list(word)
        for letter in word:
            for i in range(len(word)):
                letterList = mylist[:]
                letterList[i], letterList[letterList.index(letter)] = letterList[letterList.index(letter)], letterList[i]
                newWord = "".join(letterList)
                if newWord in anylist and newWord != word:
                    print(word , newWord)

sipe = ['conserve', 'spcner', 'sipe', 'sepi', 'converse']
metathesis(sipe)
"""
wordList = []
with open("words.txt", "r") as fin:
    for line in fin:
        word = line.strip().lower()
        wordList.append(word)      

metathesis(wordList)
"""