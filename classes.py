import numpy as np
import cv2
import coordinates
'''
Supermarket, customer and location classes
'''

class Supermarket:
    '''
    This class is the Supermarket background where the customers are
    '''
    background = cv2.imread('market.png')

    def __init__(self,customers): # define attributes
        self.customers = customers
        self.frame = self.background.copy()

    def draw(self):
        self.frame = self.background.copy()
        for customer in self.customers:
            self.frame[customer.y:customer.y+57,customer.x:customer.x+57] = customer.image

    def render (self):
        cv2.imshow('market.png',self.frame)

class Customer:
    '''
    A customer blueprint that moves in the supermarket
    '''
    image = cv2.imread('dot.png')
    yx = [0,0]
    vv = [0,0]

    def __init__(self, yx, vv): # define attributes
        self.y = yx[0]
        self.x = yx[1]
        self.vy = vv[0]
        self.vx = vv[1]
        self.counter = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.counter > 2:
            raise StopIteration
        else:
            self.counter += 1
            return self.counter -1


        fruit_coord = coordinates.fruit_coord
        fruit_up_coord = coordinates.fruit_up_coord
        fruit_down_coord = coordinates.fruit_down_coord
        fruit_check_up_coord = coordinates.fruit_check_up_coord
        fruit_check_coord = coordinates.fruit_check_coord

        spices_coord = coordinates.spices_coord
        spices_up_coord = coordinates.spices_up_coord
        spices_down_coord = coordinates.spices_down_coord
        spices_check_up_coord = coordinates.spices_check_up_coord
        spices_check_coord = coordinates.spices_check_coord

        dairy_coord = coordinates.dairy_coord
        dairy_up_coord = coordinates.dairy_up_coord
        dairy_down_coord = coordinates.dairy_down_coord
        dairy_check_up_coord = coordinates.dairy_check_up_coord
        dairy_check_coord = coordinates.dairy_check_coord

        drinks_coord = coordinates.drinks_coord
        drinks_up_coord = coordinates.drinks_up_coord
        drinks_check_coord = coordinates.drinks_check_coord


    def move(self):
        self.y = self.y + self.vy
        self.x = self.x + self.vx
