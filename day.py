import random


class Day:
    def __init__(self, x, y, date_number):

        veg_type = ["Fleurs", "Fruits", "Racines", "Feuilles"]
        moon_phase = [i for i in range(10)]
        moon_type = ["up", "down"]

        self.x = x
        self.y = y
        self.date_number = date_number
        self.veg_type = random.choice(veg_type)
        self.moon_phase = random.choice(moon_phase)
        self.moon_type = random.choice(moon_type)
