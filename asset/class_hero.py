import pygame

class Hero(object):
    def __init__(self, filename, width, height, posx, posy):
        self.filename = filename
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.x_move = 10
        self.y_move = 10


    def get_move(self,key):
        if key == 'up':
            self.posy -= self.y_move
            return self.posy
        elif key == 'down':
            self.posy += self.y_move
            return self.posy

        elif key == 'left':
            self.posx -= self.x_move
            return self.posx
        elif key == 'right':
            self.posx += self.x_move
            return self.posx
        return False
