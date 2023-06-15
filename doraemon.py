from turtle import *
import time
import random
setup(500,500)
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
colormode(255)
shape("circle")
bgcolor(r,g,b)
def drawround(size,fill):
    pendown()
    if fill:
        begin_fill()
    setheading(180)
    circle(size,360)
    if fill:
        end_fill()
def drawhead():
    color("blue")
    penup()
    goto(0,100)
    drawround(75,True)
    color("white")
    penup()
    goto(0,72)
    drawround(60,True)
def draweyes():
    color("black","white")
    penup()
    goto(-15,80)
    drawround(17,True)
    penup()
    goto(19,80)
    drawround(17,True)
    color("black")
    penup()
    goto(-8,70)
    drawround(6,True)
    penup()
    goto(12,70)
    drawround(6,True)
def drawnose():
    color("red")
    penup()
    goto(0,40)
    drawround(7,True)
def drawmouth():
    color("black")
    penup()
    goto(-30,-20)
    pendown()
    setheading(-27)
    circle(70,55)
    penup()
    goto(0,26)
    pendown()
    goto(0,-25)   
def drawwhisker():
    color("black")
    penup()
    goto(0,5)
    pendown()
    goto(-40,5)
    penup()
    goto(0,5)
    pendown()
    goto(40,5)
    penup()
    goto(-10,15)
    pendown()
    goto(-40,20)
    penup()
    goto(10,15)
    pendown()
    goto(40,20)
    penup()
    goto(-10,-5)
    pendown()
    goto(-40,-10)
    penup()
    goto(10,-5)
    pendown()
    goto(40,-10)
def drawbody():
    color("blue")
    penup()
    goto(0,-45)
    drawround(80,True)
    color("white")
    penup()
    goto(0,-45)
    drawround(70,True)
def drawpocket():
    color("black")
    penup()
    goto(-25,-150)
    pendown()
    setheading(-90)
    circle(25,180)
    goto(-25,-150)
def drawcolar():
    color("red")
    penup()
    goto(40,-55)
    pendown()
    left(90)
    begin_fill()
    forward(80)
    right(90)
    forward(10)
    right(90)
    forward(80)
    right(90)
    forward(10)
    end_fill()
def drawbell():
    color("yellow")
    penup()
    goto(0,-55)
    drawround(8,True)
    color("black")
    penup()
    goto(0,-61)
    drawround(2,True)
def drawfeet():
    color("black","white")
    penup()
    goto(-30,-180)
    drawround(20,True)
    penup()
    goto(30,-180)
    drawround(20,True)
def drawarm():
    color("blue")
    penup()
    begin_fill()
    goto(-60,-90)
    pendown()
    goto(-90,-100)
    goto(-97,-80)
    goto(-50,-65)
    goto(-60,-90)
    end_fill()
    penup()
    begin_fill()
    goto(60,-90)
    pendown()
    goto(90,-100)
    goto(97,-80)
    goto(50,-65)
    goto(60,-90)
    end_fill()
def drawhand():
    penup()
    color("black","white")
    goto(-100,-70)
    drawround(18,True)
    penup()
    color("black","white")
    goto(100,-70)
    drawround(18,True)
drawarm()
drawhand()
drawhead()
draweyes()
drawnose()
drawmouth()
drawwhisker()
drawbody()
drawpocket()
drawcolar()
drawbell()
hideturtle()
drawfeet()
time.sleep(5)