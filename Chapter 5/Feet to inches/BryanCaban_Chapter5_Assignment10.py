# Feet to inches calculator
# A calculator that checks coverts feet to inches.

# Constant: One foot is the same as 12 inches
CONVERTIONFACTOR = int(12)

# Main function that runs the calculations
def main():
    # Checks if the value for posstive or not.
    while True:
        try:
            feet = float(input('What is the number of feet?: '))
            if feet < 0:
                print("Please try and enter a possitive value.")
            else:
                break
        except ValueError:
            print("Please try and enter a valid number.")
    
    # It does the conversition for feet to inches.
    inches = feet_to_inches(feet)
    print(f'{feet} feet are the same as {inches} inches.')

# Function that asks if the user wants to run the code or not
def reruncode():
    runcode = str(input('Do you want to run this code?(Yes/No): '))
    return runcode

# Calculations that covert from feet to inches
def feet_to_inches (feet):
    inches = feet * CONVERTIONFACTOR
    return inches

# While reruncode is true it will continue to run the code
while reruncode().casefold() == 'Yes'.casefold():
    main()
    
# Since the user does not want to run the code it will run the following:
else:
    print('Code did not run. Thank You.')