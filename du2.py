import json
from abc import ABC, abstractmethod
from graphic_object import Point, Polyline, Polygon, Rectangle
import turtle

def read_json_file(nazov_suboru):
    with open (nazov_suboru, encoding ="utf-8") as f:
        return json.load(f)

class GraphicObject(ABC):
    @abstractmethod
    def draw(self):
        pass

class Point(GraphicObject):
    def __init__(self, ax = 0, ay = 0):
        self.x = ax
        self.y = ay

    def __str__(self):
        return "Point ({},{})".format(self.x, self.y)

    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.dot(3)

class Rectangle(GraphicObject):
    def __init__(self,lr,ul,ll,ur):
        lr = Point(max_x)
        ul = Point(max_y)
        ll = Point(min_x)
        ur = Point(min_y)
        pts = [ll, lr, ur, ul]
        self.pts = [ll,lr,ur,ul]

    def draw(self):
        turtle.goto(lr, ul)
        turtle.dot(3)

    def __str__(self):
        return "Rectangle ({},{})".format(self.pts[0],self.pts[2])

def calcbox(features):
    body_x = []
    body_y = []
    for x_y in features:
        props = x_y["geometry"]
        poloha = props["coordinates"]
        x = poloha[0]
        body_x.append(x)
        l = min(body_x)
        p = max(body_x)
        y = poloha[1]
        body_y.append(y)
        d = min(body_y)
        h = max(body_y)

        min_x = Point(l)
        max_x = Point(p)
        min_y = Point(d)
        max_y = Point(h)
        return Rectangle(min_x, max_x, min_y, max_y)
