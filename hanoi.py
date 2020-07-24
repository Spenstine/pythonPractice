"""this is a simulation that solves
the hanoi tower problem
"""

def move(fr, to):
    """sole purpose in life is to 
    print the moves to make
    """

    print("From: ", fr, " to: ", to)

def step(n, fr, to, spare):
    """the essence is to move the top bulk to spare
    then move the bottom-most disk to target. 
    This is done recursively.
    n : number of disks
    fr: origin
    to: target
    spare: free tower
    output: steps to solve the problem
    """
    if n <= 1:
        move(fr, to)
    else:
        #recursively move the top bulk to spare
        step(n-1, fr, spare, to)
        #move the bottom-most disk to target and print move
        move(fr, to)
        #recursively move the bulk from spare to target
        step(n-1, spare, to, fr)

step(4, 'red', 'green', 'orange')#from red, target is green and spare is orange
