import datetime
'''
siku_ya_leo is swahili word for today
'''
siku_ya_leo = datetime.datetime.today()


def get_bdays():
    '''
    constructor of a dictionary that maps birthday to list of people
    output: dict => bday -> []
    '''
    n = int(input("how many birthdays do you want? "))
    bdayDict = {}
    for _ in range(n):
        #strptime(parse) method can do time passing in an easier way
        #it works like strftime(format)
        name = input('Whose birthday are you putting? ')
        bday = input("When were you born:  YYYY-MM-DD ")
        #bday = datetime.datetime.strptime(bday, '%Y-%m-%d')
        #M -> min, m->month, d->day, y->year(two digit), Y->year(four digit)
        bday = bday.split('-')
        bday = datetime.datetime(int(bday[0]), int(bday[1]), int(bday[2]))
        bdayDict.setdefault(bday, []).append(name)
    return bdayDict


def countdown(bday):
    '''
    input: datetime object representing a birthday of person
    output: number of days, hours, minutes, seconds left to day of birthday party
    '''
    diff = siku_ya_leo.toordinal() - bday.toordinal()
    print('age: ', diff//365, 'years and', diff%365, 'days old')
    bash = bday.replace(year = siku_ya_leo.year)
    print('birthday: ', bash.strftime("%A %d %B"))
    print('today: ', siku_ya_leo.strftime("%A %d %B"))
    if bash > siku_ya_leo:
        countdown_ya_bash = bash - siku_ya_leo
    else:
        countdown_ya_bash = bash.replace(year = bash.year + 1) - siku_ya_leo
    return countdown_ya_bash

def rounderDay(bday1, bday2, n):
    '''
    bday1, bday2: datetime objects representing birthday
    n: integer to represent how many times one bday will be older than the other
    output: day when one will be n times older than the other
    '''
    bday1 = bday1.toordinal()
    bday2 = bday2.toordinal()
    if bday1 > bday2:
        old = bday1 - bday2
        diff = bday2
    elif bday1 < bday2:
        old = bday1 - bday1
        diff = bday1
    else:
        print('same birthday!')
        return None
    if n == 1 and bday1 != bday2:
        print("can't have same age!")
        return None
    if n > old:
        print("extremely large number you got there!")
        return None
    daysPassed = int(old/(n - 1))
    return datetime.date.fromordinal(old + diff + daysPassed)

sipe = datetime.datetime(1999, 1, 1)
sip = datetime.datetime(2000, 1, 1)
print(rounderDay(sip, sipe, 365))
#print("countdown: ", countdown(list(get_bdays().keys())[1]))