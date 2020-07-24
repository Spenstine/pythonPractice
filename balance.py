balance = 999999
annualInterestRate = 0.2


def initialize(f, bal, rate):
    from numpy import arange
    s_list = list(arange(round(bal/12), round((bal * (1 + rate)**12) /12), 0.2))
    f(bal, rate, s_list)

def return_balance(bal, rate, pay, month):
    remain = round((1 + rate/12) * (bal - pay), 2)
    month += 1
    if month != 12:
        return return_balance(remain, rate, pay, month)
    else:
        return remain

def return_lowest(bal, rate, s_list):
    ind = int(len(s_list)/2)
    pay = s_list[ind]
    month = 0
    mybalance = return_balance(bal, rate, pay, month)
    if len(s_list) == 1 or balance == 0:
        print("Lowest Payment: ", round(pay, 2))
    elif mybalance > 0:
        return return_lowest(bal, rate, s_list[ind:])
    elif mybalance < 0:
        return return_lowest(bal, rate, s_list[:ind])

initialize(return_lowest, balance, annualInterestRate)