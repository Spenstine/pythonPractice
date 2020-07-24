class Time():
    '''
    represent time of day
    attributes: hour, minute, seconds
    '''
    def __init__(self, hour = 0, minute = 0, seconds = 0):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    def __str__(self):
        '''
        show time in hr:min:sec
        '''
        h = self.hour 
        m = self.minute
        s = self.seconds
        return f'%.2d:%.2d:%.2d' %(h, m, s)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increament_pure(other)
            
    def __radd__(self, other):
        return self.__add__(other)

    def time_to_int(self):
        '''
        output: integer representing total number of time in seconds
        '''
        seconds = self.hour * 3600 + self.minute * 60 + self.seconds
        return seconds

    def increament_pure(self, secs):
        '''
        this is a pure method!
        secs: integer representing number of seconds
        output: new time object returned after secs added to self
        '''
        secs += self.time_to_int()
        return int_to_time(secs)

    def is_after(self, other):
        '''
        returns true if self is cronologically after other
        '''
        total1 = self.time_to_int()
        total2 = other.time_to_int()
        return total1 > total2

    def add_time(self, other):
        '''
        output: new time object from adding self and other
        '''
        new = self.time_to_int() + other.time_to_int()
        return int_to_time(new)

def isValidTime(t1):
    '''
    t1: time object
    output: bool
    '''
    if t1.hour > 23 or t1.minute > 59 or t1.seconds > 59:
        return False
    if t1.hour < 0 or t1.minute < 0 or t1.seconds < 0:
        return False    
    return True

def int_to_time(num):
    '''
    num: any integer
    output: time object
    '''
    new = Time()
    new.minute, new.seconds = divmod(num, 60)
    new.hour, new.minute = divmod(new.minute, 60)
    day, new.hour = divmod(new.hour, 24)
    if day >= 1:
        print("It's a new day", day, 'day(s) have passed')
    return new

def increament_mod(t, secs):
    '''
    this is a modifier and not a pure function!

    t: time object
    secs: integer representing number of seconds
    result: t is modified by adding secs to it
    '''
    assert isValidTime(t), 'wrong time input!'
    t.minute, t.seconds = divmod(t.minute * 60 + t.seconds + secs, 60)
    t.hour, t.minute = divmod(t.hour * 60 + t.minute, 60)
    day, t.hour = divmod(t.hour, 24)
    if day >= 1:
        print("It's a new day: ", day, 'day has passed')

mytime = Time(2, 9, 46)
anotherTime = Time(9, 29, 54)

if __name__ == '__main__':
    #showTime(mytime)
    #showTime(anotherTime)
    #print(is_after(mytime, anotherTime))
    #showTime(add_time(mytime, anotherTime))
    print(mytime)
    #increament_mod(mytime, 3600 * 22)
    mytime = mytime.increament_pure(3600*22)
    print(mytime)
    print(Time.is_after(anotherTime, mytime))