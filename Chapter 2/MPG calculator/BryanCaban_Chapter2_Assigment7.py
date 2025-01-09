#MPG Calculator.
#Calculates the miles per gallon of a car and also checks if the user inputs a negative value.

miles = input('Miles Driven: ') #asks the user for the total amount of miles driven
gallons = input('Gallons used: ') #asks the user the total amount of gallons used
mpg = float(miles) / float(gallons) #MPG is the same as dividing both variables. Used float because code would error out when using decimals.

if mpg < 0:     #checks if the user inputs a negative value. if the user does not, it displays the mpg.
    print("Can't input negative numbers. Try again with possitive numbers.")

else:
    print('Your total Miles Per Gallon (MPG)is:', mpg) #displays the total with a message the user can read.

#Written by Bry on 19/8/24. For my programming concepts class.