# Distance over time calculator

# Runcode asks the user if the user wants to run the program or not
def reruncode():
    runcode = str(input('Do you want to run this code?(Yes/No): '))
    return runcode

# If statement used to run the code for the user if they answer yes
while reruncode().casefold() == 'Yes'.casefold():

    # Checks if the input(mph) is a number
    while True:
        try:
            speed = int((input("What was your speed (MPH)?: ")))
            if speed < 0:
                print("Please try and enter a possitive speed.")
            else:
                break
        except ValueError:
            print("Please try and enter a valid number.")

    # Checks if the input(hours) is a number
    while True:
        try:
            time = int((input("How many hours have you traveled?: ")))
            if time < 0:
                print("Please try and enter a possitive time.")
            else:
                break
        except ValueError:
            print("Please try and enter a valid number.")

    # Loop that runs for the amount of hours the user specified. then gives the distance traveled.
    for time in range (1, time + 1):
        distancetraveled = time * speed
        
        print(f'Hours | Distance Traveled')
        print(f'{time}     |{distancetraveled}') # Weird spacing for the neatness in the terminal.
        
    print("This is the total distance over time")

# If the user does not run the code the following runs.
else:
    print('Code did not run. Thank You.')
    