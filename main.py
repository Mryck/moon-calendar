from p5 import *


def setup():
    size(1080, 800)  # size must be the first statement
    no_loop()


def draw():
    background(255)  # Clear the screen with a black background
    x_space = 0
    y_space_header = 40
    y_space = 0
    grid_height = height - y_space_header

    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

    # Head
    line((0, y_space_header), (width, y_space_header))
    f = create_font("Arial.ttf", 20)
    text_font(f)
    text_align("CENTER")
    for i, day in enumerate(days):
        fill(0)
        text(day, ((width / 7) * i + ((width / 7) / 2), y_space_header / 4))
    # Columns
    for _ in range(7):
        line(((width / 7) + x_space, 0), ((width / 7) + x_space, height))
        x_space += width / 7
    # Rows
    for _ in range(5):
        line(
            (0, (grid_height / 5) + (y_space + y_space_header)),
            (width, (grid_height / 5) + (y_space + y_space_header)),
        )
        y_space += grid_height / 5


if __name__ == "__main__":
    run()