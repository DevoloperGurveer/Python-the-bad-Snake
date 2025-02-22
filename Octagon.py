import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(800,700)
polygon=turtle.Turtle()
num_sides=8
side_length=123
angle=360.0/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()