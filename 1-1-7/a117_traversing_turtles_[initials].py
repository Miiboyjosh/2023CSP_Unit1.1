#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)



#Turtle Start Points
startx = 0
starty = 0


#Movement to Turtles After Each Iteration
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(45)
  t.forward(50)

#New Turtle Coords After Each Iteration
  start_x = t.xcor()
  start_y = t.ycor()

wn = trtl.Screen()
wn.mainloop()