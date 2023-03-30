import pygame, sys

class View:
    #Variables related to the screen's dimensions and attributues.
    screen_w = 1280
    screen_h = 960
    screen = pygame.display.set_mode((screen_w,screen_h))
    pygame.display.set_caption('Pong')
    screenColor = pygame.Color('black')
    
    #Clock variable that manages the FPS of the game. Kept at 60 ticks.
    clock = pygame.time.Clock()

    #model variable.
    model = ""

    def __init__(self, model):
        #Creates the font objects 
        self.score_font = pygame.font.Font('freesansbold.ttf', 28)
        self.score_font.bold = False
        self.model = model
        

    #method that updates all the objects in the screen.
    def updateScreen(self):
        self.screen.fill(self.screenColor)

        #Draws the new positions of the player, opponent, and the pongball. 
        pygame.draw.rect(self.screen, self.model.silver, self.model.player)
        pygame.draw.rect(self.screen, self.model.silver, self.model.opponent)
        pygame.draw.ellipse(self.screen, self.model.silver, self.model.pongball)
        pygame.draw.aaline(self.screen, self.model.silver, (self.screen_w/2,0), (self.screen_w/2,self.screen_h))
        pygame.draw.aaline(self.screen, self.model.silver, (0,self.screen_h/2), (self.screen_w,self.screen_h/2))
        
        #This adds vector movement to the pongball, pongball_speed_x/y are determined in the eventController.
        self.model.pongball.x += self.model.pongball_speed_x
        self.model.pongball.y += self.model.pongball_speed_y

        #renders and displays the current score. 
        self.player_text = self.score_font.render(str(self.model.player_score), True, self.model.silver)
        self.screen.blit(self.player_text, (self.screen_w * 0.75, 0))
        self.opponent_text = self.score_font.render(str(self.model.opponent_score), True, self.model.silver)
        self.screen.blit(self.opponent_text, (self.screen_w * 0.25 , 0))

        #sets the tick-rate of the clock to 60.
        self.clock.tick(60)

        #updates the display
        pygame.display.update()

        #This adds a small delay after the ball is scored to give the user time to react to the new volley being started.
        if self.model.ballScored:
            pygame.time.delay(1000)
            self.model.ballScored = False