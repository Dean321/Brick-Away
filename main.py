# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:20:01 2022

@author: Dean321
"""
from turtle import *
import random
import time
FONT = ("Courier", 24, "normal")

screen = Screen()
screen.setup(width=500, height=600)

player = Turtle(shape="triangle")
player.color("blue")
player.penup()
player.goto(x = 0, y=-250)
player.left(90)

arr = []
bullets = []
score = 0
cnt = 0
for i in range(-230,230,50):
    for j in range(-50,300,50):
        brick = Turtle("square")
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.color("brown")
        brick.goto(i, j)
        arr.append(brick)
        cnt+=1
print(35,cnt)        

def createBullets():
    bullet = Turtle()
    bullet.penup()
    bullet.shape('circle')
    bullet.color('red')
    bullet.setheading(90)
    bullet.goto(player.position())
    bullets.append(bullet)

def playerLeft():
    player.goto(player.xcor()-5,player.ycor())
  
def playerRight():
    player.goto(player.xcor()+5,player.ycor())
  
screen.listen()
screen.onkey(createBullets, "Up")
screen.onkey(playerLeft, "Left")
screen.onkey(playerRight, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.clear()
    player.write(score, font=FONT, align='left')
    for i in bullets:
        i.forward(10)
    for i in bullets:
        for j in arr:
            if i.distance(j) < 50  and i.isvisible() and j.isvisible():
                j.hideturtle()
                i.hideturtle()
                score+=1
    if score == 70:
        game_is_on = False
       
if game_is_on == False:
    arr = []
    bullets = []
    hideturtle()
    clear()
    write(f"GAME OVER", align="center", font=FONT)
    
 
    
screen.exitonclick()