import turtle as trtl

josh = trtl.Turtle()
james = trtl.Turtle()
colton = trtl.Turtle()
ryan = trtl.Turtle()
daquan = trtl.Turtle()

turtleList = [josh, james, colton, ryan, daquan]

x = -100
y = 0

for turtle in turtleList:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x = x + 30


wn = trtl.Screen()
wn.mainloop()