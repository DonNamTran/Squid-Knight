import pygame, sys, model, eventController
from view import *
from eventController import *
from model import *

#This is the class that defines our game-loop. It has the model, view, and controller objects.

class gameLoop:
    def __init__(self):
        pygame.init()
        #creates the mode, view, and events object
        
        model = Model()
        view = View(model)
        model.setViewObject(view) 
        model.initializeObjects()
        events = EventController(model, view)
        level1 = Level(view.level_map,view.screen)  
     
        #game loopplayadas 
        while True:
            #calls the method in view that updates the screen.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    
                    sys.exit()
            
            view.updateScreen(level1)
            




#Main method that starts the gameLoop
def main():
    gameLoop()

if __name__ == "__main__":
    main()