from turtle import Turtle

BALL_SPEED = 0.02


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.goto(0, -380)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, -380)
        self.x_move *= -1
