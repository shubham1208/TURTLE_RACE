import turtle
import random
import time
turtle.speed(0)
# SCREEN SETUP
turtle.bgcolor('forestgreen')

# HEADING
turtle.penup()
turtle.goto(-100, 205)
turtle.pendown()
turtle.pencolor('white')
turtle.write('TURTLE RACE', font = ("Arial", 20, 'bold'))

# DIRT
turtle.penup()
turtle.goto(-350, 200)
turtle.pendown()
turtle.color('brown')
turtle.begin_fill()
for i in range(2):
    turtle.forward(700)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
turtle.end_fill()

# FINISHING LINE
gap_size = 20
turtle.shape('square')
turtle.penup()

# WHITE SQUARE 
turtle.color('white')
for i in range(10):
    turtle.goto(250, (170 - (i * gap_size * 2)))
    turtle.stamp()

for i in range(10):
    turtle.goto(250 + gap_size, (190 - (i * gap_size * 2)))
    turtle.stamp()

# BLACK SQUARE
turtle.color('black')
for i in range(10):
    turtle.goto(250, (190 - (i * gap_size * 2)))
    turtle.stamp()

turtle.color('black')
for i in range(10):
    turtle.goto(270, (170 - (i * gap_size * 2)))
    turtle.stamp()

# THE RACING TURTLES
shubham = turtle.Turtle()
shubham.shape('turtle')
shubham.color('purple')
shubham.penup()
shubham.speed(0)
shubham.goto(-300, 30)
shubham.speed(1)
shubham.pendown()

jhanvi = turtle.Turtle()
jhanvi.shape('turtle')
jhanvi.color('blue')
jhanvi.penup()
jhanvi.speed(0)
jhanvi.goto(-300, -30)
jhanvi.speed(1)
jhanvi.pendown()

samriddhi = turtle.Turtle()
samriddhi.shape('turtle')
samriddhi.color('yellow')
samriddhi.penup()
samriddhi.speed(0)
samriddhi.goto(-300, 0)
samriddhi.speed(1)
samriddhi.pendown()

shreemoyee = turtle.Turtle()
shreemoyee.shape('turtle')
shreemoyee.color('orange')
shreemoyee.penup()
shreemoyee.speed(0)
shreemoyee.goto(-300, -60)
shreemoyee.speed(1)
shreemoyee.pendown()

riya = turtle.Turtle()
riya.shape('turtle')
riya.color('magenta')
riya.penup()
riya.speed(0)
riya.goto(-300, 60)
riya.speed(1)
riya.pendown()

# RACE MECHANICS
time.sleep(1)

while shubham.xcor() <= 250 and jhanvi.xcor() <= 250 and samriddhi.xcor() <= 250 and riya.xcor() <= 250 and shreemoyee.xcor() <= 250:
    shubham.forward(random.randint(1,10))
    jhanvi.forward(random.randint(1,10))
    samriddhi.forward(random.randint(1,10))
    riya.forward(random.randint(1,10))
    shreemoyee.forward(random.randint(1,10))
    

# CELEBRATE WIN
if shubham.xcor() > jhanvi.xcor() and shubham.xcor() > samriddhi.xcor() and shubham.xcor() > shreemoyee.xcor() and shubham.xcor() > riya.xcor() :
    print("Shubham won!")
    shubham.shapesize(outline = 4)
    for i in range(4):
        shubham.right(90)
    shubham.shapesize(outline = 1)
    
elif jhanvi.xcor() > shubham.xcor() and jhanvi.xcor() > samriddhi.xcor() and jhanvi.xcor() > shreemoyee.xcor() and jhanvi.xcor() > riya.xcor():
    print("Jhanvi won!")
    jhanvi.shapesize(outline = 4)
    for j in range(4):
        jhanvi.right(90)
    jhanvi.shapesize(outline = 4)

elif samriddhi.xcor() > jhanvi.xcor() and samriddhi.xcor() > shubham.xcor() and samriddhi.xcor() > shreemoyee.xcor() and samriddhi.xcor() > riya.xcor():
    print("Samriddhi won!")
    samriddhi.shapesize(outline = 4)
    for k in range(4):
        samriddhi.right(90)
    samriddhi.shapesize(outline = 1)

elif shreemoyee.xcor() > jhanvi.xcor() and shreemoyee.xcor() > samriddhi.xcor() and shreemoyee.xcor() > shubham.xcor() and shreemoyee.xcor() > riya.xcor():
    print("Shreemoyee won!")
    shreemoyee.shapesize(outline = 4)
    for l in range(4):
        shreemoyee.right(90)
    shreemoyee.shapesize(outline = 1)

elif riya.xcor() > jhanvi.xcor() and riya.xcor() > samriddhi.xcor() and riya.xcor() > shreemoyee.xcor() and riya.xcor() > shubham.xcor():
    print("Riya won!")
    riya.shapesize(outline = 4)
    for m in range(4):
        riya.right(90)
    riya.shapesize(outline = 1)

turtle.done()
