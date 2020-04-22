import random
import pandas as pd
import coordinates as co
import movements as m
from classes import *

prob_matrix = pd.read_csv(r'data/prob_matrix.csv')
first_location_prob = pd.read_csv(r'data/first_location_prob.csv')
first_location_prob_list = int(first_location_prob['dairy']*100)*'d'+int(first_location_prob['drinks']*100)*'r'+int(first_location_prob['fruit']*100)*'f'+int(first_location_prob['spices']*100)*'s'

def location_prob_list(loc):
    ''''
    Create a list with location*probability for any non-first location
    '''
    move_prob_list = int(prob_matrix[loc][0]*100)*'d'+int(prob_matrix[loc][1]*100)*'s'+int(prob_matrix[loc][2]*100)*'r'+int(prob_matrix[loc][3]*100)*'f'+int(prob_matrix[loc][4]*100)*'c'
    return move_prob_list

def set_loc(move):
    ''''
    Set loc variable to the location where the customer is but including 'checkout'
    '''
    if move == 'd':
        x = 'dairy'
    elif move == 'r':
        x = 'drinks'
    elif move == 's':
        x = 'spices'
    elif move == 'f':
        x = 'fruit'
    else: x = 'checkout'
    return x

def simulated_list():
    '''
    Create a list with a simulated customer behaviour in the supermarket
    '''
    # randomly choose from the list of locations
    first_move = random.choice(first_location_prob_list)

    loc = set_loc(first_move)
    locations = []
    locations.append(loc)
    while loc != 'checkout':
        move_prob_list = location_prob_list(loc)
        move = random.choice(move_prob_list)
        loc = set_loc(move)
        locations.append(loc)
    locations.insert(0, 'entrance')
    locations[-1] = locations[-2] + '_check'
    locations = pd.Series(locations)
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
    return locations

def full_simullation(locations):
    for i in range(len(locations)-1):
        start_coord = locations[i]
        try:
            destination_coord = locations[i+1]
        except:
            break

        if start_coord is co.entrance and destination_coord is co.fruit:
            m.entrance_fruit(start_coord, [0, 0])

        if start_coord is co.entrance and destination_coord is co.spices:
            m.entrance_spices(start_coord, [0, 0])

        if start_coord is co.entrance and destination_coord is co.dairy:
            m.entrance_dairy(start_coord, [0, 0])

        if start_coord is co.entrance and destination_coord is co.drinks:
            m.entrance_drinks(start_coord, [0, 0])

        elif start_coord is co.fruit and destination_coord is co.spices:
            m.fruit_spices(start_coord, [0, 0])

        elif start_coord is co.fruit and destination_coord is co.dairy:
            m.fruit_dairy(start_coord, [0, 0])

        elif start_coord is co.fruit and destination_coord is co.drinks:
            m.fruit_drinks(start_coord, [0, 0])

        elif start_coord is co.spices and destination_coord is co.fruit:
            m.spices_fruit(start_coord, [0, 0])

        elif start_coord is co.spices and destination_coord is co.dairy:
            m.spices_dairy(start_coord, [0, 0])

        elif start_coord is co.spices and destination_coord is co.drinks:
            m.spices_drinks(start_coord, [0, 0])

        elif start_coord is co.dairy and destination_coord is co.fruit:
            m.dairy_fruit(start_coord, [0, 0])

        elif start_coord is co.dairy and destination_coord is co.spices:
            m.dairy_spices(start_coord, [0, 0])

        elif start_coord is co.dairy and destination_coord is co.drinks:
            m.dairy_drinks(start_coord, [0, 0])

        elif start_coord is co.drinks and destination_coord is co.fruit:
            m.drinks_fruit(start_coord, [0, 0])

        elif start_coord is co.drinks and destination_coord is co.spices:
            m.drinks_spices(start_coord, [0, 0])

        elif start_coord is co.drinks and destination_coord is co.dairy:
            m.drinks_dairy(start_coord, [0, 0])

        elif co.array_in_list(destination_coord,co.checkouts):
            m.to_checkout(start_coord, [0, 0])

def ask_user():
    '''
    Prompt the user for a desired number of customer simulations
    '''
    while True:
        try:
            user_request = input('How many customers do you want to simulate? ')
            user_request = int(user_request)
            break
        except:
            print(user_request,'is not a valid number, please enter a number')
    return user_request

for customers in range(ask_user()):
    full_simullation(simulated_list())
    
