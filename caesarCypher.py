def cypher(word, num):
    for letter in word:
        if letter.isalpha():
            new_letter = rotator(letter, num)
            print(chr(new_letter), end = "")
        else:
            print(letter, end="")
    print("")

def rotator(letter, num):
    ascii_a = ord("a")
    ascii_A = ord("A")
    if letter.islower():
        newAscii = (ord(letter) - ascii_a + num) % 26 + ascii_a
    elif letter.isupper():
        newAscii = (ord(letter) - ascii_A + num) % 26 + ascii_A
    else:
        newAscii = letter
    return newAscii

cypher("IBM - 1  jolly    j", -7)