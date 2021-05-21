
import random
from turtle import Turtle, Screen
cooo = [(246, 242, 234), (240, 242, 247), (239, 246, 241), (248, 241, 244), (198, 164, 118), (144, 79, 56),
          (220, 201, 139), (60, 94, 122), (167, 152, 48), (138, 163, 180), (132, 34, 22), (50, 118, 87), (194, 94, 79),
          (71, 39, 33), (145, 178, 151), (97, 76, 79), (19, 91, 72), (162, 146, 157), (228, 176, 165), (34, 59, 76),
          (146, 20, 24), (58, 43, 45), (86, 148, 129), (23, 85, 89), (41, 65, 88), (10, 70, 60), (177, 202, 183),
          (188, 91, 93), (214, 182, 188), (113, 128, 145)]
screen = Screen()
screen.colormode(255)
t = Turtle()
t.up()
t.speed("fastest")
possi=0

for i in range(10):

    for i in range(10):
        # t.color(random.choice(colour))
        t.dot(20,random.choice(cooo))
        t.fd(50)
    possi+=50
    t.setpos(0,possi)



screen.exitonclick()
