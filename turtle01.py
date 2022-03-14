import turtle
import random

#03
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Kolmnurk")
k1 = turtle.Turtle()
for a in range(3):
    k1.forward(100)
    k1.rt(120)
    
turtle.exitonclick(3)
'''
#02
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Harjutus02")
angle = 0
k1 = turtle.Turtle()
for i in range(6):
    k1.rt(angle)
    k1.forward(100)
    angle=144

turtle.exitonclick(6)



#01

aken = turtle.Screen()
aken.setup(300,300)
aken.title("Harjutus01")

colors = ('red','blue','orange','green')
turn = 0
spikes = 8
size = 100
turn += 360/spikes
def okkad():
    k1 = turtle.Turtle()
    k1.speed(10)
    k1.color(random.choice(colors))
    k1.left(turn)
    k1.forward(size)
turtle.exitonclick
'''
