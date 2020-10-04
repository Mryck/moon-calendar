import random

class Day:
    def __init__(self, x, y, date_number):

        veg_type = ['Fleurs', 'Fruits', 'Racines', 'Feuilles']

        self.x = x
        self.y = y
        self.date_number = date_number
        self.veg_type = random.choice(veg_type)
