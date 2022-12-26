import turtle as t
import random

tim = t.Turtle()
tim.speed(20)
tim.pensize(5)
t.colormode(255)
# colors = ["deep sky blue", "lawn green", "dark orange"]
directions = [0, 90, 270, 180]

def randomcolours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
    
for i in range(200):
    tim.forward(10)
    tim.color(randomcolours())
    tim.setheading(random.choice(directions))
    