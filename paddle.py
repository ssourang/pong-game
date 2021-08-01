from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xpos, ypos)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

