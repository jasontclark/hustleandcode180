#!/usr/bin/env python
""" line.py - chapter 18 exerxicse 2 """
class Point(object):
    def __init__(self, x, y):
        self.point = (x,y)

    def __str__(self):
        return 'x: ' + str(self.point[0]) + ' y: ' + str(self.point[1])

    def set_location(self, x, y):
        self.point = (x,y)

class Line(object):
      def __init__(self, p1, p2):
          self.point1 = p1
          self.point2 = p2

      def __str__(self):
          return 'Point 1: ' + str(self.point1) + '\n' + \
                 'Point 2: ' + str(self.point2)

p1 = Point(1,2)
print p1
p1.set_location(10,20)
print p1
p2 = Point(8,9)
line1 = Line(p1,p2)
print(line1)
p2.set_location(12, 22)
print line1
