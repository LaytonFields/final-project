import pygame, pgzrun, numpy, os

#Setup and Variables--------------------------------------------

#Screen Size
WIDTH = 1500
HEIGHT = 500

#Variables
game_over = False
game_complete = False
START_POS = 250,400

#Actors
Doomguy = Actor("doomguy.png")
Doomguy.pos = START_POS

def draw():
    screen.blit("background.jpg", (0,0))
    Doomguy.draw()

def DG_Walk():
    if keyboard.a and Doomguy.x > 0:
        Doomguy.x -=5
    elif keyboard.d and Doomguy.x < WIDTH:
        Doomguy.x +=5

def update():
#Doomguy movement---------------------------------------------
    DG_Walk()






pgzrun.go()
