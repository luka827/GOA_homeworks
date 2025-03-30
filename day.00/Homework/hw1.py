from  turtle import*

width(10)
speed(17)

left(90)

forward(150)

# roof
begin_fill()
color("brown")
right(45)
forward(150)

right(90)
forward(150)
end_fill()

#walls
color("black")
right(45)
forward(150)

right(90)
forward(212)

left(180)
forward(80)
#door
color("blue")

left(90)
forward(65)
right(90)
forward(45)
right(90)

forward(65)
color("black")

penup()
goto(212,150)
pendown()
right(90)
forward(212)
#window
width(4)
penup()
goto(65,85)
pendown()

#second window

penup()

goto(130,85)
pendown()

left(180)
forward(55)
left(90)
forward(50)
left(90)
forward(55)
left(90)
forward(50)
left(90)
forward(27)
left(90)

forward(50)

left(90)
forward(27)
left(90)
forward(25)
left(90)
forward(55)

penup()
goto(75,85)
pendown()


left(180)

forward(55)
right(90)
forward(50)
right(90)
forward(55)
right(90)
forward(50)
right(90)
forward(27)
right(90)
forward(50)
right(90)
forward(27)
right(90)
forward(25.5)
right(90)
forward(55)

penup()
goto(110,30)

pendown()
width(3)
circle(3)
#natura
penup()
goto(106,150)
pendown()

color("black")
right(270)
forward(45)

penup()
goto(104,105)
pendown()


circle(5) 


exitonclick()