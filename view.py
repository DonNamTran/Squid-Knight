import pygame, sys
import model
class View():
    #Variables related to the screen's dimensions and attributues.
    level_map = []
    file1 = open("saves/save.txt","r")
    saveState = file1.read()
    if(saveState == "0"):
        level_map = [
        '  W                      ',
        'XXXXXXXXXXXXXXXXXXX      ',
        'DDDDDDDDDDDDDDDDDDDXD    ',
        '                         ',
        '                     X  D',
        '                         ',
        '                     X   ',
        '      D     D      X     ',
        '  X X D X X D  X X       ',
        'X     X     X         X X', #1
        ############################
        '                         ',
        'X         X            X ',
        '                         ',
        '  XX                X    ',
        '   X             X       ',
        'L  X         J           ',
        'X  X         X X         ',
        '   X             X       ',
        '   X                X    ',
        ' XXXXXX     X X   X   X X', #2
        ############################
        '      X                  ',
        'X     X                X ',
        '      X              X   ',
        '      X      XXXXXXX     ',
        'X     X                  ',
        '      X    X             ',
        '      X                  ',
        'X     X  X               ',
        'X   J X                  ',
        'X   XXXXX     X  XXX  XXX', #3
        ############################
        '        X                ',
        'XXXXX   X           X    ',
        '        X     X X X      ',
        '        X   X            ',
        'XXXXX   XX               ',
        '        X                ',
        'XXXXX   XXXXXXXXXXXX     ',
        'DDDDDXXXDDDDDDDDDDDD     ',
        'DDG                      ',
        'XXXXXXXXXXXXXXXXXXXXXXX  ', #4
        ############################
        '                         ',
        '                       XX',
        '                        L',
        '                    X    ',
        '       X  X X X  X     XX',
        '    X                    ',
        '  X                      ',
        'X                        ',
        '                         ',
        '   XXX  X  XXXX          ', #5
        ############################
        '                         ',
        '         XX              ',
        '      X      G           ',
        '            XXX          ',
        '    XX           XX      ',
        '                     J   ',
        'XXX                  XX  ',
        '                         ',
        '    XX                   ',
        'XXX    XXXX XX  X X XX   ', #6
        ############################
        '                         ',
        '                       XX',
        '                         ',
        '        XX     XX        ',
        'XXX                      ',
        '                    XX   ',
        ' L                       ',
        'XXX  X         XX        ',
        '                         ',
        '       XX XX  XX         ', #7
        ############################
        '                         ',
        '                         ',
        '             X           ',
        '                J        ',
        '         XX     XX       ',
        ' XX                      ',
        '                         ',
        '        X          XX    ',
        '                         ',
        'XXXX  X  XX  XXX      XXX', #8
        ############################
        '                         ',
        '                         ',
        '                     X   ',
        '                         ',
        '      G                  ',
        '     XX  X  XX  X  X     ',
        '   X                     ',
        ' D D                     ',
        ' DLD                     ',
        ' XXXX    XX  XXX   XX  XX', #9
        ############################
        '                         ',
        '                     XX  ',
        '     XX                  ',
        '                         ',
        '                    G    ',
        '                    XX   ',
        '                         ',
        '          XX             ',
        '     J                   ',
        'X    XX       XXXXX     X', #10
        ############################
        '                         ',
        '                     XX  ',
        '                         ',
        '       XXX          X    ',
        '                         ',
        '                  X      ',
        '  XX                     ',
        '                         ',
        '                         ',
        'XX  XXXX  XXX      X    X', #11
        ############################
        '                         ',
        '        XX               ',
        '                XX       ',
        '   X                     ',
        '        XX          G    ',
        '                    XX   ',
        '                         ',
        '        X                ',
        '                         ',
        'XX  XXX     X   XXX XX  X', #12
        ############################    
        '                         ',
        '        XXX              ',
        '                   X     ',
        '                         ',
        '  XX                     ',
        '                 J       ',
        '                XX   XX  ',
        '                         ',
        '                         ',
        'X  XX   XX X  XX X    XXX', #13
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
        'XXXXXXXX  XXXXXXXX       ', #14
        ############################
        '                         ',
        '                      XXX', 
        '        XX        XXXX   ', 
        '             XDXX        ', 
        '     XXX              XXX', 
        ' X        X              ', 
        ' XX                   X  ', 
        '     X   X    XXX    XX  ', 
        '     X         X  S  XXX ', 
        'XXXXXXXXXXXXXXXXXXXXXXXXX'] #15
    #first checkpoint
    elif(saveState == "1"):
        level_map = [
        '  W                      ',
        'XXXXXXXXXXXXXXXXXXX      ',
        'DDDDDDDDDDDDDDDDDDDXD    ',
        '                         ',
        '                     X  D',
        '                         ',
        '                     X   ',
        '      D     D      X     ',
        '  X X D X X D  X X       ',
        'X     X     X         X X', #1
        ############################
        '                         ',
        'X         X            X ',
        '                         ',
        '  XX                X    ',
        '   X             X       ',
        'L  X         J           ',
        'X  X         X X         ',
        '   X             X       ',
        '   X                X    ',
        ' XXXXXX     X X   X   X X', #2
        ############################ 
        '      X                  ',
        'X     X                X ',
        '      X              X   ',
        '      X      XXXXXXX     ',
        'X     X                  ',
        '      X    X             ',
        '      X                  ',
        'X     X  X               ',
        'X   J X                  ',
        'X   XXXXX     X  XXX  XXX', #3
        ############################
        '        X                ',
        'XXXXX   X           X    ',
        '        X     X X X      ',
        '        X   X            ',
        'XXXXX   XX               ',
        '        X                ',
        'XXXXX   XXXXXXXXXXXX     ',
        'DDDDDXXXDDDDDDDDDDDD     ',
        'DDG                      ',
        'XXXXXXXXXXXXXXXXXXXXXXX  ', #4
        ############################
        '                         ',
        '                       XX',
        '                        L',
        '                    X    ',
        '       X  X X X  X     XX',
        '    X                    ',
        '  X                      ',
        'X                        ',
        '                         ',
        '   XXX  X  XXXX          ', #5
        ############################
        '                         ',
        '         XX              ',
        '      X      G           ',
        '            XXX          ',
        '    XX           XX      ',
        '                     J   ',
        'XXX                  XX  ',
        '                         ',
        '    XX                   ',
        'XXX    XXXX XX  X X XX   ', #6
        ############################
        '                         ',
        '                       XX',
        '                         ',
        '        XX     XX        ',
        'XXX                      ',
        '                    XX   ',
        ' L                       ',
        'XXX  X         XX        ',
        '                         ',
        '       XX XX  XX         ', #7
        ############################
        '                         ',
        '                         ',
        '             X           ',
        '                J        ',
        '         XX     XX       ',
        ' XX                      ',
        '                         ',
        '        X          XX    ',
        '                         ',
        'XXXX  X  XX  XXX      XXX', #8
        ############################
        '                         ',
        '                         ',
        '                     X   ',
        '                         ',
        '      G                  ',
        '     XX  X  XX  X  X     ',
        '   X                     ',
        ' D D                     ',
        ' DLD                     ',
        ' XXXX    XX  XXX   XX  XX', #9
        ############################
        '                         ',
        '                     XX  ',
        '     XX                  ',
        '                         ',
        '                    G    ',
        '                    XX   ',    
        '                         ',
        '          XX             ',
        '     J          S        ',
        'X    XX       XXXXX     X', #10
        ############################
        '                         ',
        '                     XX  ',
        '                         ',
        '       XXX          X    ',
        '                         ',
        '                  X      ',
        '  XX                     ',
        '                         ',
        '                         ',
        'XX  XXXX  XXX      X    X', #11
        ############################
        '                         ',
        '        XX               ',
        '                XX       ',
        '   X                     ',
        '        XX          G    ',
        '                    XX   ',
        '                         ',
        '        X                ',
        '                         ',
        'XX  XXX     X   XXX XX  X', #12
        ############################    
        '                         ',
        '        XXX              ',
        '                   X     ',
        '                         ',
        '  XX                     ',
        '                 J       ',
        '                XX   XX  ',
        '                         ',
        '                         ',
        'X  XX   XX X  XX X    XXX', #13
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
        'XXXXXXXX  XXXXXXXX       ', #14
        ############################
        '                         ',
        '                      XXX', 
        '        XX        XXXX   ', 
        '             XDXX        ', 
        '     XXX              XXX', 
        ' X        X              ', 
        ' XX                   X  ', 
        '     X   X    XXX    XX  ', 
        '     X         X     XXX ', 
        'XXXXXXXXXXXXXXXXXXXXXXXXX'] #15
    #second checkpoint
    elif(saveState == "2"):
        level_map = [
        '  W                      ',
        'XXXXXXXXXXXXXXXXXXX      ',
        'DDDDDDDDDDDDDDDDDDDXD    ',
        '                         ',
        '                     X  D',
        '                         ',
        '                     X   ',
        '      D     D      X     ',
        '  X X D X X D  X X       ',
        'X     X     X         X X', #1
        ############################
        '                         ',
        'X         X            X ',
        '                         ',
        '  XX                X    ',
        '   X             X       ',
        'L  X         J           ',
        'X  X         X X         ',
        '   X             X       ',
        '   X                X    ',
        ' XXXXXX     X X   X   X X', #2
        ############################
        '      X                  ',
        'X     X                X ',
        '      X              X   ',
        '      X      XXXXXXX     ',
        'X     X                  ',
        '      X    X             ',
        '      X                  ',
        'X     X   X              ',
        'X   J X                  ',
        'X   XXXXX  X  X  XXX  XXX', #3
        ############################
        '        X                ',
        'XXXXX   X           X    ',
        '        X     X X X      ',
        '        X   X            ',
        'XXXXX   XX               ',
        '        X                ',
        'XXXXX   XXXXXXXXXXXX     ',
        'DDDDDXXXDDDDDDDDDDDD     ',
        'DDG                      ',
        'XXXXXXXXXXXXXXXXXXXXXXX  ', #4
        ############################
        '                         ',
        '                       XX',
        '                        L',
        '                    X    ',
        '       X  X X X  X     XX',
        '    X                    ',
        '  X                      ',
        'X                        ',
        '             S           ',
        '   XXX  X  XXXX          ', #5
        ############################
        '                         ',
        '         XX              ',
        '      X      G           ',
        '            XXX          ',
        '    XX           XX      ',
        '                     J   ',
        'XXX                  XX  ',
        '                         ',
        '    XX                   ',
        'XXX    XXXX XX  X X XX   ', #6
        ############################
        '                         ',
        '                       XX',
        'XXX                      ',
        '        XX     XX        ',
        'XXX                      ',
        '                    XX   ',
        ' L                       ',
        'XXX  X         XX        ',
        '                         ',
        '       XX XX  XX         ', #7
        ############################
        '                         ',
        '                         ',
        '             X           ',
        '                J        ',
        '         XX     XX       ',
        ' XX                      ',
        '                         ',
        '        X          XX    ',
        '                         ',
        'XXXX  X  XX  XXX      XXX', #8
        ############################
        '                         ',
        '                         ',
        '                     X   ',
        '                         ',
        '      G                  ',
        '     XX  X  XX  X  X     ',
        '   X                     ',
        ' D D                     ',
        ' DLD                     ',
        ' XXXX    XX  XXX   XX  XX', #9
        ############################
        '                         ',
        '                     XX  ',
        '     XX                  ',
        '                         ',
        '                    G    ',
        '                    XX   ',
        '                         ',
        '          XX             ',
        '     J                   ',
        'X    XX       XXXXX     X', #10
        ############################
        '                         ',
        '                     XX  ',
        '                         ',
        '       XXX          X    ',
        '                         ',
        '                  X      ',
        '  XX                     ',
        '                         ',
        '                         ',
        'XX  XXXX  XXX      X    X', #11
        ############################
        '                         ',
        '        XX               ',
        '                XX       ',
        '   X                     ',
        '        XX          G    ',
        '                    XX   ',
        '                         ',
        '        X                ',
        '                         ',
        'XX  XXX     X   XXX XX  X', #12
        ############################    
        '                         ',
        '        XXX              ',
        '                   X     ',
        '                         ',
        '  XX                     ',
        '                 J       ',
        '                XX   XX  ',
        '                         ',
        '                         ',
        'X  XX   XX X  XX X    XXX', #13
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
        'XXXXXXXX  XXXXXXXX       ', #14
        ############################
        '                         ',
        '                      XXX', 
        '        XX        XXXX   ', 
        '             XDXX        ', 
        '     XXX              XXX', 
        ' X        X              ', 
        ' XX                   X  ', 
        '     X   X    XXX    XX  ', 
        '     X         X     XXX ', 
        'XXXXXXXXXXXXXXXXXXXXXXXXX'] #15
    
    tile_size = 64
    screen_w = 1600
    screen_h = 640
    screen = pygame.display.set_mode((screen_w,screen_h))
    pygame.display.set_caption('Squidknight')
    screenImg = pygame.image.load("sprites/world_assets/underwatercastle.png")
    screenColor = pygame.Color('black')
    

    #Clock variable that manages the FPS of the game. Kept at 60 ticks.
    clock = pygame.time.Clock()

    #model variable.
    model = ""

    def __init__(self, model):
        pygame.mixer.music.load("Sounds/background_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.10)
        titleImg = pygame.image.load("sprites/world_assets/titlescreen.png")
        screenupdate = pygame.transform.scale(titleImg,(1600,640))
        self.screen.blit(screenupdate, (0, 0))
        pygame.display.update()
        pygame.time.wait(3000)
        #Creates the font objects 
        self.score_font = pygame.font.Font('freesansbold.ttf', 28)
        self.score_font.bold = False
        self.model = model
        

    #method that updates all the objects in the screen.
    def updateScreen(self, level):
        #self.screen.fill(self.screenColor)
        self.screen.blit(self.screenImg, (0, 0))
        #updates the display
        level.run()
        player = model.Level.actualPlayer
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render(str(player.lives), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = (0,0)
        View.screen.blit(text,text_rect)
        pygame.display.update()
        
        self.clock.tick(60)
    def lose(self):
        pygame.mixer.music.load("Sounds/youDiedDS.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.10)
        YouDied = pygame.image.load("sprites/world_assets/YouDied.jpg")
        screenupdate = pygame.transform.scale(YouDied,(1600,640))
        View.screen.blit(screenupdate,(0,0))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    def win(self):
        pygame.mixer.music.load("Sounds/youWinSound.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.10)
        YouWin = pygame.image.load("sprites/world_assets/YouWin.png")
        screenupdate = pygame.transform.scale(YouWin,(1600,640))
        View.screen.blit(screenupdate,(0,0))
        pygame.display.update()
        pygame.time.wait(6000)
        pygame.quit()
        sys.exit()
        