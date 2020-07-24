from pronounce import read_dictionary
sipe = read_dictionary()

with open("words.txt", "r") as fin:
    wordDict = dict()
    for line in fin:
        words = line.strip().lower()
        wordDict[words] = True


def check_word(word1, word2, homophone):
    if word1 not in homophone or word2 not in homophone:
        return False
    return homophone[word1] == homophone[word2]

def homophone(word, anyDict):
    word1 = word[1:]
    word2 = word[0] + word[2:]
    if word1 not in anyDict or word2 not in anyDict:
        return False
    if check_word(word, word1, sipe) and check_word(word1, word2, sipe):
        print(word, word1, word2)

for word in wordDict:
    homophone(word, wordDict)
