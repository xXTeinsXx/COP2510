# Sum of numbers
# Program that reads a txt file full of numbers and adds them together

def read_file():
    try:
        # Open the file 
        with open("numbers.txt", "r") as file:
            # Read all lines from the file
            contents = file.readlines()

            # Check if the file is empty
            if not contents:
                print("The file is empty.")
                return

            print("Numbers: ")
            # Initialize a variable to store the sum
            total = 0

            # Read the file and calculate the sum
            for line in contents:
                number = int(line.strip())  # Strip whitespace and convert to int
                total += number
                print(number)

            print("Sum of numbers:", total)

    except FileNotFoundError:
        print("numbers.txt file not found. Please make sure the file is accessible.")


def runcode():
    runcode = str(input('Do you want to run this code?(Yes/No): '))
    return runcode

# Code that runs the write_player_data and read_golf_scores function if the user does want to run the code.
while runcode().casefold() == 'yes':
    read_file()
    
# If the user does not want to run the code this will happen.
else:
     print('Code did not run. Thank You.')