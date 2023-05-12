import turtle
import game_utils

screen = turtle.Screen()
screen.title("Catch the turtle!")
screen.bgcolor("light blue")

turtle_game = turtle.Turtle()

game_utils.setup_turtle(turtle_game=turtle_game)


def turtle_timer():
    game_utils.random_turtle_loc(screen, turtle_game)
    screen.ontimer(turtle_timer, t=500)


turtle_timer()

turtle.mainloop()
