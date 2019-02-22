import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint
from Shapes import Shape, Rectangle, Square, Ellipse, Circle, Triangle, HourGlass, Diamond

class ShapeDrawer(QWidget):

  def __init__(self):
    super().__init__()
    self.__shapes = list()
    self.setGeometry(50, 50, 500, 500)
    self.setWindowTitle('Shapes')
    self.__clickx = -1
    self.__clicky = -1
    self.__randomLength = 0
    self.__randomWidth = 0
    self.show()


  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    if self.__clickx >= 0 and self.__clicky >= 0:
        for newshape in self.__shapes:
            newshape.draw(qp)
    qp.end()

  def mousePressEvent(self, event):
      self.__clickx = event.x()
      self.__clicky = event.y()
      self.__randomLength = randint(10,100)
      self.__randomWidth = randint(10,100)
      triangle_orientation = randint(1,4)
      colors = [Qt.magenta, Qt.blue, Qt.red, Qt.yellow, Qt.cyan, Qt.green]
      color_choice = colors[randint(0,5)]
      shape_choice = randint(1,7)
      if shape_choice == 1:
         newshape = Rectangle(self.__clickx - (self.__randomLength / 2), self.__clicky - (self.__randomWidth / 2), self.__randomLength, self.__randomWidth, color_choice)
         self.__shapes.append(newshape)
      if shape_choice == 2:
         newshape = Ellipse(self.__clickx - (self.__randomLength / 2), self.__clicky - (self.__randomWidth / 2), self.__randomLength, self.__randomWidth, color_choice)
         self.__shapes.append(newshape)
      if shape_choice == 3:
          newshape = Square(self.__clickx - (self.__randomLength / 2), self.__clicky - (self.__randomLength / 2), self.__randomLength, color_choice)
          self.__shapes.append(newshape)
      if shape_choice == 4:
          newshape = Circle(self.__clickx - (self.__randomLength / 2), self.__clicky - (self.__randomLength / 2), self.__randomLength, color_choice)
          self.__shapes.append(newshape)
      if shape_choice == 5:
          if triangle_orientation == 1:
              newshape = Triangle((self.__clickx - (self.__randomLength / 2)), self.__clicky, self.__randomLength, color_choice, triangle_orientation)
              self.__shapes.append(newshape)
          if triangle_orientation == 2:
              newshape = Triangle((self.__clickx + (self.__randomLength / 2)), self.__clicky, self.__randomLength, color_choice, triangle_orientation)
              self.__shapes.append(newshape)
          if triangle_orientation == 3:
              newshape = Triangle(self.__clickx, self.__clicky + (self.__randomLength / 2), self.__randomLength, color_choice, triangle_orientation)
              self.__shapes.append(newshape)
          if triangle_orientation == 4:
              newshape = Triangle(self.__clickx, self.__clicky - (self.__randomLength / 2), self.__randomLength, color_choice, triangle_orientation)
              self.__shapes.append(newshape)
      if shape_choice == 6:
          newshape = HourGlass(self.__clickx, self.__clicky + self.__randomLength, self.__randomLength, color_choice)
          self.__shapes.append(newshape)
      if shape_choice == 7:
          newshape = Diamond(self.__clickx, self.__clicky + self.__randomLength, self.__randomLength, color_choice)
          self.__shapes.append(newshape)
      self.update()



if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = ShapeDrawer()
  sys.exit(app.exec_())
