with open("sipeWords.txt") as fin:
    wordList = []
    for line in fin:
        for word in line.split():
            newWord = word.strip().lower()
            wordList.append(newWord)

print(wordList)