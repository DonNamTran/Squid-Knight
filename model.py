import pygame, sys, random

class Model:
    viewObject = ""
    
    def __init__(self):
        pass

    #This function assigns our view object storing the screen's values to the variable. 
    def setViewObject(self, viewObj):
        self.viewObject = viewObj
    
    #This fucntion initializes all the objects needed for our game. 
    def initializeObjects(self):
        #RGB color for silver
        self.silver = (192,192,192)
        
        #Creates the rects for the ball, player paddle, and opponent paddle and places them at the middle, left and right side of the screen.
        self.pongball = pygame.Rect(self.viewObject.screen_w/2 - 15, self.viewObject.screen_h/2 - 15, 30, 30)
        self.player = pygame.Rect(self.viewObject.screen_w - 20, self.viewObject.screen_h/2 - 70, 10, 140)
        self.opponent = pygame.Rect(10, self.viewObject.screen_h/2 - 70, 10, 140)

        #Sets the pong ball to move 10 in both Y and X and chooses a random direction using random.choice
        self.pongball_speed_x = 10 * random.choice((1,-1))
        self.pongball_speed_y = 10 * random.choice((1,-1))
    
        #Stores the paddle speed for both player and opponent along with score and if a score was made
        self.player_speed = 0
        self.opponent_speed = 15
        self.player_score = 0
        self.opponent_score = 0
        self.ballScored = False
