# Read Golf file
# It reads the information from the golf file

# Function to read and display the contents of the golf.txt file
def read_golf_scores():
    try:
        # Open the file in read mode
        with open("golf.txt", "r") as file:
            # Read all lines from the file
            contents = file.readlines()

            # Check if the file is empty
            if not contents:
                print("The file is empty.")
                return

            print("Golf Scores:")
            for i in range(0, len(contents), 3):  # Reading in sets of 3 lines (name, score, blank line)
                player_name = contents[i].strip()  # Strip newline characters from the name
                player_score = contents[i + 1].strip()  # Strip newline characters from the score
                print(f"Player: {player_name}, Score: {player_score}")
    except FileNotFoundError:
        print("golf.txt file not found. Please run the program to add scores first.")

# Function that asks if the user wants to run the code.
def runcode():
    runcode = str(input('Do you want to run this code?(Yes/No): '))
    return runcode

# Code that runs the main function if the user does want to run the code.
while runcode().casefold() == 'Yes'.casefold():
    read_golf_scores()

# If the user does not want to run the code this will happen.
else:
     print('Code did not run. Thank You.')
