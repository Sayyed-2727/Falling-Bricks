from turtle import Turtle, Screen
from paddel import Paddel
from bricks import Bricks
from score import Score
import random
import time

#Screen adjustment

Window = Screen()
Window.bgcolor("black")
Window.setup(width= 800, height= 600)
Window.title("FALLING BRICKS")
Window.tracer(0)



#recall paddel object

paddel = Paddel()
bricks = Bricks()
score  = Score()


# Screen controling
Window.listen()
Window.onkeypress(paddel.go_right,"Right")
Window.onkeypress(paddel.go_left, "Left")

# Main loop of the game
game_on = True
default_sleep = 0.1
while game_on:
    Window.update()
    time.sleep(default_sleep)
    bricks.move()
    
    # shapes score when bouncing with paddel
    if bricks.distance(paddel)   <=50 and bricks.ycor() <= -230:
        shape_type  = bricks.shape()
        shape_color = bricks.color()[0]
        
        if shape_type == "turtle":
          if shape_color == "white":
            game_on = False
            score.game_over()
          else:
            points = 5
            score.increase_score(points)
        elif shape_type == "circle":
          points = 1
          score.increase_score(points)
        elif shape_type == "square":
          points = 2
          score.increase_score(points)
        elif shape_type == "triangle":
          score.reset_score()
          default_sleep = 0.1
          
        #reset the falling shape
        bricks.reset_position()
        default_sleep *= 0.9
        
    # when bricks misses
    if bricks.ycor() < -300:
      # reset the bricks without affecting the results
      bricks.reset_position()
        
Window.exitonclick()