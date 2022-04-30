from ast import walk
import pygame, pgzrun, numpy, os

START_POS = 250,400
doomguy_model = "doomguy.png"
bullet = "bullet.png"

#Screen Size
WIDTH = 1500
dsasdHEIGHT = 500

#Animation frames
doomguy_walk1 = "doomguy_walk1.png"
doomguy_walk2 = "doomguy_walk2.png"
doomguy_walk3 = "doomguy_walk3.png"
doomguy_walk4 = "doomguy_walk4.png"
stand_still = True
walk1 = False
walk2 = False
walk3 = False
walk4 = False


#Doomguy ---------------------------------------------
class Doomguy():
   
    def DG_walk(self):
        global walk1
        if keyboard.a and self.actor.x > 0:
            self.actor.x -=5
            
        elif keyboard.d and self.actor.x < WIDTH:
            self.actor.x +=5
            walk1 = True

    def __init__(self):
        self.actor = Actor(doomguy_model)
        self.actor.pos = (START_POS)

        self.bullet = Actor(bullet)
        self.bullet.pos = (START_POS)

    def DG_Walk_animation(self):
        global walk1, walk2, walk3, walk4, stand_still
        walkupdate = 0

        if keyboard.d == True:
            stand_still = False
        
        if stand_still == False and walkupdate == 0:
            self.actor.image = doomguy_walk1
            walkupdate += 1
        elif stand_still == False and walkupdate == 1:
            self.actor.image = doomguy_walk2
            walkupdate += 1
        elif stand_still == False and walkupdate == 2:
            self.actor.image = doomguy_walk3
            walkupdate += 1
        elif stand_still == False and walkupdate == 3:
            self.actor.image = doomguy_walk4
            walkupdate += 1   
        else:
            self.actor.image = doomguy_model
            stand_still = True
            

    def shoot(self):
        if keyboard.q:
            self.bullet.draw

#Setup and Variables--------------------------------------------


#Variables
game_over = False
game_complete = False
DG = Doomguy()
num_of_updates = 0


def draw():
    screen.blit("background.jpg", (0,0))
    DG.actor.draw()

def update():
    global num_of_updates
    DG.DG_walk()
    DG.shoot()

    if num_of_updates == 10:
        DG.DG_Walk_animation()
        num_of_updates = 0
    else:
        num_of_updates += 1

pgzrun.go()
