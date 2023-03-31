import pygame, sys

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        
class PowerUps(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('blue')
        
        self.rect = self.image.get_rect(topleft = pos)


class Level():
    def __init__(self, level_layout, surface):
        
        self.surface = surface
        self.setup_level(level_layout)
        self.world_shift = 0
    
    def setup_level(self, layout):
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                #print(f'{row_index},{col_index}:{col}')
                x = col_index * View.tile_size
                y = row_index * View.tile_size
                if col == 'X':
                    tile = Tile((x,y),View.tile_size)
                    self.tiles.add(tile)
                if col == 'S':
                    player_sprite = Player((x,y),View.tile_size)
                    self.player.add(player_sprite)
                if col == 'P':
                    x = col_index * View.tile_size +21
                    y = row_index * View.tile_size +21
                    powerup = PowerUps((x,y),20)
                    self.powerups.add(powerup)
        
    def side_collision(self):
        #The singular rect in the player sprite
        
        #List of the tiles in the sprite tiles
        #tiles = self.tiles.sprites
        

        player = self.player.sprite
        player.rect.x += player.direction.x * player.horizontalSpeed
        
        for sprite in self.tiles.sprites():
            
            if sprite.rect.colliderect(player.rect):
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
                
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jumping = False
                    
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
    
    def jumpPowerUp_collision(self):
        #you are welcome
        dict = pygame.sprite.groupcollide(self.player, self.powerups, False, True)
        if dict: 
            list_dict = list(dict.keys())
            list_dict[0].image.fill((0, 0, 200))
            list_dict[0].jump_speed = list_dict[0].jump_speed * 1.4
            
        

    def run(self):
        # the tiles being added
        #self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
        self.powerups.draw(self.surface)
        

        self.jumpPowerUp_collision()
        self.player.update()
        self.top_collision()
        self.side_collision()
        
        self.player.draw(self.surface)
        
    
class Player(pygame.sprite.Sprite, Level):
   
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((40,40),size)
        #self.image.fill('grey')
        img = pygame.image.load("squidknight.png")
        self.image = img
        #self.image.load('squidknight.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2(0,0)
        self.horizontalSpeed = 2
        self.gravity = 0.5
        self.jump_speed = -12
        self.jumping = False
        

    def physics(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            
            self.direction.x = 1
        elif keys[pygame.K_a]:
            
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            #print(self.jumping)
            if (not self.jumping):
                self.jumping = True
                self.jump()
                
            
            

    def jump(self):
        
        self.direction.y = self.jump_speed
        #print(self.top_collision())
            

        

    def update(self):
        self.rect.x += self.direction.x * self.horizontalSpeed
        self.input()
        self.physics()


class View:
    #Variables related to the screen's dimensions and attributues.
    level_map = [

    '        XX        XXXX   ',
    '              P          ',
    '      S      XXXX        ',
    ' P   XXX              XXX',
    ' X        X              ',
    ' XX  P   P           X   ',
    '     X   X    XXX    XX  ',
    '     X         X     XXX ',
    '  XXXX XXXX    XXX   XXX ',
    'XXXXXX XXXXX  XXXXXX XXX ']
    tile_size = 64
    screen_w = 1280
    screen_h = len(level_map) * tile_size
    #screen_w = len(level_map) * tile_size
    #screen_h = 10 * tile_size
    screen = pygame.display.set_mode((screen_w,screen_h))
    pygame.display.set_caption('Platformer')
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
        self.screen.fill(self.screenColor)
        #updates the display
        
        #test_tile = pygame.sprite.Group(Tile((100,100),200))
        #test_tile.draw(self.screen)
        #level1 = Level(self.level_map,self.screen)
        
        level.run()
        pygame.display.update()
        
        self.clock.tick(60)
    
    