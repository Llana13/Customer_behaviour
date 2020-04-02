from coordinates import *
from classes import *
import movements as m

locations = ['drinks_coord','dairy_coord','spices_coord','fruit_coord','entrance_coord']

list_starts = [fruit_coord, drinks_coord]
list_destinations = [spices_coord,spices_coord]

for start_coord, destination_coord in zip(list_starts,list_destinations):
    print('hello')
    if np.all(destination_coord) in locations:
        if start_coord is entrance_coord:
            customer = Customer(start_coord,vv)
            supermarket = Supermarket([customer])
            m.move_to(customer,supermarket,250,customer.yx[1]) # e to f
            break
            if destination_coord is fruit_coord:
                break
            else: # customer goes to other location
                continue
        else: # MOAB customer is not in the entrance
            if start_coord is fruit_coord and destination_coord is spices_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # f to fu
                m.move_to(customer,supermarket,customer.yx[0],550) # fu to su
                m.move_to(customer,supermarket,250,customer.yx[1]) #  su to s
                break

            elif start_coord is fruit_coord and destination_coord is dairy_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # f to fu
                m.move_to(customer,supermarket,customer.yx[0],550) # fu to su
                m.move_to(customer,supermarket,customer.yx[0],315) # su to du
                m.move_to(customer,supermarket,250,customer.yx[1]) # du to d
                break

            elif start_coord is fruit_coord and destination_coord is drinks_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # f to fu
                m.move_to(customer,supermarket,customer.yx[0],550) # fu to su
                m.move_to(customer,supermarket,customer.yx[0],315) # su to du
                m.move_to(customer,supermarket,customer.yx[0],85) # du to ru
                m.move_to(customer,supermarket,85,customer.yx[1]) # ru to r
                break

            elif start_coord is spices_coord and destination_coord is fruit_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1])# s to su
                m.move_to(customer,supermarket,customer.yx[0],770)# su to fu
                m.move_to(customer,supermarket,250,customer.yx[1])# fu to f
                break

            elif start_coord is spices_coord and destination_coord is dairy_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1])# s to su
                m.move_to(customer,supermarket,customer.yx[1],315)# su to du
                m.move_to(customer,supermarket,250,customer.yx[1])# du to d
                break

            elif start_coord is spices_coord and destination_coord is drinks_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1])# s to su
                m.move_to(customer,supermarket,customer.yx[1],315)# su to du
                m.move_to(customer,supermarket,customer.yx[0],85) # du to ru
                m.move_to(customer,supermarket,85,customer.yx[1]) # ru to r
                break

            elif start_coord is dairy_coord and destination_coord is fruit_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # d to du
                m.move_to(customer,supermarket,customer.yx[1],550) # du to su
                m.move_to(customer,supermarket,customer.yx[0],770)# su to fu
                m.move_to(customer,supermarket,250,customer.yx[1])# fu to f
                break

            elif start_coord is dairy_coord and destination_coord is spices_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # d to du
                m.move_to(customer,supermarket,customer.yx[1],550) # du to su
                m.move_to(customer,supermarket,250,customer.yx[1]) #  su to s
                break

            elif start_coord is dairy_coord and destination_coord is drinks_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # d to du
                m.move_to(customer,supermarket,customer.yx[0],85) # du to ru
                m.move_to(customer,supermarket,85,customer.yx[1]) # ru to
                break

            elif start_coord is drinks_coord and destination_coord is fruit_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # r to ru
                m.move_to(customer,supermarket,85,customer.yx[1]) # ru to su
                m.move_to(customer,supermarket,315,customer.yx[1]) # su to du
                m.move_to(customer,supermarket,customer.yx[1],550) # du to su
                m.move_to(customer,supermarket,customer.yx[0],770)# su to fu
                m.move_to(customer,supermarket,250,customer.yx[1])# fu to
                break

            elif start_coord is drinks_coord and destination_coord is spices_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1]) # r to ru
                m.move_to(customer,supermarket,85,customer.yx[1]) # ru to su
                m.move_to(customer,supermarket,315,customer.yx[1]) # su to du
                m.move_to(customer,supermarket,customer.yx[1],550) # du to su
                m.move_to(customer,supermarket,250,customer.yx[1]) # su to s
                break
            else: # start_coord = drinks_coord and destination_coord = dairy_coord:
                customer = Customer(start_coord,vv)
                supermarket = Supermarket([customer])
                m.move_to(customer,supermarket,60,customer.yx[1])
                m.move_to(customer,supermarket,315,customer.yx[1])
                m.move_to(customer,supermarket,250,customer.yx[1])

    # destination is checkout
    else:
        if start_coord is fruit_coord:
            customer = Customer(start_coord,vv)
            supermarket = Supermarket([customer])
            m.move_to(customer,supermarket,450,customer.yx[1])
            m.move_to(customer,supermarket,500,customer.yx[1])
            m.move_to(customer,supermarket,600,customer.yx[1])
            break

        elif start_coord is spices_coord:
            customer = Customer(start_coord,vv)
            supermarket = Supermarket([customer])
            m.move_to(customer,supermarket,450,customer.yx[1])
            m.move_to(customer,supermarket,350,customer.yx[1])
            m.move_to(customer,supermarket,600,customer.yx[1])
            break

        elif start_coord is dairy_coord:
            customer = Customer(start_coord,vv)
            supermarket = Supermarket([customer])
            m.move_to(customer,supermarket,450,customer.yx[1])
            m.move_to(customer,supermarket,customer.yx[0],218)
            m.move_to(customer,supermarket,600,customer.yx[1])
            break

        else: # start_coord is drinks_coord:
            customer = Customer(start_coord,vv)
            supermarket = Supermarket([customer])
            m.move_to(customer,supermarket,600,customer.yx[1])
            break
