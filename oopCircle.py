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
myrectangle.height = 10
myrectangle.width = 5

#print(distance(mycircle.center, mypoint))
#print(mycircle.radius)
#print(pointInCircle(mycircle, mypoint))
print(rectCircleOverlap(myrectangle, mycircle))