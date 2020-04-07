import numpy as np
'''
Coordinates of the locations and the related places
Supermarket dimensions = (675, 943, 3)
'''

# Locations:
entrance = np.array([600,770])
fruit = np.array([250,770])
spices = np.array([250,550])
dairy = np.array([250,315])
drinks = np.array([250,85])

# Checkouts
fruit_check = np.array([600,500])
spices_check = np.array([600,355])
dairy_check = np.array([600,218])
drinks_check = np.array([600,85])
checkouts = [np.array([600,500]), np.array([600,355]), np.array([600,218]), np.array([600,85])]
# Customer
vv = [0,0]
yx = [0,0]

def array_in_list(arr, list_arrays):
    '''
    Check if an array is in a list of arrays or not
    '''
    return next((True for elem in list_arrays if np.array_equal(elem, arr)), False)
