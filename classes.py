'''
Supermarket, customer and location classes
'''

import cv2
import coordinates as c

class Supermarket:
    '''
    This class is the Supermarket background where the customers are
    '''
    background = cv2.imread('data/market.png')

    def __init__(self, customers): # define attributes
        '''
        Init
        '''
        self.customers = customers
        self.frame = self.background.copy()

    def draw(self):
        '''
        Set customer over background
        '''
        self.frame = self.background.copy()
        for customer in self.customers:
            self.frame[customer.y:customer.y+57, customer.x:customer.x+57] = customer.image
        
    def render(self):
        '''
        Show the background
        '''
        cv2.imshow('market.png', self.frame)

class Customer:
    '''
    A customer blueprint that moves in the supermarket
    '''
    image = cv2.imread('data/dot.png')
    yx = [0, 0]
    vv = [0, 0]

    def __init__(self, yx, vv): # define attributes
        '''
        Init
        '''
        self.y = yx[0]
        self.x = yx[1]
        self.vy = vv[0]
        self.vx = vv[1]
        self.counter = 0

    def __iter__(self):
        '''
        Creates iterator
        '''
        return self

    def __next__(self):
        '''
        Counter
        '''
        if self.counter > 2:
            raise StopIteration
        else:
            self.counter += 1
            return self.counter -1

    def move(self):
        '''
        Movement dynamic
        '''
        self.y = self.y + self.vy
        self.x = self.x + self.vx
