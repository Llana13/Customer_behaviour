import pandas as pd
import random

def location_prob_list(loc):
    ''''
    Create a list with location*probability for any non-first location
    '''
    move_prob_list = int(prob_matrix[loc][0]*100)*'d'+int(prob_matrix[loc][1]*100)*'s'+int(prob_matrix[loc][2]*100)*'r'+int(prob_matrix[loc][3]*100)*'f'+int(prob_matrix[loc][4]*100)*'c'
    return move_prob_list

prob_matrix = pd.DataFrame(data={'dairy':[0,0.195713,0.223151,0.189925,0.391211],
                   'spices':[0.323553,0,0.273140,0.152307,0.251000],
                   'drinks':[0.027159,0.216756,0,0.219062,0.537023],
                   'fruit':[0.238319,0.125904,0.136266,0,0.499511]},index=['dairy','spices','drinks','fruit','checkout'])

first_location_prob = pd.DataFrame(data={'dairy':[0.287576],'drinks':[0.153526],'fruit':[0.377435],'spices':[0.181464]})

first_location_prob_list = int(first_location_prob['dairy']*100)*'d'+int(first_location_prob['drinks']*100)*'r'+int(first_location_prob['fruit']*100)*'f'+int(first_location_prob['spices']*100)*'s'

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

def full_simulation():
    '''
    Simulates a customer behaviour in the supermarket
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
    return pd.Series(locations)
