
from coordinates import *
from classes import *
import movements as m
from simulation import full_simulation



locations = full_simulation()
locations.insert(0,entrance)
for i in locations:
    globals()[i]
print(locations)

LIST_START = [fruit, dairy]
LIST_DESTINATION = [checkout]

for start_coord, destination_coord in zip(LIST_START, LIST_DESTINATION):

    if start_coord is entrance and destination_coord is fruit:
        m.entrance_fruit(start_coord, [0,0])

    if start_coord is entrance and destination_coord is spices:
        m.entrance_spices(start_coord, [0,0])

    if start_coord is entrance and destination_coord is dairy:
        m.entrance_dairy(start_coord, [0,0])

    if start_coord is entrance and destination_coord is drinks:
        m.entrance_drinks(start_coord, [0,0])

    elif start_coord is fruit and destination_coord is spices:
        m.fruit_spices(start_coord, [0,0])

    elif start_coord is fruit and destination_coord is dairy:
        m.fruit_dairy(start_coord, [0,0])

    elif start_coord is fruit and destination_coord is drinks:
        m.fruit_drinks(start_coord, [0,0])

    elif start_coord is spices and destination_coord is fruit:
        m.spices_fruit(start_coord, [0,0])

    elif start_coord is spices and destination_coord is dairy:
        m.spices_dairy(start_coord, [0,0])

    elif start_coord is spices and destination_coord is drinks:
        m.spices_drinks(start_coord, [0,0])

    elif start_coord is dairy and destination_coord is fruit:
        m.dairy_fruit(start_coord, [0,0])

    elif start_coord is dairy and destination_coord is spices:
        m.dairy_spices(start_coord, [0,0])

    elif start_coord is dairy and destination_coord is drinks:
        m.dairy_drinks(start_coord, [0,0])

    elif start_coord is drinks and destination_coord is fruit:
        m.drinks_fruit(start_coord, [0,0])

    elif start_coord is drinks and destination_coord is spices:
        m.drinks_spices(start_coord, [0,0])

    elif start_coord is drinks and destination_coord is dairy:
        m.drinks_dairy(start_coord, [0,0])

    else:
        m.to_checkout(start_coord,[0,0])
