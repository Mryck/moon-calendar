from p5 import *
from day import Day


def setup():
    size(1080, 800)  # size must be the first statement
    no_loop()


def draw():
    background(255)  # Clear the screen with a black background
    y_space_header = 40
    grid_height = height - y_space_header

    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

    # Head
    f = create_font("Arial.ttf", 20)
    text_font(f)
    text_align("CENTER")
    for i, day in enumerate(days):
        stroke(0)
        fill(255)
        x = i * (width / 7)
        rect(x, 0, (width / 7), 40)
        fill(0)
        text(day, ((width / 7) * i + ((width / 7) / 2), y_space_header / 4))

    day_cells = []
    day_number = 1
    for i in range(5):
        for j in range(7):
            x = j * (width / 7)
            y = i * (grid_height / 5) + y_space_header
            stroke(0)
            fill(255)
            rect(x, y, (width / 7), (grid_height / 5))
            day_cells.append(Day(x, y, day_number))
            day_number += 1

    for day in day_cells:
        fill(0)
        text(str(day.date_number), (day.x + 15, day.y + 10))
        text_align("LEFT")
        fill(200, 200, 0)
        text(day.veg_type, (day.x + 60, day.y + 120))
        text_align("CENTER")
        fill(0)
        text(str(day.moon_phase), (day.x + 80, day.y + 77))
        text(day.moon_type, (day.x + 110, day.y + 20))


if __name__ == "__main__":
    run()