
from coordinates import *
from classes import *
import movements as m



LOCATIONS = ['drinks_coord', 'dairy_coord', 'spices_coord', 'fruit_coord', 'entrance_coord']

LIST_START = [entrance_coord, dairy_coord]
LIST_DESTINATION = [drinks_coord, fruit_coord]

for start_coord, destination_coord in zip(LIST_START, LIST_DESTINATION):

    if start_coord is entrance_coord and destination_coord is fruit_coord:
        m.entrance_fruit(start_coord, [0,0])

    if start_coord is entrance_coord and destination_coord is spices_coord:
        m.entrance_spices(start_coord, [0,0])

    if start_coord is entrance_coord and destination_coord is dairy_coord:
        m.entrance_dairy(start_coord, [0,0])

    if start_coord is entrance_coord and destination_coord is drinks_coord:
        m.entrance_drinks(start_coord, [0,0])

    elif start_coord is fruit_coord and destination_coord is spices_coord:
        m.fruit_spices(start_coord, [0,0])

    elif start_coord is fruit_coord and destination_coord is dairy_coord:
        m.fruit_dairy(start_coord, [0,0])

    elif start_coord is fruit_coord and destination_coord is drinks_coord:
        m.fruit_drinks(start_coord, [0,0])

    elif start_coord is spices_coord and destination_coord is fruit_coord:
        m.spices_fruit(start_coord, [0,0])

    elif start_coord is spices_coord and destination_coord is dairy_coord:
        m.spices_dairy(start_coord, [0,0])

    elif start_coord is spices_coord and destination_coord is drinks_coord:
        m.spices_drinks(start_coord, [0,0])

    elif start_coord is dairy_coord and destination_coord is fruit_coord:
        m.dairy_fruit(start_coord, [0,0])

    elif start_coord is dairy_coord and destination_coord is spices_coord:
        m.dairy_spices(start_coord, [0,0])

    elif start_coord is dairy_coord and destination_coord is drinks_coord:
        m.dairy_drinks(start_coord, [0,0])

    elif start_coord is drinks_coord and destination_coord is fruit_coord:
        m.drinks_fruit(start_coord, [0,0])

    elif start_coord is drinks_coord and destination_coord is spices_coord:
        m.drinks_spices(start_coord, [0,0])

    elif start_coord is drinks_coord and destination_coord is dairy_coord:
        m.drinks_dairy(start_coord, [0,0])

    elif start_coord is fruit_coord and destination_coord is fruit_check_coord:
        m.fruit_checkout(start_coord, [0,0])

    elif start_coord is spices_coord and destination_coord is spices_check_coord:
        m.spices_checkout(start_coord, [0,0])

    elif start_coord is dairy_coord and destination_coord is dairy_check_coord:
        m.dairy_checkout(start_coord, [0,0])

    else:
        m.drinks_checkout(start_coord, [0,0])
    print('ronda')
