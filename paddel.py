from turtle import Turtle


class Paddel(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len= 5, stretch_wid=  1)
        self.color("white")
        self.penup()
        self.goto(x= 0, y=-250)
        
        
    def go_right(self):
        new_x = self.xcor() + 40
        if new_x < 350:
            self.goto(new_x, self.ycor())
        
    def go_left(self):
        new_X = self.xcor() - 40
        if new_X > -350:
            self.goto(new_X, self.ycor())