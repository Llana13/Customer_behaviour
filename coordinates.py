import numpy as np
'''
Coordinates of the locations and the related places
'''

# y,x,vy,vx
# Supermarket dimensions = (675, 943, 3)

# Locations:
entrance_coord = np.array([600,770])
fruit_coord = np.array([250,770])
spices_coord = np.array([250,550])
dairy_coord = np.array([250,315])
drinks_coord = np.array([250,85])

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
fruit_check_coord = np.array([600,500])
spices_check_coord = np.array([600,355])
dairy_check_coord = np.array([600,218])
drinks_check_coord = np.array([600,85])

# Cutomer
vv = [0,0]
yx = [0,0]
