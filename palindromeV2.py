def palindrome(word):
    if str(word).lower() == str(word)[::-1].lower() : return True
    return False

print(palindrome(2112))