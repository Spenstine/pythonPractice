def contains_all_letters(w1, w2):
    for letter in w2: 
        if letter not in w1:
            return False
    return True

def contains_all(w1, w2):
    return all(letter in w1 for letter in w2)

def contains_all_set(w1, w2):
    return len(set(w2) - set(w1)) == 0

def avoids_set(w1, w2):
    return len(set(w1) - set(w2)) == len(set(w1))

'''
print(contains_all_letters('spenc9er', 'abcdefghijlkmnopqrstuvwxyz'))
print(contains_all('spencer', 'abcdefghijlkmnopqrstuvwxyz'))
print(contains_all_set('abcdefghijlkmnopqrstuvw3xyz', 'abcdefghijklmnopqrs08tuvwxyz'))
'''
print(avoids_set('spencer', 'wsxyz'))
