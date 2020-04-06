
import coordinates as co
from classes import *
import movements as m
from simulation import full_simulation



locations = full_simulation()
print(locations)
locations = locations.map({'entrance': co.entrance,
                'fruit': co.fruit,
                'spices': co.spices,
                'dairy': co.dairy,
                'drinks': co.drinks,
                'fruit_check': co.fruit_check,
                'spices_check': co.spices_check,
                'dairy_check': co.dairy_check,
                'drinks_check': co.drinks_check})

locations = locations.tolist()

for i in range(len(locations)-1):
    start_coord = locations[i]
    try:
        destination_coord = locations[i+1]
    except:
        break

    if start_coord is co.entrance and destination_coord is co.fruit:
        m.entrance_fruit(start_coord, [0,0])

    if start_coord is co.entrance and destination_coord is co.spices:
        m.entrance_spices(start_coord, [0,0])

    if start_coord is co.entrance and destination_coord is co.dairy:
        m.entrance_dairy(start_coord, [0,0])

    if start_coord is co.entrance and destination_coord is co.drinks:
        m.entrance_drinks(start_coord, [0,0])

    elif start_coord is co.fruit and destination_coord is co.spices:
        m.fruit_spices(start_coord, [0,0])

    elif start_coord is co.fruit and destination_coord is co.dairy:
        m.fruit_dairy(start_coord, [0,0])

    elif start_coord is co.fruit and destination_coord is co.drinks:
        m.fruit_drinks(start_coord, [0,0])

    elif start_coord is co.spices and destination_coord is co.fruit:
        m.spices_fruit(start_coord, [0,0])

    elif start_coord is co.spices and destination_coord is co.dairy:
        m.spices_dairy(start_coord, [0,0])

    elif start_coord is co.spices and destination_coord is co.drinks:
        m.spices_drinks(start_coord, [0,0])

    elif start_coord is co.dairy and destination_coord is co.fruit:
        m.dairy_fruit(start_coord, [0,0])

    elif start_coord is co.dairy and destination_coord is co.spices:
        m.dairy_spices(start_coord, [0,0])

    elif start_coord is co.dairy and destination_coord is co.drinks:
        m.dairy_drinks(start_coord, [0,0])

    elif start_coord is co.drinks and destination_coord is co.fruit:
        m.drinks_fruit(start_coord, [0,0])

    elif start_coord is co.drinks and destination_coord is co.spices:
        m.drinks_spices(start_coord, [0,0])

    elif start_coord is co.drinks and destination_coord is co.dairy:
        m.drinks_dairy(start_coord, [0,0])

    elif destination_coord is co.fruit_check or destination_coord is co.spices_check or destination_coord is co.dairy_check or destination_coord is co.drinks_check:
        m.to_checkout(locations[i],[0,0])
