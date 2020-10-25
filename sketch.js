function setup() {
  createCanvas(1280, 800);
  //no_loop()
}

function draw() {
  background(255);
    var x_space = 0
    var y_space = 0
    for (var x = 0; x < 7; x++) {
        line((width / 7) + x_space, 0, (width / 7) + x_space, height)
        x_space += width / 7
    }
    for (var y = 0; y < 5; y++) {
        line(0, (height / 5) + y_space, width, (height / 5) + y_space)
        y_space += height / 5
    }
}
