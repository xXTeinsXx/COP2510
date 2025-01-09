# Intials Program
# Program that gets a string containing a person’s first, middle, and last names, and then display their first, middle, and last initials.

# Def that asks if the user wants to run the code
def runcode():
    runcode = str(input('\nDo you want to run this code?(Yes/No): '))
    return runcode

# Def that gets the name from the user and checks if the input is valid
def get_name():
    global name
    while True:
        name = input("Enter your full name: ")
        if name.isnumeric():
                    print('You entered a number. Please try again and enter a name.')
        else:
            break

# Def that gets the initals from the name inputed by the user.
def get_initials(name):
    words = name.split()
    initials = [word[0].upper() for word in words]
    return ".".join(initials)

# Def that runs the code by usinf the other functions.
def main():
   get_name()
   print("Your initials are:", get_initials(name))

# Code that Runs when the user wants to run the code
while runcode().casefold() == 'yes':
    main()

# If the user does not want to run the code this will happen.
else:
    print('Code did not run. Thank You.')

# Code written by Bry on Oct 17, 2024. Started writing code around 1:30pm and finished around 2:02pm.