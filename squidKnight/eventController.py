import pygame, sys, random

class EventController:
    #Variables that keep track of the model and view class. 
    model = ""
    view = ""
    def __init__(self, model, view):
        self.model = model
        self.view = view


