import time

def in_bisect(sorted_list, targetWord):
    mid = int(len(sorted_list)/2)
    if len(sorted_list) < 1:
        return False
    if targetWord == sorted_list[mid]:
        return True
    elif targetWord < sorted_list[mid]:
        return in_bisect(sorted_list[:mid], targetWord)
    elif targetWord > sorted_list[mid]:
        return in_bisect(sorted_list[mid+1:], targetWord)

def sortSipe(anyList):
    anyList.sort()
    return

def initialize_search(f1, anylist, word):
    word = word.lower()
    anylist = [wordInList.lower() for wordInList in anylist]
    sortSipe(anylist)
    print(f1(anylist, word))

def find_reverse_linearSearch(anylist, target):
    for word in anylist:
        if target == word[::-1]:
            return True
    return False

def find_reverse_binarySearch(anylist, target):
    searchWord = target[::-1]
    return in_bisect(anylist, searchWord)

def interlock(anylist):
    anylist.sort()
    for word in anylist:
        first = word[::2]
        second = word[1::2]
        if in_bisect(anylist, first) and in_bisect(anylist, second):
            print(first, 'and', second, 'interlock to form', word)

wordList = []
with open("words.txt", 'r') as fin:
    for lines in fin:
        word = lines.strip()
        wordList.append(word)

"""
uncommment the line below the lines below
run the code to utilize the search functionality
"""
#uTarget = input("Which word are you searching for?  ")
#initialize_search(in_bisect, wordList, uTarget)

#uTarget = input("Print the target word: ")
"""
uncommment the line below the lines below
run the code to utilize the reverse funtion with linear search
"""
#startLinear = time.time()
#print(find_reverse_linearSearch(wordList, uTarget))
#durationLinear = time.time() - startLinear

#startBinary = time.time()
#print(find_reverse_binarySearch(wordList, uTarget))
#dutationBinary = time.time() - startBinary
#print("Linear search took: ", durationLinear, " seconds.")
#print("Binary search took: ", dutationBinary, " seconds.")

#interlock(wordList)