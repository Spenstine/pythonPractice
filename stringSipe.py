import string
digits = string.digits
inTab = string.ascii_uppercase
outTab = string.ascii_lowercase
delTable = string.punctuation + string.whitespace + digits
transTable = str.maketrans(inTab, outTab, delTable)

#with open("sipeWords.txt") as fin:
with open('Buffallo_bill_entrapped.txt', 'r') as fin:
    wordList = {}
    for line in fin:
        for word in line.split():
            newWord = word.translate(transTable)
            wordList[newWord] = wordList.get(newWord, 0) + 1

#print(wordList)
vals = list(wordList.values())
keys = list(wordList.keys())
#print("total words: ",sum(vals))
#print('specific words: ', len(keys))

'''
frequentWords = {}
highest = max(vals)
while len(frequentWords) < 20:
    for key in keys:
        if wordList[key] == highest:
            frequentWords[key] = highest
    highest -= 1

print("20 most frequent words are: ")
print(frequentWords)
'''

with open('words.txt', 'r') as fin:
    wordDict = {}
    for line in fin:
        word = line.strip().lower()
        wordDict[word] = wordDict.get(word, 0) + 1

print('america in wordDict: ' , 'america' in wordDict)

'''spellings = []
for word in wordList:
    if word not in wordDict:
        spellings.append(word)

print("numbers of misspelled words: ", len(spellings))
print(spellings)'''

print(set(wordList) - set(wordDict))