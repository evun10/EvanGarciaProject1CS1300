Part 1: Draw a puppy face (50 pts)
1. In main create a Screen and a Turtle.
2. Create the following functions:
a. draw_square- that takes a turtle as a parameter and the size of the square
b. draw_filled_square – that takes a turtle, the size you want the square to be
and the color as parameters.
c. draw_filled_triangle – that takes a turtle, the size you want the triangle to be
and the color as parameters.
3. Using the functions you just created and the built in turtle functions create a picture
that is similar to this:
REMEMBER: all functions should have comments telling what they are doing and what
the parameters are.
Part 2: Refactoring your code (25 pts)
Now let’s clean up your code by refactoring (cleaning up and revising) your code. You will
take the code you have written and move it into functions (that you create).
1. You should create a function that is called draw_eyes that takes a turtle, x
position, y position, and color) this function will call the turtle commands to
create your eyes.
a. Add code to correct the eye that is not filled in.
b. Add code to give the eyes pupils (another circle inside the existing one)
2. Also, you should have a function that draw_nose that takes a turtle, x, y, and
color.
3. Lastly take the code you used to draw the ears and move/revise it into a function
call draw_ear that takes a turtle, x, y, color. By doing one ear you can change the
color of each and if you wanted to could change the direction the ear is pointing.
4. A function that draws a mouth for your puppy draw_mouth this one will most
likely only need the turtle and x and y as parameters
REMEMBER: all functions should have comments telling what they are doing and what
the parameters are.
Part 4 Draw a border (15 pts)
Now lets draw a border of shapes around our picture. I chose to use squares but you can
use any shape you want as long as you use for loops while creating the border. It is much
easier to do one side at a time.
You will need a function call draw_border that takes a turtle and depending on the shape
you choose a size. This function is very specific to your drawing so it will be different for
each person.
Part 5: Challenge (5pts)
As a challenge see if you can get each shape to draw a random color.
Hint: you will need to import the random function and change the turtle’s color mode
