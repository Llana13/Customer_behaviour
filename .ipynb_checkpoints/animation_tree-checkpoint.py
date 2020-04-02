'''
Description of every possible move
'''
from coordinates import *
from classes import *
import movements as m

LOCATIONS = ['drinks_coord', 'dairy_coord', 'spices_coord', 'fruit_coord', 'entrance_coord']

LIST_START = [fruit_coord, drinks_coord]
LIST_DESTINATION = [spices_coord, spices_coord]

for start_coord, destination_coord in zip(LIST_START, LIST_DESTINATION):

    #destination is not checkout
    if np.all(destination_coord) in LOCATIONS:
        if start_coord is entrance_coord and destination_coord is fruit_coord:
            entrance_fruit()

        elif start_coord is fruit_coord and destination_coord is spices_coord:
            m.fruit_spices()

        elif start_coord is fruit_coord and destination_coord is dairy_coord:
            m.fruit_dairy()

        elif start_coord is fruit_coord and destination_coord is drinks_coord:
            m.fruit_drinks()

        elif start_coord is spices_coord and destination_coord is fruit_coord:
            m.spices_fruit()

        elif start_coord is spices_coord and destination_coord is dairy_coord:
            m.spices_dairy()

        elif start_coord is spices_coord and destination_coord is drinks_coord:
            m.spices_drinks()

        elif start_coord is dairy_coord and destination_coord is fruit_coord:
            m.dairy_fruit()

        elif start_coord is dairy_coord and destination_coord is spices_coord:
            m.dairy_spices()

        elif start_coord is dairy_coord and destination_coord is drinks_coord:
            m.dairy_drinks()

        elif start_coord is drinks_coord and destination_coord is fruit_coord:
            m.drinks_fruit()

        elif start_coord is drinks_coord and destination_coord is spices_coord:
            m.drinks_spices()
        else: # start_coord = drinks_coord and destination_coord = dairy_coord:
            m.drinks_dairy()

    # destination is checkout
    else:
        if start_coord is fruit_coord:
            m.fruit_checkout()

        elif start_coord is spices_coord:
            m.spices_checkout()

        elif start_coord is dairy_coord:
            m.dairy_checkout()

        else: # start_coord is drinks_coord:
            m.drinks_checkout()
