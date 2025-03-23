from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(x=0, y=250)
        self.write(arg=(f"Score: {self.score}"), align="center", font=("courier", 20, "normal"))
        
    def increase_score(self,points):
        self.score += points
        self.update_score()
        
    def reset_score(self):
        self.score = 0 
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg=("Game Over"), align="center", font=("courier", 20, "normal"))
        


