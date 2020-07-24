import turtle
length = int(input("length:  "))
sides = int(input("sides:  "))
bob = turtle.Turtle()
def polygon(pointer, length, sides):
    """pointer: turtle object
    length: length of each side of desired polygon
    sides: number of sides of desired polygon
    """ 
    angle = (sides - 2) * 180 / sides
    for _ in range(sides):
        pointer.fd(length)
        pointer.lt(180 - angle)
    turtle.mainloop()

polygon(bob, length, sides)