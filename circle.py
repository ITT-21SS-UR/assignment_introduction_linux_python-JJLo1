import turtle
import math
import sys

if __name__ == "__main__":
    radius = float(sys.argv[1])

# Calculate distance moved per 1 degree
distance_per_degree = (1/360)*2*math.pi*radius

# Move to starting position
turtle.penup()
turtle.left(90)
turtle.forward(radius)
turtle.right(90)
turtle.pendown()

# Save starting position coordinates
start_x = turtle.xcor()
start_y = turtle.ycor()

# Move the first step, so our while doesnt stop immediately
turtle.forward(distance_per_degree)

# Turn right by 1 degree then move our calculated distancePerDegree as long as x and y
# are not within 1 distancePerDegree of their starting values
while abs(turtle.xcor()-start_x) >= distance_per_degree or abs(turtle.ycor()-start_y) >= distance_per_degree:
    turtle.right(1)
    turtle.forward(distance_per_degree)

# Move forward 1 more step to finish the circle
turtle.forward(distance_per_degree)

turtle.done()






