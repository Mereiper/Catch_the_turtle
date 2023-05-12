import turtle

def setup_turtle(turtle_game):
    turtle.hideturtle()
    turtle_game.penup()
    turtle_game.color("green")
    turtle_game.shape("turtle")
    turtle_game.turtlesize(3)
    turtle_game.left(90)