# import turtle from turtle module.
import turtle

# creates a turtle object named "dog".
t = turtle.Turtle()

# creates a sceeen object named "screen". This will create a GUI window.
world = turtle.Screen()

# function draw_square will draw a square! 
# t is turtle.
# size is the size of the square.
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)

# function draw_filled_sqaure will draw a square.. but this time FILLED!
# t is the turtle.
# size is the size of the filled square.
# color is the color of the filled square.
def draw_filled_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

# function draw_ears will draw a filled triangle!
# t is the turtle.
# size is the size of the filled triangle.
# color is the color of the filled triangle.
def draw_ears(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

# function draw_eyes draws the eyes for the dog!
# t is the turtle.
# radius is the radius for the eyes because "t" the turtle is utilizing .circle in the turtle module.
# x is the x position of the eyes.
# y is the y position of the eyes.
# color is the color for the eyes.
def draw_eyes(t, radius, x, y, color):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# function draw_eyes draws the nose for the dog!
# t is the turtle.
# size is the size of the nose.
# x is the x positon for the nose. 
# y is the y position for the nose. 
# color is the color for the nose. 
def draw_nose(t, size, x, y, color):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

# function draw_mouth will draw the mouth for the dog!
# t is the turtle.
# x is the x position for the mouth.
# y is the y positon for the mouth.
def draw_mouth(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.forward(100)

# main function that will run our application.
def main():
    # draw_filled_square is the face of the dog.
    draw_filled_square(t, 500, "tan")

    # creates the right ear.
    t.up()
    t.goto(500,0)
    t.down()
    draw_ears(t, 200, "tan")

    # creates the left ear.
    t.up()
    t.goto(-200,0)
    t.down()
    draw_ears(t, 200, "tan")

    # creates both eyes.
    draw_eyes(t, 50, 150, -150, "white")
    draw_eyes(t, 50, 350, -150, "white")

    # creates the pupils for the eyes!
    draw_eyes(t, 30, 150, -150, "black")
    draw_eyes(t, 30, 350, -150, "black")

    draw_nose(t, 150, 180, -250, "black")

    draw_mouth(t, 100, -400)
    turtle.done()
main()