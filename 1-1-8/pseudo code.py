

import turtle as trtl

# Set the Background Color of the “Artistic Artifact”
trtl.speed(0)
trtl.bgcolor("Midnight Blue")

# Create and Empty List of hill_turtles
hill1_trtl = []
hill2_trtl = []
# Give the hill_turtles color
trtl_shapes = ["circle"]
hill1_color = ["dark slate gray", "green"]
hill2_color = ["green", "dark slate gray"]

# Give the Turtles an Origin Location

tloc = -150
# Use a for loop for the hill_turtles
for s in trtl_shapes:
	h1 = trtl.Turtle(shape=s)
	h1.penup()
	new_color = hill1_color.pop()
	h1.fillcolor(new_color)
	h1.goto(-400, tloc)
	h1.setheading(90)

	h2 = trtl.Turtle(shape=s)
	h2.penup()
	new_color = hill2_color.pop()
	h2.fillcolor(new_color)
	h2.goto(100, tloc)
	h2.setheading(270)

	tloc += 50

for steps in range(50):
	for h1 in hill1_trtl:
		for h2 in hill2_trtl:
			h1.shape("semicircle")
			h2.shape("semicircle")

wn = trtl.Screen()
wn.mainloop()
