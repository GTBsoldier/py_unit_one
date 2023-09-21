import turtle

def draw_an_octagon(color,size):
    turtle.begin_fill()
    for x in range(8):
        turtle.color(color)
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()

def move(x_coordinate, y_coordinate):
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()

draw_an_octagon(color="blue", size=90)
move(x_coordinate=0, y_coordinate=260)
draw_an_octagon(color="pink", size=90)
move(x_coordinate=-260, y_coordinate=260)
draw_an_octagon(color="red", size=90)
move(x_coordinate=-260, y_coordinate=-0)
draw_an_octagon(color="purple", size=90)

turtle.exitonclick()