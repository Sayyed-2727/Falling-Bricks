from turtle import Turtle
import random

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()     
        self.y_move = -10
        self.colors = ["red", "yellow", "green", "orange", "purple"]
        self.shapes = ["turtle", "triangle", "square", "circle"]
        self.reset_position()
           
    def move(self):
        self.goto(self.xcor(), self.ycor() + self.y_move)
        
    def reset_position(self):
        # setting a random location up there in the screen
        random_x = random.randint(-350,350)
        self.goto(random_x,250)
        
        # setting a random shape
        random_shape = random.choice(self.shapes)
        self.shape(random_shape)
        
        # setting a random color
        if random_shape == "turtle" and random.randint(1,10) == 1:
            self.color("white")
        else:
            random_color = random.choice(self.colors)
            self.color(random_color)
        
        random_size = random.uniform(0.5,2)
        self.shapesize(stretch_len= random_size, stretch_wid= random_size)
        
