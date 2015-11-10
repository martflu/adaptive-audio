import pygame
import color
import vector
import rectangle

class player():
    
    def __init__(self, res_x, res_y):
        w = 20
        h = 20
        x = (res_x / 4)
        y = 2 * (res_y / 3) - (h / 2)
        c = color.color((40, 40, 40))
        self.rectangle = rectangle.rectangle(x, y, w, h, c)
        self.vector = vector.vector(0, 0)  