from turtle import Turtle

class Brick(Turtle):

    def __init__(self, origin, clr):
        super().__init__()
        self.shape("square")
        self.color(clr)
        self.shapesize(stretch_wid=0.7, stretch_len=2.2)
        self.penup()
        self.setpos(origin)
        self.point = 0
