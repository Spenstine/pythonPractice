from anagramAndBingo import anagram, get_dict
import shelve

wordDict = get_dict()
sipe = anagram(wordDict, 0, 0)
spencer = shelve.open('sipeAnagram', 'c')
for word, wordList in sipe.items():
    spencer[word] = wordList
spencer.close()

with shelve.open('sipeAnagram') as spencer:
    print(spencer['eintu'])

print(sipe['eintu'])