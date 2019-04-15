
# Python 3 on windows
import math
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

# Step 5: Create the enemy
enemy = turtle.Turtle()  # Another turtle bbject created
enemy.color("red")  # Set enemy color to red
enemy.shape("circle")  # Set the enemy shape to circle
enemy.penup()  # We don't want anymore drawing in the background.
enemy.speed(0)  # Fast as possible
enemy.setposition(-200, -200)  # This will place our enemy somewhere on the top left of the screen

enemy_speed = 2

# step 7: Player defence
bullet = turtle.Turtle()  # turtle object
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()  # hides the turtle object until we need i.e when we are firing

bullet_speed = 20  # local var of the speed of the bullet

#Define bullet state
#ready - ready to fire
#fire - bullet is firing

bulletstate = "ready"


def fire_bullet():
    if not bullet.isvisible(): # if bullet state is ready which it is
        bulletstate = "fire"  # change var to fire
        # Move the bullet just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)  # so its the tip of the triangle
        bullet.showturtle()  # have the bullet come out of hiding

def isCollision(t1,t2): #bullet has hit the enemy (two turtle objects)
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(), 2)) #pythagoras thyroum distance between the xcor plus the distance between the ycor

    if distance < 15:
        return True
    else:
        return False


def move_left():  # The following are two function that will move our player left and right respectively.
    x = player.xcor()  # this is 0 when the game starts
    x -= player_speed  # subtracts the players speed and assigns it to x. X = 15
    if x < -280:  # If our player goes beyoud -280 pixels (our border on the left) it will be set back to - 280
        x = - 280
    player.setx(x)  # get current x subtract the speed and change the players location to the new x


def move_right():  # Same method except we are adding seeing how we are moving to the right
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)



# Create keyboard bindings for player and bullets


wn.listen()  # listen for keyboard actions
wn.onkey(move_left, "Left")  # when key is pressed move to the left
wn.onkey(move_right, "Right")  # when key is pressed move to the right.
wn.onkey(fire_bullet, "space")  # Fire when space is pressed

# Step 6: Main game loop
while True: #when the game runs meaning forever
    #  Move the enemy similar to our player from earlier
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    #boundary checking for enemy
    if enemy.xcor() > 280:
        enemy_speed *= -1 #Basically when our enemy goes over the boundary it needs to turn around and go back this is by we mutiple by postive 1 so it goes the other direction
        y = enemy.ycor() #get current y cor
        y -= 40 # bring down our enimy 40 pixels
        enemy.sety(y)

    if enemy.xcor() < -280:  # Same principle applies here
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    # Step 8: Move the bullet only in the fire state
    if bullet.isvisible():
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:  # if the posiiton of our bullet goes off of the screen
        bullet.hideturtle()  # Hide object
        bulletstate = "ready"  # Change state back to ready to fire again

    # check for collision between the bullet and the enemy
    if isCollision(bullet, enemy):
        #Reset the bullet
        bullet.hideturtle() #hide bullet
        bulletstate = "ready" #state to ready
        bullet.setposition(0, -400) #set the bullet position back to it's orignal place
        #Reset the enermy
        enemy.setposition(-200, 250)  # when hit set it back to the start

    if isCollision(player, enemy):  # When the enemy comes into contact with the player
        player.hideturtle()  # make the player go away
        enemy.hideturtle()  # make it go away
        print("Game Over")
        break  # games over break the loop







# This command tells python that we are finnish using turle commands this effeictvely means that we have to reimport it again if we want to use the turtle module
wn.mainloop()
