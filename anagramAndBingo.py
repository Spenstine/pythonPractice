def get_dict(filename = "words.txt"):
    with open(filename, "r") as fin:
        wordDict = {}
        for line in fin:
            word = line.strip().lower()
            word2 = "".join(sorted(word)) 
            wordDict.setdefault(word2, []).append(word)
    return wordDict

def anagram(anydict, n, max):
    """
    n: number of letter of words
    max: maximum number of anagram output
    outup: list of anagrams
    """
    Vals = list(anydict.values())
    highest = 0
    for item in Vals:
        if len(item) > highest:
            highest = len(item)
    while highest >= max:
        for word in anydict:
            if len(word) == n and len(anydict[word]) == highest:
                print(word, ":",  wordDict[word])
        highest -= 1
    return anydict

if __name__ == '__main__':
    wordDict = get_dict()
    sipe = anagram(wordDict, 8, 7)
    print(sipe)