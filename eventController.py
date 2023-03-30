import pygame, sys, random

class EventController:
    #Variables that keep track of the model and view class. 
    model = ""
    view = ""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    #Controlls all aspects of the player object (Movement, Collision)
    def movePlayer(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #If down arrow key is pressed
            if event.type == pygame.KEYDOWN:
                #if pressed and held then move player object down with a speed of 8
                if event.key == pygame.K_DOWN:
                    self.model.player_speed += 8
                #if released then reset speed back to 0
                if event.key == pygame.K_UP:
                    self.model.player_speed -= 8
            #If up arrow key is pressed
            if event.type == pygame.KEYUP:
                #if pressed and held then move player object down with a speed of 8
                if event.key == pygame.K_DOWN:
                    self.model.player_speed -= 8
                #if released then reset speed back to 0
                if event.key == pygame.K_UP:
                    self.model.player_speed += 8
        self.model.player.y += self.model.player_speed
        #If you move out of bounds then reset position to just on the border
        if self.model.player.top <= 0:
            self.model.player.top = 0
        if self.model.player.bottom >= self.view.screen_h:
            self.model.player.bottom = self.view.screen_h


    #Controlls the opponents paddle aspects (Movement, Collision)
    def moveOpponent(self):
        #If the opponent moves out of bounds then reset position to just on the border
        if self.model.opponent.top <= 0:
            self.model.opponent.top = 0
        if self.model.opponent.bottom >= self.view.screen_h:
            self.model.opponent.bottom = self.view.screen_h

        #Move the opponent up and down based on if the ball is above or below his current pos.
        if self.model.opponent.top < self.model.pongball.y:
            self.model.opponent.top += self.model.opponent_speed
        if self.model.opponent.bottom > self.model.pongball.y:
            self.model.opponent.bottom -= self.model.opponent_speed
    
    #Controlls the balls aspects (Movement, Collision)
    def moveBall(self):
        #Collision with borders
        if(self.model.pongball.top <= 0 or self.model.pongball.bottom >= self.view.screen_h):
            self.model.pongball_speed_y *= -1
        if(self.model.pongball.left <= 0 or self.model.pongball.right >= self.view.screen_w):
            if self.model.pongball.left <= 0:
                self.model.player_score += 1
            if self.model.pongball.right >= self.view.screen_w:
                self.model.opponent_score += 1
            
            #This resets the ball in the center after one side has scored. 
            self.model.pongball.center = (self.view.screen_w/2,self.view.screen_h/2)
            self.model.pongball_speed_x *= random.choice((1,-1))
            self.model.pongball_speed_y *= random.choice((1,-1))
            self.model.ballScored = True
            
        #Colissions with player paddle and opponent paddle
        if(self.model.pongball.colliderect(self.model.player) or self.model.pongball.colliderect(self.model.opponent)):
            self.model.pongball_speed_x *= -1