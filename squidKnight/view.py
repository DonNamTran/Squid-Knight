import pygame, sys

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
        
class Level():
    currLevel = 1
    print(currLevel)
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
                x = col_index * View.tile_size
                y = row_index * View.tile_size
                if col == 'X':
                    tile = Tile((x,y),View.tile_size)
                    self.tiles.add(tile)
                if col == 'D':
                    tileDanger = TileDanger((x,y),View.tile_size)
                    self.tiles.add(tileDanger) 
                if col == 'S':
                    player_sprite = Player((x,y),View.tile_size)
                    self.player.add(player_sprite)
                if col == 'J':
                    x = col_index * View.tile_size +21
                    y = row_index * View.tile_size +21
                    powerup = JumpPowerUp((x,y),20)
                    self.powerups.add(powerup)
                    #self.powerupNum = self.powerupNum + 1
                    #print("# of powerups: " + str(self.powerupNum))
                if col == 'G':
                    x = col_index * View.tile_size +21
                    y = row_index * View.tile_size +21
                    powerup = GhostPowerUp((x,y),20)
                    self.powerups.add(powerup)
                if col == 'L':
                    x = col_index * View.tile_size +21
                    y = row_index * View.tile_size +21
                    powerup = LifePowerUp((x,y),20)
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
                    print(player.lives)
                
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
            
        
        #print(player.rect)
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
                    print(player.lives)
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jumping = False
                    
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0                      
    def powerUp_collision(self):
        #you are welcome
        dict = pygame.sprite.groupcollide(self.player, self.powerups, False, True)
        if dict: 
            #the keys of the dictionary is just a group containing the player character sprite. 
            player = list(dict.keys())
            #the values are a group that contains all the sprites that the first group collides with
            powerup = list(dict.values())

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
                player[0].ghosting = True
            if isinstance(powerup[0][0], LifePowerUp):
                pygame.time.set_timer(LifePowerUp.TIME, 500, 1)
                player[0].image = pygame.image.load("sprites/player/squid_life.png")
                player[0].lives = player[0].lives + 1
                print(player[0].lives)
    def scroll_y(self):
        #Holds the players positions
        player = self.player.sprite
        powerups = self.powerups.spritedict
        player_y = player.rect.centery
        player_top = player.rect.top
        #direction_y = player.direction.y
        #If the player passes the bottom of the screen, move the screen by the screen_h downward
        if player_y > 640:
            Level.currLevel = Level.currLevel + 1
            self.beforeSwitch_Y = player_y
            self.tiles.update(-View.screen_h)
            player.rect.centery = self.beforeSwitch_Y - View.screen_h
            
            for pu in powerups.keys():
                pu.scroll(-View.screen_h)
            #powerups.rect.centery -= View.screen_h

            
        #If the player passes the top of the screen, move the screen by the screen_h upward
        if player_top < 0:
            Level.currLevel = Level.currLevel - 1
            self.beforeSwitch_Y = player_top
            self.tiles.update(View.screen_h)
            player.rect.top = self.beforeSwitch_Y + View.screen_h
            for pu in powerups.keys():
                pu.scroll(View.screen_h)
            #powerups.rect.top += View.screen_h
        print(Level.currLevel) 
        #rint("Top pos: " + str(player.rect.top))
            
        #print("Y Position:" +str(player_y))
        #print("Before Switch: " +str(self.beforeSwitch_Y))
        #self.tiles.update(-640)
        #print(player_x)
        '''if player_y < 200 and direction_y < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_y > 500 and direction_y > 0:
            self.world_shift = -10
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5'''
    
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
        
    def input(self):
        #this is the player character object (don needed this)
        #player = self.player.sprite
        #print("Players Centery" + str(self.rect.centery))
        space_pressed = False
        font = pygame.font.SysFont(None, 20)
        #timer = font.render("Held: {} ms".format(self.space_hold_time), True, (255, 255, 255))
        #View.screen.blit(timer,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    
                sys.exit()   
            #this is don's stuff, handles the timer for the players 
            if event.type == JumpPowerUp.TIME:
                self.image = pygame.image.load("sprites/player/squidknight.png")
                self.jump_speed = -10
            if event.type == GhostPowerUp.TIME:
                self.image = pygame.image.load("sprites/player/squidknight.png")
                self.ghosting = False
            if event.type == TileDanger.HURT:
                self.image = pygame.image.load("sprites/player/squidknight.png")
                self.hurt = False
            if event.type == LifePowerUp.TIME:
                self.image = pygame.image.load("sprites/playersquidknight.png")
                
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    #space_pressed = True
                    self.space_start_time = pygame.time.get_ticks()
                '''elif event.key == pygame.K_a:
                    self.direction.x = -1
                elif event.key == pygame.K_d:
                    self.direction.x = 1
                    #print("Start time is " + str(space_start_time))'''
             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    #space_pressed = False
                    #print("pygame.time.get_ticks - startime: " + str(pygame.time.get_ticks()) + " - " + str(self.space_start_time))
                    self.space_hold_time = pygame.time.get_ticks() - self.space_start_time
                    
                    if (not self.jumping):
                        #Set jumping to True
                        self.jumping = True
                        self.jump()
                '''elif event.key == pygame.K_a:
                    self.direction.x = 0
                elif event.key == pygame.K_d:
                    self.direction.x = 0'''
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            
            self.direction.x = -1
        else:
            self.direction.x = 0 
        '''if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0'''
                

                    
        
        '''
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            scroll_thresh = 50
            #if self.rect.top > 1280 - scroll_thresh:
            
            #Will check to see if the character is currently jumping with the variable: jumping.
            if (not self.jumping):
                #Set jumping to True

                self.jumping = True
                self.jump()
        '''
        
    def jump(self):
        #print(self.space_hold_time)
        
        if self.space_hold_time < 500:
            self.direction.y = self.jump_speed 
        elif self.space_hold_time > 500 and self.space_hold_time < 2000:
            self.direction.y = self.jump_speed*1.5
        else:
            self.direction.y = self.jump_speed*1.75
        #self.direction.y = self.jump_speed
        
        #print(self.top_collision())
    
    def update(self):
        self.rect.x += self.direction.x * self.horizontalSpeed
        self.input()
        self.physics()


class View(Level):
    #Variables related to the screen's dimensions and attributues.
    level_map = []
    file1 = open("saves/save.txt","r")
    saveState = file1.read()
    #full level
    if(saveState == "0"):
        level_map = [
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '        XX               ',
        '                         ',
        '   X                     ',
        '                         ',
        '                    XX   ',
        '                         ',
        '        X                ',
        '                         ',
        'XX  XXX     X   XXX XX  X',
        ############################    
        '                         ',
        '                         ',
        '                   X     ',
        '                         ',
        '  XX                     ',
        '                 J       ',
        '                XX       ',
        '                         ',
        '                         ',
        'X  XX   XX    XX X    XXX',
        ############################    
        '                         ', 
        '                         ', 
        '                         ', 
        '     XXX                 ', 
        '                         ', 
        '  J       X              ', 
        '                     X   ',
        '     X   X    XXX    X   ',
        '           X   X     XX  ', 
        'XXXXXXXX  XXXXXXXX       ',
        ############################
        '                         ',
        '                      XXX', 
        '        XX        DXXX   ', 
        '             XXXX        ', 
        '     XXX              XXX', 
        ' X        X              ', 
        ' XX                   X  ', 
        '     X   X    XXX    XX  ', 
        '     X         X  S  XXX ', 
        'XXXXXXXXXXXXXXXXXXXXXXXXX']
    #first checkpoint
    elif(saveState == "1"):
        level_map = [
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                   S     ',
        'XXXXXXXXXXXXXXXXXXXXXXXXX']
    #second checkpoint
    elif(saveState == "2"):
        level_map = [
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        ############################
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                         ',
        '                  S      ',
        'XXXXXXXXXXXXXXXXXXXXXXXXX']

    tile_size = 64
    screen_w = 1600
    screen_h = 640
    screen = pygame.display.set_mode((screen_w,screen_h))
    pygame.display.set_caption('Platformer')
    screenImg = pygame.image.load("sprites/world_assets/underwatercastle.png")
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
    def updateScreen(self, level):
        self.screen.blit(self.screenImg, (0, 0))
        #updates the display
        
        #test_tile = pygame.sprite.Group(Tile((100,100),200))
        #test_tile.draw(self.screen)
        #level1 = Level(self.level_map,self.screen)
        
        level.run()
        pygame.display.update()
        
        self.clock.tick(60)
    
    