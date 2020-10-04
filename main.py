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

    for i in range(7):
        for j in range(5):
            x = i * (width / 7)
            y = j * (grid_height / 5) + y_space_header
            stroke(0)
            fill(255)
            rect(x, y, (width / 7), (grid_height / 5))


if __name__ == "__main__":
    run()