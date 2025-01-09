# Bug Collector program
# Program that asks the user each day how many bugs they have collected over the span of 5 days

# Runcode asks the user if the user wants to run the program or not
runcode = str(input('Do you want to run this code?(Yes/No): '))

# Runs the code if the user wants to run it. Asks the amount of days the user wants to fun it for. 
# Then does loop to ask how many bugs were caught each day then adds the total amount. Displays the value.

if runcode.casefold() == 'Yes'.casefold():
    day = int(input('How many days were you catching bugs?: '))

    total = 0 
    for day in range (1, day + 1):
        while True:
            try:
                bugs = int((input(f"How many bugs collected on day, {day}: ")))
                if bugs < 0:
                    print("Please try and enter a possitive speed.")
                else:
                    break
            except ValueError:
                print("Please try and enter a valid number.")

        total += bugs

    print(f'You have collected a total of {total} bugs over the span of {day} days.')

# If the user does not want to run the code the following message displays.
else:
    print('Code did not run. Thank You.')