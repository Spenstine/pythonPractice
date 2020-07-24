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
    

def drawRect(pointer, rect):
    pointer.pu()
    pointer.goto(rect.corner.x, rect.corner.y)
    pointer.setheading(0)
    pointer.pd()
    for _ in range(2):
        pointer.fd(rect.width)
        pointer.lt(90)
        pointer.fd(rect.height)
        pointer.lt(90)
    pointer.pu()
    pointer.goto(0, 0)
    pointer.setheading(0)
    pointer.pd()


def drawCircle(pointer, circle):
    pointer.pu()
    pointer.goto(circle.center.x, circle.center.y)
    pointer.setheading(0)
    pointer.pd()
    pointer.rt(90)
    pointer.fd(circle.radius)
    pointer.lt(90)
    length = 1
    arc = 360
    sides = int(2*3.14159562*circle.radius/length)
    polygon(pointer, length, sides, arc)


class circle:
    '''
    center: point
    radius: lenth
    '''

class point:
    '''
    x: x-coord
    y: y-coord
    '''

class rectangle:
    '''
    corner: point of left bottom corner
    height: height of rectangle
    width: width of rectangle
    '''

def showPoint(point):
    print(f'(%d, %d)' %(point.x, point.y))

def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** 0.5

def pointInCircle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rectInCircle(rect, circle):
    leftUCorner = point(); rightUCorner = point(); rightLCorner = point()
    leftUCorner.y = rect.corner.y + rect.height
    leftUCorner.x = rect.corner.x

    rightUCorner.x = rect.corner.x + rect.width
    rightUCorner.y = rect.corner.y + rect.height

    rightLCorner.x = rect.corner.x + rect.width
    rightLCorner.y = rect.corner.y

    if pointInCircle(circle, rightLCorner):
        return pointInCircle(circle, leftUCorner)
    return False

def rectCircleOverlap(rect, circle):
    rightUCorner = point()
    rightUCorner.y = rect.corner.y + rect.height
    rightUCorner.x = rect.corner.x + rect.width
    for _ in range(rect.height):
        if pointInCircle(circle, rect.corner) or pointInCircle(circle, rightUCorner):
            return True
        rect.corner.y += 1
        rightUCorner.y -= 1 
    for _ in range(rect.width):
        if pointInCircle(circle, rect.corner) or pointInCircle(circle, rightUCorner):
            return True
        rect.corner.x += 1
        rightUCorner.x -= 1
    return False

def visualize(pointer, rect, circle):
    drawRect(pointer, rect)
    drawCircle(pointer, circle)
    turtle.mainloop()



mycircle = circle()
mycircle.center = point()
mycircle.center.x = 150
mycircle.center.y = 100
mycircle.radius = 75

mypoint = point()
mypoint.x = 0
mypoint.y = 8

myrectangle = rectangle()
myrectangle.corner = point()
myrectangle.corner.x = 0
myrectangle.corner.y = 0
myrectangle.height = 200
myrectangle.width = 100

#print(distance(mycircle.center, mypoint))
#print(mycircle.radius)
#print(pointInCircle(mycircle, mypoint))
print(rectCircleOverlap(myrectangle, mycircle))
visualize(bob, myrectangle, mycircle)