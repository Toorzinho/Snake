import turtle
import time
import random

delay = 0.1

# Score
score = 0                        # Starts with 0
high_score = 0                   # Starts with 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake")                # Game Name
wn.bgcolor("green")              # Background Color
wn.setup(width=600, height=600)  # Screen
wn.tracer(0)                     # Turns off the screen updates

# Snake head
head = turtle.Turtle()           # Using turtle you can draw the snake's head 
head.speed(0)                    # Giving the head a speed 
head.shape("square")             # Giving the head a shape
head.color("black")              # Giving the head a color 
head.penup()                     # Giving the head a penup (No drawing when moving)
head.goto(0,0)                   # Giving the head a coordinate 
head.direction = "stop"          # Giving the head a direction 

# Snake food
food = turtle.Turtle()           # Using turtle you can draw food 
food.speed(0)                    # Giving food a set speed
food.shape("circle")             # Giving food a set shape
food.color("red")                # Giving food a set color 
food.penup()                     # Giving food a set penup (No drawing when moving)
food.goto(0,100)                 # Giving food a set coordinate 

segments = []                    # Creates a list for segments 

# Pen
pen = turtle.Turtle()            # Using turtle you can draw the pen that draws the rest of the snake  
pen.speed(0)                     # Giving pen a set speed
pen.shape("square")              # Giving pen a set shape
pen.color("white")               # Giving pen a set color 
pen.penup()                      # Giving pen a set penup (No drawing when moving)
pen.hideturtle()                 # Giving pen an invisible state 
pen.goto(0, 260)                 # Giving pen a coordinate 
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")) # Creating Highscore

# Functions
def go_up():                     # Going up
    if head.direction != "down":
        head.direction = "up"

def go_down():                   # Going down
    if head.direction != "up":
        head.direction = "down"

def go_left():                   # Going left
    if head.direction != "right":
        head.direction = "left"

def go_right():                  # Going right
    if head.direction != "left":
        head.direction = "right"

def move():                      # Bevægelse
    if head.direction == "up":   # Bruger hovedet til at bestemme y koordinaten 
        y = head.ycor()
        head.sety(y + 20)        # Giver y koordinaten en værdi 

    if head.direction == "down": # Gører det samme
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left": # Gører det samme
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right": # Gører det samme
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()                       # Bruger skærm tegning til at lytte til inout 
wn.onkeypress(go_up, "w")         # Bruger de definere variabler til at bevæge slangen
wn.onkeypress(go_down, "s")       # Bruger de definere variabler til at bevæge slangen
wn.onkeypress(go_left, "a")       # Bruger de definere variabler til at bevæge slangen
wn.onkeypress(go_right, "d")      # Bruger de definere variabler til at bevæge slangen

# Main game loop
while True:
    wn.update()                   # Da vores skærm opdateres konstant, så opdaterer vi skærmen

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:  # Hvis slangen rammer kanten
        time.sleep(1)             # Så stopper spillet i et sekund
        head.goto(0,0)            # Slangen starter forfra ved koordinaterne (0,0)
        head.direction = "stop"   # Derefter stopper slangen med at bevæge sig 

        # Hide the segments
        for segment in segments:  
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()