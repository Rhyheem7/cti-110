# Rhyheem Rushing
# 4/21/2026
# P4LAB1

import turtle

win = turtle.Screen()
win.bgcolor("lightblue")   # simple required improvement

pen = turtle.Turtle()
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

# square (for loop)
for side in range(4):
    pen.forward(100)
    pen.left(90)

# move to top of square
pen.left(90)
pen.forward(100)
pen.right(90)

# triangle (while loop)
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

win.mainloop()