def is_anagram(firstWord, secondWord):
    if firstWord.lower() == secondWord.lower():
        #print(firstWord, "is", secondWord)
        return False
    return sorted(firstWord) == sorted(secondWord)

"""
print(is_anagram('fried', 'fired'))
print(is_anagram('listen', 'silent'))
print(is_anagram('ochieng', 'spencer'))
print(is_anagram('ochieng', 'ochieng'))
"""