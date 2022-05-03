import pygame, pgzrun, numpy, os

START_POS = 250,400
doomguy_model = "doomguy_r.png"
bullet = "bullet.png"

#Screen Size
WIDTH = 1500
HEIGHT = 500

#Animation frames
doomguy_walk1L = "doomguy_walk1l.png"
doomguy_walk1R = "doomguy_walk1r.png"
stand_still = True
walkupdate = 0
left = False
right = False



#Doomguy ---------------------------------------------
class Doomguy():

    def __init__(self):
        self.actor = Actor(doomguy_model)
        self.actor.pos = (START_POS)

        self.bullet = Actor(bullet)
        

    def update(self):
        global stand_still, walkupdate, left, right

    #walk--------------------------------------------------------
        if keyboard.a and self.actor.x > 0:
            self.actor.x -=5
            left = True
            right = False
            stand_still = False
            
        elif keyboard.d and self.actor.x < WIDTH:
            self.actor.x +=5
            left = False
            right = True
            stand_still = False
        
    #animation------------------------------------------------
        
        if stand_still == False and right == True and left == False:
            self.actor.image = doomguy_walk1R
            stand_still = True
        elif stand_still == False and left == True and right == False:
            self.actor.image = doomguy_walk1L
            stand_still = True
        elif left == True and stand_still == True:
            self.actor.image = 'doomguy_l.png'
            left = False
        elif right == True and stand_still == True:
            self.actor.image = 'doomguy_r.png'
            right = False

    #Shoot---------------------------------------------------------
        if keyboard.q:
           self.actor.image = 'doomguy_shoot.png'
           self.bullet.draw()

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
    DG.update()

pgzrun.go()
