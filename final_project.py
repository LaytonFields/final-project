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
walkupdate = 0



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
        global stand_still, walkupdate
        
        if keyboard.d == True:
            stand_still = False
        else:
            stand_still = True
        
        if stand_still == False:
            self.actor.image = doomguy_walk1
            walkupdate += 1
            print(int(walkupdate))
        elif walkupdate >= 1:
            self.actor.image = doomguy_walk2
        else:
            self.actor.image = doomguy_model
            

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
    clock.schedule_interval(DG.DG_Walk_animation, 1.0)


pgzrun.go()
