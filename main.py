# import colorgram
from turtle import Turtle, Screen
import turtle
import random
#
# colors = colorgram.extract("super-mario-bros-1985.jpeg", 10)
#
#
# color = colors[0]

colors = [(95, 147, 246), (185, 76, 22), (249, 203, 191), (11, 155, 12), (39, 11, 6), (216, 148, 94),
          (130, 200, 24), (6, 9, 26)]


def next_color():
    return random.choice(colors)


my_turtle = Turtle()
my_screen = Screen()
my_turtle.speed(0)

turtle.colormode(255)
my_turtle.penup()

print(f" Initial turtle position {my_turtle.pos()[0]}, {my_turtle.pos()[1]}")

screen_width_limit = my_screen.window_width() / 2 - 50
screen_height_limit = my_screen.window_height() / 2 - 50
initial_x = my_screen.window_width() / 2 * -1 + 50
initial_y = my_screen.window_height() / 2 * -1 + 50
my_turtle.goto(initial_x, initial_y)
dot_size = 20
dot_distance = 50
line_distance = 50


print(f" screen width and height {my_screen.window_width()} , {my_screen.window_height()}")
print(f" screen width and height limits {screen_width_limit} , {screen_height_limit}")
print(f"Initial X = {initial_x}, initial Y = {initial_y}")
print(f" Dot size set to  {dot_size} , Dot distance set to  {dot_distance}, Line distance {line_distance}")


for i in range(int(initial_y), int(screen_height_limit), line_distance):
    for j in range(int(initial_x), int(screen_width_limit), dot_distance):
        my_turtle.dot(dot_size, next_color())
        my_turtle.forward(dot_distance)
        # print(f"{my_turtle.pos()[0]} and i = {i} and j={j}")

    # y = my_turtle.pos()[1]
    # print(f"Y = {y}")
    my_turtle.goto(initial_x, my_turtle.pos()[1] + line_distance)



my_screen.mainloop()