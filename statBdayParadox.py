import random

members = int(input("Number of people involved: "))
def bdayParadox(members):
    birthdayLists = []

    for i in range(members):
        bday = random.randint(1, 365)
        birthdayLists.append(bday)

    birthdayLists.sort()
    for i in range(len(birthdayLists) - 1):
        if birthdayLists[i] == birthdayLists[i + 1]:
            return True
    return False

totalNum = 1000
counter = 0
for i in range(totalNum):
    if bdayParadox(members):
        counter += 1

print("probability: ", counter/totalNum)