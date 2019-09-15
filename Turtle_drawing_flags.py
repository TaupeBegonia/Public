#############################
#   Computer Project #4
#
#   Algorithm
#      Import turtle and time module
#      Define golden ratio as symbolic constant
#      Define turtle draw speed and graphics screen size
#      Define main function
#      Define shape functions based on attributes
#      Define country flag functions based on starting coordinates and height
#      Call main function
#          Ask for input
#              Reprompt if invalid choice
#          Draw 1 or all country flags
#          Reprompt or quit program
#      Close turtle
#############################      
import turtle, time # imports turtle and time modules

GOLDEN_RATIO = 1.618 # Used in calculating star side length
# Sets up turtle screensize at 850px width and 600px height, so flags visible
turtle.setup(width = 850, height = 600, startx = None, starty = None)
turtle.speed(100) # Faster draw speed
def main():
    """ Main function that interacts with user """
    country_choice = input('''
Select one of the following options:
    TUN: Tunisia
    LBY: Libya
    TUR: Turkey
    SGP: Singapore
    ALL: All flages
    Q: Quit
''')
    while country_choice.lower() != "q":
        while country_choice.lower() != "tun" and \
            country_choice.lower() != "lby" and \
            country_choice.lower() != "tur" and \
            country_choice.lower() != "sgp" and \
            country_choice.lower() != "all":
            print("That is not a choice. Choose again.")
            country_choice = input('''
Select one of the following options:
    TUN: Tunisia
    LBY: Libya
    TUR: Turkey
    SGP: Singapore
    ALL: All flages
    Q: Quit
''')
        if country_choice.lower() == "tun":
            tunisia_flag(0, 0, 240) # Values replace parameters when run
        elif country_choice.lower() == "lby":
            libya_flag(0, 0, 240)
        elif country_choice.lower() == "tur":
            turkey_flag(0, 0, 240)
        elif country_choice.lower() == "sgp":
            singapore_flag(0, 0, 240)
        elif country_choice.lower() == "all":
            turkey_flag(0, 0, 240)
            tunisia_flag(-400, 0, 240)
            libya_flag(-400, -280, 240)
            singapore_flag(0, -280, 240)
        turtle.hideturtle() # hides turtle pointer
        time.sleep(5)
        turtle.reset() # Clears screen
        country_choice = input('''
Select one of the following options:
    TUN: Tunisia
    LBY: Libya
    TUR: Turkey
    SGP: Singapore
    ALL: All flages
    Q: Quit
''') # Reprompt the options
        
    else: # Run when quitting
        print("Goodbye!")
        
def rectangle(x, y, length, height, color): # Parameters of the function
    """
    Draws a colored rectangle
    x, y: starting coordinates (float)
    length: rectangle length (float)
    height: rectangle height (float)
    color: rectangle fill color (str)
    """
    turtle.goto(x, y)
    turtle.setheading(0) # Sets starting angle at 0 degrees (facing east)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()
    turtle.up()
    turtle.home()

def blank_rectangle(x, y, length, height, color):
    """
    Draws a blank rectangle with outline
    x, y: starting coordinates (float)
    length: rectangle length (float)
    height: rectangle height (float)
    color: rectangle border color (str)
    """
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.down()
    turtle.pencolor(color) # Sets the pen color, without fill color
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.up()
    turtle.home()

def circle(x, y, radius, color):
    """
    Draws a colored circle
    x, y: starting coordinates (float)
    radius: circle radius (float)
    color: circle fill color (str)
    """
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    turtle.home()

def crescent(x1, y1, x2, y2, R1, R2, color1, color2):
    """
    Draws a colored crescent from 2 circles
    x1, y1: first circle starting coordinates (float)
    x2, y2: second circle starting coordinates (float)
    R1: first circle radius (float)
    R2: second circle radius (float)
    color1: first circle fill color (str)
    color2: second circle fill color (str)
    """
    turtle.goto(x1, y1) # Go to first set of starting coordinates
    turtle.setheading(0)
    turtle.down()
    turtle.color(color1)
    turtle.begin_fill()
    turtle.circle(R1)
    turtle.end_fill()
    turtle.up()
    turtle.goto(x2, y2) # Go to second set of starting coordinates
    turtle.down()
    turtle.color(color2)
    turtle.begin_fill()
    turtle.circle(R2)
    turtle.end_fill()
    turtle.up()
    turtle.home()

def star(x, y, size, color, theta):
    """
    Draws a colored star with a left vertex
    x, y: starting coordinates (float)
    size: star side length (float)
    color: star fill color (str)
    theta: angle between lengths (int)
    """
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(90)
    for sides in range(1, 5): # Repeat process 4 times
        turtle.forward(size)
        turtle.right(theta)
        turtle.forward(size)
        turtle.right(theta * 2) # Alternates between angles of 72 and 144
    turtle.forward(size)
    turtle.right(theta)
    turtle.forward(size)
    turtle.end_fill()
    turtle.up()
    turtle.home()
    
def star_circle(x, y, height):
    """
    Draws a circle of colored stars from leftmost star
    x, y: starting coordinates (int)
    height: height of the flag (int)
    """
    turtle.right(90) # changes starting angle so star is upright
    star(x + height/3 - 4*height/90, \
                 y + height/2 + height/4 + 4*height/90, \
                 (4*height/45)/GOLDEN_RATIO, "white", 72) # star function
    turtle.setheading(0) # Resets the starting angle
    turtle.right(90)
    star((x + height/3 + height/3 + height/6 - 4*height/90)/2, \
                 y + height/2 + height/4 + 4*height/90 + 4*height/45, \
                 (4*height/45)/GOLDEN_RATIO, "white", 72)
    turtle.setheading(0)
    turtle.right(90)
    star(x + height/3 + height/6, \
                 y + height/2 + height/4 + 4*height/90, \
                 (4*height/45)/GOLDEN_RATIO, "white", 72)
    turtle.setheading(0)
    turtle.right(90)
    star(x + height/3, y + height/2 + 4*height/24, \
                 (4*height/45)/GOLDEN_RATIO, "white", 72)
    turtle.setheading(0)
    turtle.right(90)
    star(x + height/3 + height/6 - 4*height/90, \
                 y + height/2 + 4*height/24, \
                 (4*height/45)/GOLDEN_RATIO, "white", 72)
    turtle.home() # Goes back to (0,0)

def tunisia_flag(x, y, height):
    """
    Draws the flag of Tunisia
    x, y: starting coordinates (int)
    height: height of the flag (int)
    """
    rectangle(x, y, 1.5*height, height, "red")
    circle(x + 1.5*height/2, y + height/4, height/4, "white")
    crescent(x + 1.5*height/2, y + height/4 + height/16, \
             x + 1.5*height/2 + height/20, y + height/4 + height/10, \
             3*height/16, 3*height/20, "red", "white")
    star(x + 1.5*height/2 + height/20, y + height/4 + height/10 + 3*height/80,\
         (9*height/40)/GOLDEN_RATIO, "red", 72)

def libya_flag(x, y, height):
    """
    Draws the flag of Libya
    x, y: starting coordinates (int)
    height: height of the flag (int)
    """
    rectangle(x, y, 1.5*height, height/4, "green")
    rectangle(x, y + height/4, 1.5*height, height/2, "black")
    rectangle(x, y + 3*height/4, 1.5*height, height/4, "red")
    crescent(x + 3*height/4, y + height/4 + height/8, \
             x + 3*height/4 + height/24, y + height/4 + height/8 + height/40, \
             height/8, height/10, "white", "black")
    star(x + 3*height/4 + height/6, y + height/2 - height/16, \
         (height/8)/GOLDEN_RATIO, "white", 72)

def turkey_flag(x, y, height):
    """
    Draws the flag of Turkey
    x, y: starting coordinates (int)
    height: height of the flag (int)
    """
    blank_rectangle(x, y, height/30, height, "black") # only draws an outline
    rectangle(x + height/30, y, 1.5*height, height, "red")
    crescent(x + height/30 + height/2, y + height/4, \
             x + height/30 + height/2 + height/16, y + height/4 + height/20, \
             height/4, height/5, "white", "red")
    star(x + height/30 + 2*height/3 + height/8, y + height/2 - height/8, \
         (height/4)/GOLDEN_RATIO, "white", 72)

def singapore_flag(x, y, height):
    """
    Draws the flag of Singapore
    x, y: starting coordinates (int)
    height: height of the flag (int)
    """
    blank_rectangle(x, y, 1.5*height, height/2, "black")
    rectangle(x, y + height/2, 1.5*height, height/2, "red")
    crescent(x + height/3, y + height/2 + 7*height/108, \
             x + height/3 + height/10, y + height/2 + height/20, 5*height/27, \
             height/5, "white", "red")
    star_circle(x, y, height) # Uses same parameters as flags

main() # Calls main function
turtle.bye() # Closes turtle screen