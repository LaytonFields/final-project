import pygame, pgzrun, numpy, os

START_POS = 250,400
doomguy_model = "doomguy.png"
bullet = "bullet.png"

#Screen Size
WIDTH = 1500
HEIGHT = 500

#Doomguy ---------------------------------------------
class Doomguy():

    def DG_Walk_animation(self):        
        if keyboard.d:
            doomguy_model == ("doomguy_walk1.png")

    def DG_walk(self):
        if keyboard.a and self.actor.x > 0:
            self.actor.x -=5
        elif keyboard.d and self.actor.x < WIDTH:
            self.actor.x +=5

    def __init__(self):
        self.actor = Actor(doomguy_model)
        self.actor.pos = (START_POS)

        self.bullet = Actor(bullet)
        self.bullet.pos = (START_POS)

    def shoot(self):
        if keyboard.q:
            self.bullet.draw

#Setup and Variables--------------------------------------------


#Variables
game_over = False
game_complete = False
DG = Doomguy()


def draw():
    screen.blit("background.jpg", (0,0))
    DG.actor.draw()

def update():
    DG.DG_walk()
    DG.DG_Walk_animation()
    DG.shoot()


pgzrun.go()
