#   a114_while_guess.py

import turtle as trtl

# modify with your two favorite colors
color1 = "darkred"
color2 = "black"

wn = trtl.Screen()
height = 150 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 34
angle = 130 # experiment with the shape
seg = int(360/angle)
y_cor = painter.ycor()
while (y_cor < height):
  y_cor = painter.ycor()
  if (space % 5 == 0):
    painter.fillcolor(color1)
    painter.color(color1)
  else:
    painter.fillcolor(color2)
    painter.color(color2)

  painter.right(angle)
  painter.forward(2*space + 10) # experiment
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  space += 1

wn.mainloop()