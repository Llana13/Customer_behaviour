import cv2
from classes import Customer, bg
import coordinates as co
import random
import pandas as pd


def route_decision(start_coord, destination_coord):
    '''
    Analyze where customer is and move according to the destination
    '''
    if start_coord is co.entrance and destination_coord is co.fruit:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 250, customer.x) # e to fu

    if start_coord is co.entrance and destination_coord is co.spices:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # e to fu
        move_to(customer, customer.y, 550) # fu to su
        move_to(customer, 250, customer.x) #  su to s

    if start_coord is co.entrance and destination_coord is co.dairy:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # e to fu
        move_to(customer, customer.y, 315) # su to du
        move_to(customer, 250, customer.x) # du to d

    if start_coord is co.entrance and destination_coord is co.drinks:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # e to fu
        move_to(customer, customer.y, 85) # fu to ru
        move_to(customer, 250, customer.x) # ru to r

    elif start_coord is co.fruit and destination_coord is co.spices:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # f to fu
        move_to(customer, customer.y, 550) # fu to su
        move_to(customer, 250, customer.x) #  su to s

    elif start_coord is co.fruit and destination_coord is co.dairy:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # f to fu
        move_to(customer, customer.y, 315) # su to du
        move_to(customer, 250, customer.x) # du to d

    elif start_coord is co.fruit and destination_coord is co.drinks:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # f to fu
        move_to(customer, customer.y, 85) # du to ru
        move_to(customer, 250, customer.x) # ru to r

    elif start_coord is co.spices and destination_coord is co.fruit:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x)# s to su
        move_to(customer, customer.y, 770)# su to fu
        move_to(customer, 250, customer.x)# fu to f

    elif start_coord is co.spices and destination_coord is co.dairy:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x)# s to su
        move_to(customer, customer.y, 315)# su to du
        move_to(customer, 250, customer.x)# du to d

    elif start_coord is co.spices and destination_coord is co.drinks:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x)# s to su
        move_to(customer, customer.y, 85) # du to ru
        move_to(customer, 250, customer.x) # ru to r

    elif start_coord is co.dairy and destination_coord is co.fruit:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # d to du
        move_to(customer, customer.y, 770)# su to fu
        move_to(customer, 250, customer.x)# fu to f

    elif start_coord is co.dairy and destination_coord is co.spices:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # d to du
        move_to(customer, customer.x, 550) # du to su
        move_to(customer, 250, customer.x) #  su to s

    elif start_coord is co.dairy and destination_coord is co.drinks:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # d to du
        move_to(customer, customer.y, 85) # du to ru
        move_to(customer, 250, customer.x) # ru to

    elif start_coord is co.drinks and destination_coord is co.fruit:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # r to ru
        move_to(customer, customer.y, 770)# ru to fu
        move_to(customer, 250, customer.x)# fu to

    elif start_coord is co.drinks and destination_coord is co.spices:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # r to ru
        move_to(customer, customer.y, 550) # ru to su
        move_to(customer, 250, customer.x) # su to s

    elif start_coord is co.drinks and destination_coord is co.dairy:
        customer = Customer(start_coord, [0, 0], bg)
        move_to(customer, 60, customer.x) # r to ru
        move_to(customer, customer.y, 315) # ru to du
        move_to(customer, 250, customer.x) # du to d

    elif co.array_in_list(destination_coord,co.checkouts):
        customer = Customer(start_coord, [0, 0], bg)
        if customer.x == 770: # fruit
            move_to(customer, 450, customer.x)
            move_to(customer, customer.y, 500)
            move_to(customer, 600, customer.x)
        elif customer.x == 550: # spices
            move_to(customer, 450, customer.x)
            move_to(customer, customer.y, 355)
            move_to(customer, 600, customer.x)
        elif customer.x == 315: #dairy
            move_to(customer, 450, customer.x)
            move_to(customer, customer.y, 218)
            move_to(customer, 600, customer.x)
        else: # drinks
            move_to(customer, 600, customer.x)


def move_to(customer, target_y, target_x):
    # up
    if target_y < customer.y and target_x is customer.x:
        print('going up')
        customer.vy = -10
        customer.vx = 0
        customer.location[0] += customer.vy
        customer.location[1] += customer.vx
        customer.draw()
        customer.move()
        if customer.y == target_y:
            customer.arrived = 1
    # down
    elif target_y > customer.y and target_x is customer.x:
        print('going down')
        customer.vy = 10
        customer.vx= 0
        customer.location[0] += customer.vy
        customer.location[1] += customer.vx
        customer.draw()
        customer.move()
    # left
    elif target_x < customer.x and target_y is customer.y:
        print('going left')
        customer.vx = -10
        customer.vy = 0
        customer.location[0] += customer.vy
        customer.location[1] += customer.vx
        customer.draw()
        customer.move()
    # right
    else:
        print('going right')
        customer.vx = 10
        customer.vy = 0
        customer.location[0] += customer.vy
        customer.location[1] += customer.vx
        customer.draw()
        customer.move()

def ask_user():
    '''
    Prompt the user for a desired number of customer simulations
    '''
    while True:
        try:
            user_request = input('How many customers do you want to simulate?')
            user_request = int(user_request)
            break
        except:
            print(user_request,'is not a valid number, please enter a number')
    return user_request

def location_prob_list(loc):
    ''''
    Create a list with location*probability for any non-first location
    '''
    prob_matrix = pd.read_csv(r'data/prob_matrix.csv')
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
    first_location_prob = pd.read_csv(r'data/first_location_prob.csv')
    first_location_prob_list = int(first_location_prob['dairy']*100)*'d'+int(first_location_prob['drinks']*100)*'r'+int(first_location_prob['fruit']*100)*'f'+int(first_location_prob['spices']*100)*'s'
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
