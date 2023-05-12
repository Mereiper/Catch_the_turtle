import turtle
import game_utils

count = 0
duration = 10

screen = turtle.Screen()
screen.title("Catch the turtle!")
screen.bgcolor("light blue")

turtle_game = turtle.Turtle()
turtle_time = turtle.Turtle()
turtle_point = turtle.Turtle()
turtle_point.hideturtle()

game_utils.setup_turtle(turtle_game=turtle_game)


def turtle_timer():
    if duration > 0:
        game_utils.random_turtle_loc(screen=screen, turtle_game=turtle_game)
        screen.ontimer(turtle_timer, t=500)


def game_timer():
    global duration
    if duration > 0:
        duration -= 1
        turtle_time.clear()
        game_utils.time_text_loc(screen=screen, turtle_time=turtle_time, duration=duration)
        turtle_game.onclick(turtle_count)
        screen.ontimer(game_timer, t=1000)
    else:
        game_utils.end_game(turtle_end=turtle_game)
        turtle_game.hideturtle()


def turtle_count(x, y):
    turtle_point.clear()
    global count
    count += 1
    game_utils.point_text_loc(screen=screen, turtle_point=turtle_point, count=count)


turtle_timer()
game_timer()

turtle.mainloop()
