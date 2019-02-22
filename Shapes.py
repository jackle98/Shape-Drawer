from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint

class Shape(object):
    def __init__(self, xcor, ycor, length, color):
        self.length = length
        self.xcor = xcor
        self.ycor = ycor
        self.color = color

class Rectangle(Shape):
    def __init__(self, xcor, ycor, length, width, color):
        super().__init__(xcor, ycor, length, color)
        self.width = width

    def draw(self, qp):
        qp.setBrush(self.color)
        qp.drawRect(self.xcor, self.ycor, self.length, self.width)


class Square(Rectangle):
    def __init__(self, xcor, ycor, length, color):
        super().__init__(xcor, ycor, length, length, color)

class Ellipse(Shape):
    def __init__(self, xcor, ycor, length, width, color):
        super().__init__(xcor, ycor, length, color)
        self.width = width

    def draw(self, qp):
        qp.setBrush(self.color)
        qp.drawEllipse(self.xcor, self.ycor, self.length, self.width)


class Circle(Ellipse):
    def __init__(self, xcor, ycor, length, color):
        super().__init__(xcor, ycor, length, length, color)

class Triangle(Shape):
    def __init__(self, xcor, ycor, length, color, orientation):
        super().__init__(xcor, ycor, length, color)
        self.orientation = orientation

    def draw(self, qp):
        qp.setBrush(self.color)
        if self.orientation == 1:
            qp.drawPolygon(QPoint(self.xcor, self.ycor), QPoint(self.xcor + self.length, self.ycor + self.length), QPoint(self.xcor + self.length, self.ycor - self.length))
        if self.orientation == 2:
            qp.drawPolygon(QPoint(self.xcor, self.ycor), QPoint(self.xcor - self.length, self.ycor + self.length), QPoint(self.xcor - self.length, self.ycor - self.length))
        if self.orientation == 3:
            qp.drawPolygon(QPoint(self.xcor, self.ycor), QPoint(self.xcor + self.length, self.ycor - self.length), QPoint(self.xcor - self.length, self.ycor - self.length))
        if self.orientation == 4:
            qp.drawPolygon(QPoint(self.xcor, self.ycor), QPoint(self.xcor - self.length, self.ycor + self.length), QPoint(self.xcor + self.length, self.ycor + self.length))

class HourGlass(Shape):
    def __init__(self, xcor, ycor, length, color):
        super().__init__(xcor, ycor, length, color)

    def draw(self, qp):
        qp.setBrush(self.color)
        qp.drawPolygon(QPoint(self.xcor, self.ycor), QPoint(self.xcor - self.length, self.ycor - self.length), QPoint(self.xcor + self.length, self.ycor - self.length), QPoint(self.xcor, self.ycor - (self.length * 2)))

class Diamond(Shape):
    def __init__(self, xcor, ycor, length, color):
        super().__init__(xcor, ycor, length, color)

    def draw(self, qp):
        qp.setBrush(self.color)
        qp.drawPolygon(QPoint(self.xcor, self.ycor), QPoint(self.xcor + self.length, self.ycor - self.length), QPoint(self.xcor, self.ycor - (self.length * 2)) ,QPoint(self.xcor - self.length, self.ycor - self.length))
