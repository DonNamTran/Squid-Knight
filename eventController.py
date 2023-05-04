import pygame, sys, random
import model
import view
class EventController:
    #Variables that keep track of the model and view class. 
    model = ""
    view = ""
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def input(self):
        font = pygame.font.SysFont(None, 20)
        #player = model.Player()
        player = model.Level.actualPlayer
        if player.lives <= 0:
            
            view.View.lose(self)
            
            #pygame.quit()
            #sys.exit()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    
                sys.exit()

            if event.type == model.JumpPowerUp.TIME:
                player.image = pygame.image.load("sprites/player/squidknight.png")
                player.jump_speed = -10

            if event.type == model.GhostPowerUp.TIME:
                player.image = pygame.image.load("sprites/player/squidknight.png")
                player.ghosting = False
            if event.type == model.TileDanger.HURT:
                player.image = pygame.image.load("sprites/player/squidknight.png")
                player.hurt = False
            if event.type == model.LifePowerUp.TIME:
                player.image = pygame.image.load("sprites/player/squidknight.png")
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    
                    player.space_start_time = pygame.time.get_ticks()
             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.space_hold_time = pygame.time.get_ticks() - player.space_start_time
                    if (not player.jumping):
                        #Set jumping to True
                        player.jumping = True
                        player.jump()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.direction.x = 1
        elif keys[pygame.K_a]:
            player.direction.x = -1
        else:
            player.direction.x = 0
            
