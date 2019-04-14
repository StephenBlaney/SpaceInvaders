
# Python 3 on windows

import turtle
import os


# Step 1: Set up the screen
wn = turtle.Screen()  # basically we need to create a screen object which we derive from the turtle module
wn.bgcolor("black")  # Background of are screen is set to black as it's the color of our space background
wn.title("Space Invaders")  # The opening title of our screen object

# Step 2: Draw a border  the game will be 600x 600 in teh centre of the screen.
border_pen = turtle.Turtle()  # Create a turtle pen the following is than a list of all the attrbutes for that turle this basically is like a pencil that draws our screen
border_pen.penup()
border_pen.speed(0)  # This line means the speed of drawing and zero in this cause is teh fastest which is what we want
border_pen.color("white")  # Set border color to white
border_pen.setposition(-300, -300) # These are the pixel dimensions of our screen.
border_pen.pendown()
border_pen.pensize(3)  # This describes the thickness of the line
for side in range(4):  # loop 4 times
    border_pen.fd(600)  # forward 600 pixels
    border_pen.lt(90)   # left 90 degrees
border_pen.hideturtle() # hides our turtle pen

# Step 3: Create a player turtle
player = turtle.Turtle()  # Turtle object created
player.color("blue")
player.shape("triangle")
player.penup()  # lift the pen
player.speed(0)  # needs to be the fastest due to the nature of it being a game
player.setposition(0, -250)  # Centre towards the bottom
player.setheading(90)  # Now, initially our triangle is positioned to the right we need to change by 90 degrees using this line

# Step 4: Player controls
player_speed = 15 # variable that contains our chractar speed for now

# The following are two function that will move our player left and right respectively.
def move_left():
    x = player.xcor()  # this is 0 when the game starts
    x -= player_speed  # subtracts the players speed and assigns it to x. X = 15
    if x < -280:  # If our player goes beyoud -280 pixels (our border on the left) it will be set back to - 280
        x = - 280
    player.setx(x)  # get current x subtract the speed and change the players location to the new x

def move_right(): #Same method except we are adding seeing how we are moving to the right
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


# Create keyboard bindings
turtle.listen()  # listen for keyboard actions
turtle.onkey(move_left, "Left")  # when key is pressed move to the left
turtle.onkey(move_right, "Right")  # when key is pressed move to the right.















turtle.done() # This command tells python that we are finnish using turle commands this effeictvely means that we have to reimport it again if we want to use the turtle module
