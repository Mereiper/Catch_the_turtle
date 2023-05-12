import turtle
import game_utils

count = 0
duration = 10

screen = turtle.Screen()
screen.title("Catch the turtle!")
screen.bgcolor("light blue")

turtle_game = turtle.Turtle()
turtle_time = turtle.Turtle()

game_utils.setup_turtle(turtle_game=turtle_game)


def turtle_timer():
    if duration > 0:
        game_utils.random_turtle_loc(screen, turtle_game)
        screen.ontimer(turtle_timer, t=500)


def game_timer():
    global duration
    if duration > 0:
        duration -= 1
        turtle_time.clear()
        game_utils.time_tex_loc(screen=screen, turtle_time=turtle_time, duration=duration)
        screen.ontimer(game_timer, 1000)


turtle_timer()
game_timer()

turtle.mainloop()
