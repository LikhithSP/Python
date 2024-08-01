# import turtle

# bts = turtle.Turtle()
# bts.shape('arrow')
# bts.color('green')
# bts.speed(6)

# v = turtle.Screen()
# rv.bgcolor('white')
# rv.title('My First Program')


# 1) Rectangle : for i in range(4):
#    bts.forward(100)
#   bts.left(90)

# 2) Circle and others :
# bts.circle(100, steps=6)
# bts.reset()

# 3) Program :
# bts.goto(220, -220)
# bts.down()
# bts.begin_fill()
# bts.fillcolor('yellow')
# bts.circle(50)
# bts.end_fill()
# bts.up()
# bts.home()

# OR Just : bts.up()
# draw_circle(0,-50, 'green', 50)
# draw_circle(200,200, 'orange', 50)
# draw_circle(-200,200, 'blue', 50)
# draw_circle(-200,-200, 'red', 50)
# draw_circle(200,-200, 'yellow', 50)

# 4)list1 = ['yellow', 'red', 'blue', 'green']
# bts.up()
# bts.goto(200, 0)
# for i in range(4):
# bts.down()
# bts.color(list1[i])
# bts.pensize(25)
# bts.circle(100)
# bts.up()
# bts.bk(100)

# 5) list2 = ['purple', 'red', 'orange', 'blue', 'green']
# for i in range(200):
#    bts.color(list2[i % 5])
#    bts.pensize(i/10+1)
#    bts.forward(i)
#    bts.left(59)

# bts.hideturtle()
# turtle.exitonclick()

# import turtle
# ef rectangle(color):
#    bts.begin_fill()
#    bts.fillcolor(color)
#    for i in range(2):
#        bts.forward(400)
#        bts.right(90)
#        bts.forward(100)
#        bts.right(90)
#    bts.end_fill()

# bts = turtle.Turtle()

# bts.up()
# bts.pensize(4)
# bts.goto(0, -300)
# bts.down()
# bts.goto(0, 400)
# rectangle('orange')

# bts.goto(0, 300)
# bts.forward(200)
# bts.color('blue')
# bts.circle(-50)
# bts.setheading(270)
# bts.forward(50)
# bts.setheading(0)
# for i in range(24):
#    bts.forward(45)
#    bts.bk(45)
#    bts.left(15)
# bts.setheading(90)
# bts.forward(50)
# bts.setheading(0)
# bts.color('black')
# bts.forward(200)
# bts.right(90)
# bts.forward(100)
# bts.right(90)
# bts.forward(400)
# bts.right(90)
# bts.forward(100)
# bts.right(90)

# bts.goto(0, 200)
# rectangle('green')

# bts.hideturtle()
# turtle.exitonclick()

import turtle as bts
bts.pensize(5)
bts.speed(1)
bts.color('black')
bts.begin_fill()
bts.fillcolor('red')
bts.left(150)
bts.forward(180)
bts.circle(-90, 180)
bts.setheading(60)
bts.circle(-90, 180)
bts.forward(180)
bts.end_fill()
bts.hideturtle()
bts.exitonclick()
bts.done()
