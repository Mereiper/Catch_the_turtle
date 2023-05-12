import turtle
import random


def setup_turtle(turtle_game):
    turtle.hideturtle()
    turtle_game.penup()
    turtle_game.color("green")
    turtle_game.shape("turtle")
    turtle_game.turtlesize(3)
    turtle_game.left(90)


def random_turtle_loc(screen, turtle_game):
    turtle_game.hideturtle()
    random_x = random.randrange(-int(screen.window_width() // 3), int(screen.window_width() // 3))
    random_y = random.randrange(-int(screen.window_height() // 3 - 100), int(screen.window_height() // 3 - 100))
    turtle_game.goto(random_x, random_y)
    turtle_game.showturtle()


def time_tex_loc(screen, turtle_time, duration=0):
    turtle_time.hideturtle()
    turtle_time.penup()
    turtle_time.goto(-40, int(screen.window_height() // 3 + 70))
    turtle_time.write(f"Time: {duration}", font=("Verdana", 20, "bold"))
