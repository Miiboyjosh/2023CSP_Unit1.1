
import turtle as trtl

# Set the Background Color of the “Artistic Artifact”
trtl.speed(0)
trtl.bgcolor("Midnight Blue")
trtl.stamp()

hill1 = trtl.Turtle()
hill2 = trtl.Turtle()
bgstars = trtl.Turtle()

tloc = -475

# Draw Hill 2
hill2.penup()
hill2.goto(600, tloc)
hill2.pendown()
hill2.pensize(75)
hill2.color("cadet blue")
hill2.setheading(90)
hill2.fillcolor("cadet blue")
hill2.begin_fill()
hill2.circle(400, 180)
hill2.end_fill()
hill2.stamp()

# draw hill 1
hill1.penup()
hill1.goto(0, tloc)
hill1.pendown()
hill1.pensize(75)
hill1.color("dark slate gray")
hill1.setheading(90)
hill1.fillcolor("dark slate gray")
hill1.begin_fill()
hill1.circle(500, 180)
hill1.end_fill()
hill1.stamp()

# Draw BackGround Stars

for m in range(15):
    bgstars.penup()
    bgstars.goto(randint(-500, 500),randint(500, 850))
    bgstars.pensize()

# Draw the four main stars
# First Main Star


wn = trtl.Screen()
wn.mainloop()
