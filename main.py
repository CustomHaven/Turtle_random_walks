from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)

########### Challenge - Random Turtle Walk ########

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)


random_angle = [0, 90, 180, 270]

tim.shape("turtle")
tim.speed("fastest")
tim.pensize(15)

for _ in range(200):
  tim.fd(30)
  tim.color(random_color())
  tim.setheading(random.choice(random_angle))

screen = Screen()
screen.exitonclick()