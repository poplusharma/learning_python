from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("lightblue")
        self.shapesize(stretch_wid=0.7, stretch_len=5)
        self.penup()
        self.setpos((0, -400))

    def go_left(self):
        if self.xcor() > -300:
            new_x = self.xcor() - 40
            self.goto(x=new_x, y=self.ycor())
        else:
            pass

    def go_right(self):
        if self.xcor() < 300:
            new_x = self.xcor() + 40
            self.goto(x=new_x, y=self.ycor())
        else:
            pass

    def reset_position(self):
        self.setpos((0, -400))