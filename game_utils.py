import turtle
import random


def setup_turtle(turtle_game):
    turtle.hideturtle()
    turtle_game.penup()
    turtle_game.color("green")
    turtle_game.shape("turtle")
    turtle_game.turtlesize(3)


def random_turtle_loc(screen, turtle_game):
    turtle_game.hideturtle()
    random_x = random.randrange(-int(screen.window_width() // 3), int(screen.window_width() // 3))
    random_y = random.randrange(-int(screen.window_height() // 3 - 100), int(screen.window_height() // 3 - 100))
    turtle_game.goto(random_x, random_y)
    turtle_game.showturtle()


def time_text_loc(screen, turtle_time, duration=0):
    turtle.tracer(0)
    turtle_time.hideturtle()
    turtle_time.penup()
    turtle_time.goto(-40, int(screen.window_height() // 3 + 70))
    turtle_time.write(f"Time: {duration}", font=("Verdana", 20, "bold"))
    turtle.tracer(1)


def point_text_loc(screen, turtle_point, count=0):
    turtle.tracer(0)
    turtle_point.hideturtle()
    turtle_point.penup()
    turtle_point.goto(-40, int(screen.window_height() // 3 + 40))
    turtle_point.clear()
    turtle_point.write(f"Point: {count}", font=("Verdana", 20, "bold"))
    turtle.tracer(1)


def end_game(turtle_end):
    turtle.tracer(0)
    turtle_end.clear()
    turtle_end.hideturtle()
    turtle_end.penup()
    turtle_end.color("black")
    turtle_end.goto(0, 100)
    turtle_end.write("Game Over", font=("Verdana", 50, "bold"), align="center")
    turtle.tracer(1)
