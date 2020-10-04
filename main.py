from p5 import *


def setup():
    size(1280, 800)  # size must be the first statement
    no_loop()


def draw():
    background(255)  # Clear the screen with a black background
    x_space = 0
    y_space = 0
    for x in range(7):
        line(((width / 7) + x_space, 0), ((width / 7) + x_space, height))
        x_space += width / 7
    for y in range(5):
        line((0, (height / 5) + y_space), (width, (height / 5) + y_space))
        y_space += height / 5


if __name__ == "__main__":
    run()