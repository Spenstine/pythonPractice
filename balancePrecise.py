balance = 320000
annualInterestRate = 0.2


def initialize(f, bal, rate):
    start = bal/12
    end = (bal * (1 + rate)**12) /12
    f(bal, rate, start, end)

def return_balance(bal, rate, pay, month):
    remain = (1 + rate/12) * (bal - pay)
    month += 1
    if month != 12:
        return return_balance(remain, rate, pay, month)
    else:
        return remain

def return_lowest(bal, rate, start, end):
    mid = (start + end)/2
    pay = mid
    month = 0
    mybalance = return_balance(bal, rate, pay, month)
    if 0.0 <= mybalance <= 0.1:
        print("Lowest Payment: ", round(mid, 2))
    elif mybalance < 0:
        end = mid
        return return_lowest(bal, rate, start, end)
    elif mybalance > 0:
        start = mid
        return return_lowest(bal, rate, start, end)

initialize(return_lowest, balance, annualInterestRate)  