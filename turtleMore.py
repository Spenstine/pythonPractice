import turtle
bob = turtle.Turtle()
def polygon(pointer, length, sides, loop):
    """pointer: turtle object
    length: length of each side of desired polygon
    sides: number of sides of desired polygon
    """ 
    loop = int(sides/(360/loop))
    angle = (sides - 2) * 180 / sides
    for _ in range(loop):
        pointer.fd(length)
        pointer.lt(180 - angle)
    turtle.mainloop()


def circle(pointer, radius, arc):
    length = 1
    sides = int(2*3.14159562*radius/length)
    polygon(pointer, length, sides, arc)

#polygon(bob, 100, 4, 360)
circle(bob, 300, 90)