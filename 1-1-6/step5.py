#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# Create a Spider Body

spider.pensize(40)
spider.circle(20)

# Configure Spider Legs

legs = 8
lengthOfLegs = 80
spacing = 180 / legs
spider.pensize(5)
n = 0

# Draw Spider Legs

while (n < legs):
  if (n > 3):
  # Draw First Half of Legs
    spider.goto(0,20)
    spider.setheading(spacing * n)
    spider.forward(lengthOfLegs)
    n = n + 1
  else:
  # Draw Second Half of Legs
    spider.goto(0,20)
    spider.setheading(spacing * -n)
    spider.forward(lengthOfLegs)
    n = n + 1

# Draw Spider Eyes

while ()
spider.pensize(40)
spider.circle(10)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()