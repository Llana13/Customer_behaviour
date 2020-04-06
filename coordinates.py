import numpy as np
'''
Coordinates of the locations and the related places
'''

# y,x,vy,vx
# Supermarket dimensions = (675, 943, 3)

# Locations:
entrance = np.array([600,770])
fruit = np.array([250,770])
spices = np.array([250,550])
dairy = np.array([250,315])
drinks = np.array([250,85])

# Upper aisle
fruit_up_coord = np.array([60,770])
spices_up_coord = np.array([60,550])
dairy_up_coord = np.array([60,315])
drinks_up_coord = np.array([60,85])

# Down aisle
spices_down_coord = np.array([450,550])
fruit_down_coord = np.array([450,770])
dairy_down_coord = np.array([450,315])
fruit_check_up_coord = np.array([450,500])
dairy_check_up_coord = np.array([450,218])
spices_check_up_coord = np.array([450,355])

# Checkouts
fruit_check = np.array([600,500])
spices_check = np.array([600,355])
dairy_check = np.array([600,218])
drinks_check = np.array([600,85])
checkout = 0
checkouts = [np.array([600,500]), np.array([600,355]), np.array([600,218]), np.array([600,85])]
# Customer
vv = [0,0]
yx = [0,0]

def array_in_list(arr, list_arrays):
    '''
    Check if an array is in a list of arrays or not
    '''
    return next((True for elem in list_arrays if np.array_equal(elem, arr)), False)
