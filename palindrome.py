'''
a palindrome is a word that
can be spelt from left to right or
right to left and still maintain its spelling
'''

def palindrome(word):
    word = str(word).lower()
    first = word[0]
    last = word[-1]

    if first == last:
        if len(word) > 2:
            word = word[1:-1]
            return palindrome(word)
        else:
            return True
    return False

print(palindrome(' '))