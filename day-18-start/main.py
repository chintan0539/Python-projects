from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
direction = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
di=5
timmy.speed("fastest")

while di<360:
    timmy.color(choice(colours))
    timmy.circle(100)
    timmy.setheading(di)
    di+=5















# timmy.speed(8)
# timmy.pensize(10)
#
# for i in range(100):
#     timmy.color(choice(colours))
#     timmy.setheading(choice(direction))
#     timmy.forward(30)
#












# for i in range(3,11):
#     timmy.color(random.choice(colours))
#     for j in range(i):
#         timmy.forward(100)
#         timmy.left(360/i)


# for i in range(0,10):
#     timmy.pendown()
#     timmy.forward(10)
#
#
#     timmy.penup()
#     timmy.forward(10)


# timmy.color("blue")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
#


screen = Screen()
screen.exitonclick()
