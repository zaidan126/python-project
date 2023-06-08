from turtle import *
import random
color("mediumspringgreen")
colormode(255)
width(3)
speed(10)
anger=random.randint(122,133)
for i in range(100):
    forward(100)
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    color(red,green,blue)
    left(anger)