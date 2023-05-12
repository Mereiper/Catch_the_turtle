import turtle
import game_utils

screen = turtle.Screen()
screen.title("Catch the turtle!")
screen.bgcolor("light blue")

turtle_game = turtle.Turtle()

game_utils.setup_turtle(turtle_game)

turtle.mainloop()
