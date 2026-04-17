#Import the turtle module
import turtle

#Create a turtle named phil
phil = turtle.Turtle()

#Ask user what outline color they want and set phil's pen color
outer_coloring = input("What color do you want the shape's outline to be?")
phil.color(outer_coloring)

#Ask user what filling color they want if any and set phil's filling color
inner_coloring = input("What inner color do you want for the shape? Enter 'white' for no filling.")
phil.fillcolor(inner_coloring)

#Ask user how many sides they want for their shape
side_number= int(input("How many sides do you want for your shape? Enter '0' for a circle."))

#Phil remembers the starting point for a filled shape
phil.begin_fill()

#Set up a graphic window
window = turtle.Screen()

#Ask user for radius length if they didn't want any sides and draw a circle
if side_number == 0:
    radius = int(input("What's the circle's radius?"))
    phil.circle(radius)

#Ask user for side length if they did want sides and draw the shape    
else:
    side_length = int(input("What are the sides' lengths?"))
    for sides in range(side_number):
        phil.forward(side_length)
        phil.left(360/side_number)

#Phil closes the shape and fills it with the fill color        
phil.end_fill()

#Ask user if they want to use a different fill color
new_color = input("Enter a new filler color if you want. Enter 'q' if you want to quit.")

#If the user wants to quit, print a message
if new_color == 'q':
    print("Thanks for drawing!")

else:

#Refills a circle    
    if side_number == 0:
        phil.fillcolor(new_color)
        phil.begin_fill()
        phil.circle(radius)

#Refills a shape with sides        
    else:
        phil.fillcolor(new_color)
        phil.begin_fill()
        for sides in range(side_number):
            phil.forward(side_length)
            phil.left(360/side_number)


phil.end_fill()

#Wait for user to click window to close it 
window.exitonclick()