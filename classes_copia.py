class FruitClass(Customer):
    '''
    Fruit location coordinates
    '''
    fruit_coord = coordinates.fruit_coord
    fruit_up_coord = coordinates.fruit_up_coord
    fruit_down_coord = coordinates.fruit_down_coord
    fruit_check_up_coord = coordinates.fruit_check_up_coord
    fruit_check_coord = coordinates.fruit_check_coord
    def __init__(self):
        super().__init__(self, yx, vy, vx,FruitClass,SpicesClass,DairyClass,DrinksClass)
class SpicesClass(Customer):
    '''
    Spices location coordinates
    '''
    spices_coord = coordinates.spices_coord
    spices_up_coord = coordinates.spices_up_coord
    spices_down_coord = coordinates.spices_down_coord
    spices_check_up_coord = coordinates.spices_check_up_coord
    spices_check_coord = coordinates.spices_check_coord
    def __init__(self):
        super().__init__(self, yx, vy, vx,FruitClass,SpicesClass,DairyClass,DrinksClass)
class DairyClass(Customer):
    '''
    Dairy location coordinates
    '''
    dairy_coord = coordinates.dairy_coord
    dairy_up_coord = coordinates.dairy_up_coord
    dairy_down_coord = coordinates.dairy_down_coord
    dairy_check_up_coord = coordinates.dairy_check_up_coord
    dairy_check_coord = coordinates.dairy_check_coord

    def __init__(self):
        super().__init__(self, yx, vy, vx,FruitClass,SpicesClass,DairyClass,DrinksClass)
class DrinksClass(Customer):
    '''
    Drinks location coordinates
    '''
    drinks_coord = coordinates.drinks_coord
    drinks_up_coord = coordinates.drinks_up_coord
    drinks_check_coord = coordinates.drinks_check_coord
    def __init__(self):
        super().__init__(self, yx, vy, vx,FruitClass,SpicesClass,DairyClass,DrinksClass)
