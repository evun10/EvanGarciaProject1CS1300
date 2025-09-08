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

# function draw_filled_squaere will draw a filled triangle!
# t is the turtle.
# size is the size of the filled triangle.
# color is the color of the filled triangle.
def draw_filled_triangle(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

# main function that will run our application.
def main():
    draw_filled_square(t, 500, "tan")

    t.up()
    t.goto(500,0)
    t.down()
    draw_filled_triangle(t, 200, "tan")

    t.up()
    t.goto(-200,0)
    t.down()
    draw_filled_triangle(t, 200, "tan")
    turtle.done()
main()