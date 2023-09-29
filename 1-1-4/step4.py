#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
variable = 5
# Add a loop with a zero-iteration condition
while (variable < 6):
    painter.circle(50, 180, 4)


# Add an infinite loop
while (variable > 0):
    painter.right(angle)
    painter.forward(space)
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()

wn = trtl.Screen()
wn.mainloop()