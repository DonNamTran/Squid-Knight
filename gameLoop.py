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

        #game loop
        while True:

            #calls the method in view that updates the screen. 
            view.updateScreen()

            #calls the methods to move the player, opponent, and the ball.
            events.movePlayer()
            events.moveOpponent()
            events.moveBall()

#Main method that starts the gameLoop
def main():
    gameLoop()

if __name__ == "__main__":
    main()