import pygame, sys, random
import view, eventController
class Model:
    viewObject = ""
    
    def __init__(self):
        pass

    #This function assigns our view object storing the screen's values to the variable. 
    def setViewObject(self, viewObj):
        self.viewObject = viewObj
    
    #This fucntion initializes all the objects needed for our game. 
    def initializeObjects(self):
        pass
        
    
class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        img = pygame.image.load("sprites/world_assets/rock_img.png")
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, shift):
        self.rect.y += shift

class TileDanger(pygame.sprite.Sprite):
    HURT = pygame.USEREVENT + 4
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("sprites/world_assets/spike.png")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, shift):
        self.rect.y += shift     
class JumpPowerUp(pygame.sprite.Sprite):
    #This is the event that handles how long the powerup lasts for
    TIME = pygame.USEREVENT + 1
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        img = pygame.image.load("sprites/powerups/jump_boost.png")
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)
    def scroll(self,shift):
        self.rect.y += shift
class GhostPowerUp(pygame.sprite.Sprite):

    TIME = pygame.USEREVENT + 2
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        img = pygame.image.load("sprites/powerups/ghost_powerup.png")
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)
    def scroll(self,shift):
        self.rect.y += shift
class LifePowerUp(pygame.sprite.Sprite):


    TIME = pygame.USEREVENT + 3
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        img = pygame.image.load("sprites/powerups/extra_life.png")
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)
    def scroll(self,shift):
        self.rect.y += shift

class WinPowerUp(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        img = pygame.image.load("sprites/powerups/win.png")
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)
    def scroll(self,shift):
        self.rect.y += shift
class Level():
    currLevel = 1
    actualPlayer = 0
    def __init__(self, level_layout, surface):
        
        self.surface = surface
        self.setup_level(level_layout)
        self.world_shift = 0
        self.beforeSwitch_Y = 0
        self.powerupNum = 0
    
    def setup_level(self, layout):
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * view.View.tile_size
                y = row_index * view.View.tile_size
                if col == 'X':
                    tile = Tile((x,y),view.View.tile_size)
                    self.tiles.add(tile)
                if col == 'D':
                    tileDanger = TileDanger((x,y),view.View.tile_size)
                    self.tiles.add(tileDanger) 
                if col == 'S':
                    player_sprite = Player((x,y),view.View.tile_size)
                    Level.actualPlayer = player_sprite
                    self.player.add(player_sprite)
                if col == 'J':
                    x = col_index * view.View.tile_size +21
                    y = row_index * view.View.tile_size +21
                    powerup = JumpPowerUp((x,y),20)
                    self.powerups.add(powerup)
                if col == 'G':
                    x = col_index * view.View.tile_size +21
                    y = row_index * view.View.tile_size +21
                    powerup = GhostPowerUp((x,y),20)
                    self.powerups.add(powerup)
                if col == 'L':
                    x = col_index * view.View.tile_size +21
                    y = row_index * view.View.tile_size +21
                    powerup = LifePowerUp((x,y),20)
                    self.powerups.add(powerup)
                if col == 'W':
                    x = col_index * view.View.tile_size +21
                    y = row_index * view.View.tile_size +21
                    powerup = WinPowerUp((x,y),20)
                    self.powerups.add(powerup)
                    
    def side_collision(self):
        

        player = self.player.sprite
        player.rect.x += player.direction.x * player.horizontalSpeed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):

                #this checks if the player is touching a "danger tile" 
                if isinstance(sprite, TileDanger) and not player.hurt:
                    player.lives = player.lives - 1
                    player.hurt = True
                    #makes them invulnerable for 3 seconds
                    pygame.time.set_timer(TileDanger.HURT, 3000, 1)
                    hurtSound = pygame.mixer.Sound("Sounds/Danger.mp3")
                    pygame.mixer.Sound.set_volume(hurtSound, 0.05)
                    pygame.mixer.Sound.play(hurtSound)

                #if the player has the ghost powerup enabled. they will be able to clip through
                #the side of the tiles if they are jumping. 
                if player.ghosting:
                    #these if-statements make sure the player does not clip through the side if they are on the ground. 
                    if player.direction.x < 0 and not player.jumping:
                        player.rect.left = sprite.rect.right
                        player.direction.x = 0
                        jumping = False
                    elif player.direction.x > 0 and not player.jumping:
                        player.rect.right = sprite.rect.left
                        player.direction.x = 0
                        jumping = False
                else:
                    #these if-statements are for when the ghost powerup is not enabled.
                    #it will make sure the player never clips through the side. 
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                        player.direction.x = 0
                        jumping = False
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        player.direction.x = 0
                        jumping = False

    def top_collision(self):
        player = self.player.sprite
        player.physics()

        for sprite in self.tiles.sprites():
            
            if sprite.rect.colliderect(player.rect):
                if isinstance(sprite, TileDanger) and not player.hurt:
                    player.lives = player.lives - 1
                    player.hurt = True
                    player.image = pygame.image.load("sprites/player/squid_damaged.png")
                    pygame.time.set_timer(TileDanger.HURT, 3000, 1)
                    hurtSound = pygame.mixer.Sound("Sounds/Danger.mp3")
                    pygame.mixer.Sound.set_volume(hurtSound, 0.12)
                    pygame.mixer.Sound.play(hurtSound)
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jumping = False
                elif player.direction.y < 0 and not player.ghosting :
                    bonksound = pygame.mixer.Sound("Sounds/evenBetterBonk.mp3")
                    pygame.mixer.Sound.set_volume(bonksound, 0.3)
                    pygame.mixer.Sound.play(bonksound)
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
    def powerUp_collision(self):
        
        dict = pygame.sprite.groupcollide(self.player, self.powerups, False, True)
        if dict: 
            #the keys of the dictionary is just a group containing the player character sprite. 
            player = list(dict.keys())
            #the values are a group that contains all the sprites that the first group collides with
            powerup = list(dict.values())
            pickup = pygame.mixer.Sound("Sounds/powerupPickup.mp3")
            pygame.mixer.Sound.set_volume(pickup, 0.3)
            pygame.mixer.Sound.play(pickup)
            #this determines what type of powerup was touched, and applies the appropriate changes. 
            if isinstance(powerup[0][0], JumpPowerUp):
                #This sends an event telling the program to reset the player back to normal after a certain amount of time. 
                pygame.time.set_timer(JumpPowerUp.TIME, 10000, 1)
                player[0].image = pygame.image.load("sprites/player/squid_jumpboost.png")
                player[0].jump_speed = -14
            if isinstance(powerup[0][0], GhostPowerUp):
                #This sends an event telling the program to reset the player back to normal after a certain amount of time. 
                pygame.time.set_timer(GhostPowerUp.TIME, 5000, 1)
                player[0].image = pygame.image.load("sprites/player/squid_ghost.png")
                #player[0].jump_speed = player[0].jump_speed * 1.4
                player[0].ghosting = True
            if isinstance(powerup[0][0], LifePowerUp):
                player[0].image = pygame.image.load("sprites/player/squid_life.png")
                player[0].lives = player[0].lives + 1
                pygame.time.set_timer(LifePowerUp.TIME, 500, 1)
                print(player[0].lives)
            if isinstance(powerup[0][0], WinPowerUp):
                view.View.win(self)
                
    def scroll_y(self):
        #Holds the players positions
        player = self.player.sprite
        powerups = self.powerups.spritedict
        player_y = player.rect.centery
        player_top = player.rect.top
        
        #If the player passes the bottom of the screen, move the screen by the screen_h downward
        if player_y > 640:
            Level.currLevel = Level.currLevel + 1
            self.beforeSwitch_Y = player_y
            self.tiles.update(-view.View.screen_h)
            player.rect.centery = self.beforeSwitch_Y - view.View.screen_h
            
            for pu in powerups.keys():
                pu.scroll(-view.View.screen_h)
          
        #If the player passes the top of the screen, move the screen by the screen_h upward
        if player_top < 0:
            Level.currLevel = Level.currLevel - 1
            self.beforeSwitch_Y = player_top
            self.tiles.update(view.View.screen_h)
            player.rect.top = self.beforeSwitch_Y + view.View.screen_h
            for pu in powerups.keys():
                pu.scroll(view.View.screen_h)
            
    def checkSave(self):
        file1 = open("saves/save.txt", "r+")
        saveState = file1.read()
        if(saveState == "0" and (Level.currLevel == 10)):
            file1.seek(0)
            file1.truncate()
            file1.write("1")
        elif(saveState == "1"):
            if(Level.currLevel > 10):
                file1.seek(0)
                file1.truncate()
                file1.write("0")
            elif(Level.currLevel <= 5):
                file1.seek(0)
                file1.truncate()
                file1.write("2")
        elif(saveState == "2"):
            if(Level.currLevel > 10):
                file1.seek(0)
                file1.truncate()
                file1.write("0")
            elif(Level.currLevel > 5 and Level.currLevel <= 10):
                file1.seek(0)
                file1.truncate()
                file1.write("1")
    
    def run(self):
        self.tiles.draw(self.surface)
        self.powerups.draw(self.surface)
        self.powerUp_collision()
        self.player.update()
        self.top_collision()
        self.side_collision()
        self.scroll_y()
        self.checkSave()
        self.tiles.update(self.world_shift)
        self.player.draw(self.surface)
class Player(pygame.sprite.Sprite, Level):
    
    def __init__(self, pos, size):
        super().__init__()
        
        self.image = pygame.Surface((40,40),size)
        #self.image.fill('grey')
        img = pygame.image.load("sprites/player/squidknight.png")
        self.image = img
        #self.image.load('squidknight.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.lives = 3
        self.direction = pygame.math.Vector2(0,0)
        self.horizontalSpeed = 2
        #Change back to .5
        self.gravity = .5
        self.jump_speed = -10
        self.jumping = False
        self.num = 0
        self.space_start_time = 0
        self.space_hold_time = 0
        self.ghosting = False
        self.hurt = False
    
    def physics(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def changePos(self,pos):
        self.rect.centery = pos  
    def jump(self):
        if self.space_hold_time < 500:
            self.direction.y = self.jump_speed 
        elif self.space_hold_time > 500 and self.space_hold_time < 2000:
            self.direction.y = self.jump_speed*1.5
        else:
            self.direction.y = self.jump_speed*1.75
        sound = pygame.mixer.Sound("Sounds/jump.mp3")
        pygame.mixer.Sound.set_volume(sound, 0.05)
        pygame.mixer.Sound.play(sound)
    def update(self):
        self.rect.x += self.direction.x * self.horizontalSpeed
        eventController.EventController.input(self)
        self.physics()
        
