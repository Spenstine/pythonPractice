from protoTime import *

def mult_time(t1, num):
    '''
    t1: time object
    num: any number
    '''
    assert isValidTime(t1), 'invalid time object'
    seconds = t1.time_to_int() * num
    return int_to_time(seconds)

def get_pace(t1, num):
    '''
    t1: finish time
    num: distance in miles
    output: pace in terms of time per mile
    '''
    return mult_time(t1, 1/num)

time = Time()
time.hour = 10
time.minute = 0
time.seconds = 0
print(get_pace(time, 5))