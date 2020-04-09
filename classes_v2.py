'''
Supermarket, customer and location classes
'''

import cv2
from PIL import Image

bg = cv2.imread('data/market.png')

class Customer:
    '''
    A customer blueprint that moves in the supermarket
    '''
    image = cv2.imread('data/dot.png')
    # pic = cv2.imread('data/market.png')

    def __init__(self, yx, vv, background):
        '''
        Init
        '''
        self.y = yx[0]
        self.x = yx[1]
        self.vy = vv[0]
        self.vx = vv[1]
        self.counter = 0
        self.location = [self.y, self.x]
        self.arrived = 0
        self.background = bg

    def draw(self):
        '''
        Set customer over background
        '''
        # cv2.imshow('Customer behavior simulation', self.frame)
        # self.frame = self.background.copy()
        cv2.circle(self.background, (200, 500), 50, (34, 123, 200), -1)
        self.background[self.y:self.y+57, self.x:self.x+57] = self.image

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
