import turtle

#defining how the octagon should be drawn
def draw_an_octagon(color,size):
    turtle.begin_fill()
    #the loop that will repeat 8 times to draw an octagon
    for x in range(8):
        turtle.color(color)
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()
#defining where/how the pen should move once it completes an octagon
def move(x_coordinate, y_coordinate):
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()

#the commands that are repeated 4 times to create all 4 octagons in 4 different colors
draw_an_octagon(size=90, color="blue")
move(x_coordinate=0, y_coordinate=260)
draw_an_octagon(size=90, color="pink")
move(x_coordinate=-260, y_coordinate=260)
draw_an_octagon(size=90, color="red")
move(x_coordinate=-260, y_coordinate=-0)
draw_an_octagon(size=90, color="purple")

turtle.exitonclick()