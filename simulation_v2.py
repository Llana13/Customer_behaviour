from movements import ask_user, simulated_list, route_decision
import cv2
from classes import bg

cv2.imshow('Supermarket', bg)

customers_locs = []
for customers in range(ask_user()):
    customers_locs.append(simulated_list())

i = 0
for customer in customers_locs:
    print('locations: ', customer)
    start_coord = customer[i]
    print('starting' ,start_coord)
    try:
        destination_coord = customer[i+1]
        print('destination ', destination_coord)
    except:
        break
    i += 1
    route_decision(start_coord, destination_coord)

cv2.waitKey(0)
cv2.destroyAllWindows()
