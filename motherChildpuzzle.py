"""
This is the mother-child puzzle,
where child's age is reverse of mothers age
"""

def reverse_int(x):
    """
    x: any value
    output: reverse of x
    """
    y = int(str(x).zfill(2)[::-1])
    return y

def occurance(max_num):
    """
    max_num: max number of occurance of reverse ages
    output: first time when reverse occured
    """
    for i in range(1, 10):
        counter = 0
        #addition is by 11 to ensure reverse holds
        addition = 11
        x = i
        y = reverse_int(x)
        while x < 99:
            if x == reverse_int(y):
                counter += 1
            x += addition
            y += addition
        if counter == max_num:
            return i

first_time = occurance(8)

#nth time would be (n-1) * 11 + first_time
n = 8
age = first_time + (n-1) * 11
print(f"at {n}th time, my age will be {age}")