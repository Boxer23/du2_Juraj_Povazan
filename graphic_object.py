import turtle
from abc import ABC, abstractmethod

def calcbox(points):
    xmin = float("inf")
    for p in points:
        if p.x < xmin:
            xmin = p.x

    xmax = float("-inf")
    for p in points:
        if p.x > xmax:
            xmax = p.x

    ymin = float("inf")
    for p in points:
        if p.y < ymin:
            ymin = p.y

    ymax = float("-inf")
    for p in points:
        if p.y > ymax:
            ymax = p.y

    ll = Point(xmin, ymin)
    ur = Point(xmax, ymax)
    return Rectangle(ll, ur)

class GraphicObject(ABC):
    @abstractmethod
    def draw(self):
        pass

class Point(GraphicObject):
    def __init__(self, ax = 0, ay = 0, color = "black"):
        self.x = ax
        self.y = ay
        self.color = color


    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.dot(3)

    def __str__(self):
        return "Point ({},{})".format(self.x, self.y)

class Polyline (GraphicObject):
    def __init__(self, points, color = "black"):
        self.pts = points
        self.color = color
        self.bbox = calcbox(self.pts)

    def draw(self):
        turtle.goto(self.pts[0].x, self.pts[0].y)
        turtle.pencolor(self.color)
        turtle.pendown()
        for p in self.pts:
            turtle.goto(p.x, p.y)
        turtle.penup()

    def __str__(self):
        return "Polyline ({},{})".format(self.pts)

class Polygon (GraphicObject):
    def __init__(self, points):
        self.pts = points

    def draw(self):
        turtle.goto(self.pts[0].x, self.pts[0].y)
        turtle.pendown()
        for p in self.pts:
            turtle.goto(p.x, p.y)
        turtle.goto(self.pts[0].x, self.pts[0].y)
        turtle.penup()

    def __str__(self):
        return "Polygon({},{})".format(self.pts)

class Rectangle(Polygon):
    def __init__(self,ll,ur):
        lr = Point(ur.x,ll.y)
        ul = Point(ll.x,ur.y)
        pts = [ll, lr, ur, ul]
        self.pts = [ll,lr,ur,ul]

    def __str__(self):
        return "Rectangle ({},{})".format(self.pts[0],self.pts[2])

class LineSegment(Polyline):
    def __init__(self,p1,p2, color = "black"):
        self.pts = [p1,p2]
        super().__init__(self.pts, color)

    def __str__(self):
        return "Line segment ({} - {})".format(self.pts[0],self.pts[1])

