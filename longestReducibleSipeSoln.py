def get_children(word, dictionary):
    word_list = list(word)
    wordList = []
    for i in range(len(word)):
        word_list_copy = word_list[:]
        del(word_list_copy[i])
        newWord = "".join(word_list_copy)
        if newWord in dictionary:
            wordList.append(newWord)
    return wordList

def is_reducible(word, dictionary):
    children = get_children(word, dictionary)
    if len(children) >= 1:
        return True
    else:
        return False

def reducible(word, dictionary, wordDict):
    if word.lower() in wordDict:
        return True
    elif is_reducible(word, dictionary):
        children = get_children(word, dictionary)
        for child in children:
            return reducible(child, dictionary, wordDict)
    else:
        return False

def init(list):
    wordDict = {'i':'i', 'a':'a'}
    for word in list:
        if reducible(word, list, wordDict):
            wordDict[word] = word
    vals = wordDict.values()
    highest = 0
    sipeList = []
    for ele in vals:
        if len(ele) > highest:
            highest = len(ele)
    for keys in wordDict:
        if len(wordDict[keys]) == highest or len(wordDict[keys]) == highest - 1:
            sipeList.append(keys)
    return sipeList

with open("words.txt", 'r') as fin:
    wordList= {}
    for line in fin:
        words = line.strip().lower()
        wordList.setdefault(words, []).append(words)

sipe = ['spencer','a' ,'sipe', 'sip', 'ip', 'i', 'spence', 'ipe', 'sie']
finalWord = init(wordList)
print(finalWord)
