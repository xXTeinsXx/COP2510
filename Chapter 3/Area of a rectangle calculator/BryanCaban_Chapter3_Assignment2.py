# Area of a rectangle calculator. Also indicates which rectangle is bigger or if they are the same area.

# Getting all of the valuables in preparation for the logic/equation.
length1 = float(input('What is the legth of the first rectangle?: '))
width1 = float(input('What is the width of the first rectangle?: '))
length2 = float(input('What is the legth of the second rectangle?: '))
width2 = float(input('What is the width of the second rectangle?: '))

# Calculating the area of the rectangles.
rectanglearea1 = length1 * width1
rectanglearea2 = length2 * width2

# Checks which rectangle is larger or if they are the same. Then tells the user which of the options it is.
if rectanglearea1 > rectanglearea2:
    print(f"The area of rectangle one is greater than the area of rectangle two.")

elif rectanglearea2 > rectanglearea1:
    print(f"The area of rectangle two is greater than the area of rectangle one.")

else:
    print(f'The area of both rectangles is the same.')

# Written by Bry on 20/8/24 for my programming concepts class.