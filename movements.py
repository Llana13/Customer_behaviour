import cv2
from classes import Supermarket, Customer

def move_to(customer, supermarket, target_y, target_x):

    # up
    if target_y < customer.yx[0] and target_x is customer.yx[1]:
        while customer.yx[0] > target_y:
            customer.vv[0] = -1
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break
    # down
    elif target_y > customer.yx[0] and target_x is customer.yx[1]:
        while customer.yx[0] < target_y:
            customer.vv[0] = 1
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break
    # left
    elif target_x < customer.yx[1] and target_y is customer.yx[0]:
        while customer.yx[1] > target_x:
            customer.vv[1] = -1
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break
    # right
    else:
        while customer.yx[1] < target_x:
            customer.vv[1] = 1
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break

# Start_Destination

def entrance_fruit():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    m.move_to(customer, supermarket, 250, customer.yx[1])

def fruit_spices():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # f to fu
    move_to(customer, supermarket, customer.yx[0], 550) # fu to su
    move_to(customer, supermarket, 250, customer.yx[1]) #  su to s

def fruit_dairy():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # f to fu
    move_to(customer, supermarket, customer.yx[0], 550) # fu to su
    move_to(customer, supermarket, customer.yx[0], 315) # su to du
    move_to(customer, supermarket, 250, customer.yx[1]) # du to d

def fruit_drinks():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # f to fu
    move_to(customer, supermarket, customer.yx[0], 550) # fu to su
    move_to(customer, supermarket, customer.yx[0], 315) # su to du
    move_to(customer, supermarket, customer.yx[0], 85) # du to ru
    move_to(customer, supermarket, 85, customer.yx[1]) # ru to r

def spices_fruit():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1])# s to su
    move_to(customer, supermarket, customer.yx[0], 770)# su to fu
    move_to(customer, supermarket, 250, customer.yx[1])# fu to f

def spices_dairy():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1])# s to su
    move_to(customer, supermarket, customer.yx[1], 315)# su to du
    move_to(customer, supermarket, 250, customer.yx[1])# du to d

def spices_drinks():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1])# s to su
    move_to(customer, supermarket, customer.yx[1], 315)# su to du
    move_to(customer, supermarket, customer.yx[0], 85) # du to ru
    move_to(customer, supermarket, 85, customer.yx[1]) # ru to r

def dairy_fruit():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # d to du
    move_to(customer, supermarket, customer.yx[1], 550) # du to su
    move_to(customer, supermarket, customer.yx[0], 770)# su to fu
    move_to(customer, supermarket, 250, customer.yx[1])# fu to f

def dairy_spices():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # d to du
    move_to(customer, supermarket, customer.yx[1], 550) # du to su
    move_to(customer, supermarket, 250, customer.yx[1]) #  su to s

def dairy_drinks():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # d to du
    move_to(customer, supermarket, customer.yx[0], 85) # du to ru
    move_to(customer, supermarket, 85, customer.yx[1]) # ru to

def drinks_fruit():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # r to ru
    move_to(customer, supermarket, 85, customer.yx[1]) # ru to su
    move_to(customer, supermarket, 315, customer.yx[1]) # su to du
    move_to(customer, supermarket, customer.yx[1], 550) # du to su
    move_to(customer, supermarket, customer.yx[0], 770)# su to fu
    move_to(customer, supermarket, 250, customer.yx[1])# fu to

def drinks_spices():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1]) # r to ru
    move_to(customer, supermarket, 85, customer.yx[1]) # ru to su
    move_to(customer, supermarket, 315, customer.yx[1]) # su to du
    move_to(customer, supermarket, customer.yx[1], 550) # du to su
    move_to(customer, supermarket, 250, customer.yx[1]) # su to s

def drinks_dairy():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.yx[1])
    move_to(customer, supermarket, 315, customer.yx[1])
    move_to(customer, supermarket, 250, customer.yx[1])

def fruit_checkout():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 450, customer.yx[1])
    move_to(customer, supermarket, 500, customer.yx[1])
    move_to(customer, supermarket, 600, customer.yx[1])

def spices_checkout():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 450, customer.yx[1])
    move_to(customer, supermarket, 350, customer.yx[1])
    move_to(customer, supermarket, 600, customer.yx[1])

def dairy_checkout():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 450, customer.yx[1])
    move_to(customer, supermarket, customer.yx[0], 218)
    move_to(customer, supermarket, 600, customer.yx[1])

def drinks_checkout():
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 600, customer.yx[1])
