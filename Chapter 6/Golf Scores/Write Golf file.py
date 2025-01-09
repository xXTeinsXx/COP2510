# Golf Scores
# Create a program to input each player's name and golf score from the keyboard and save the information as records in a file named golf.txt.

# Main function that gets the inputs and writes them to a .txt file.
def write_player_data(): 
    # Asks fot the number of player that want to be added
    while True:
        try:
            num_players = (int(input('How many player do you want to add?: ')))
            if num_players < 0:
                    print("Please try and enter a possitive value.")
            else:
                break
        except ValueError:
                print("Please try and enter a valid number.")
    
    player_data = []
    # Asks the users to get the playes name and score.
    for num_players in range (1, num_players + 1):
        
        print(f'Enter player {num_players} name and score:')

        while True:
            player_name = str(input('Player name: '))
            if player_name.isnumeric():
                    print('You entered a number. Please try again and enter a name.')
            else:
                break

        while True:
            try:
                player_score = int(input('Player score: '))
                if player_score < 0:
                    print("Please try and enter a possitive value.")
                else:
                    break
            except ValueError:
                    print("Please try and enter a valid number.")
        player_data.append((player_name, player_score))
    

    with open("golf.txt", "a") as playernameandscore:
        for player_name, player_score in player_data:
            playernameandscore.write(f"{player_name}\n{player_score}\n\n")

    print('Data saved correctly.')

# Function that asks if the user wants to run the code.
def runcode():
    runcode = str(input('Do you want to run this code?(Yes/No): '))
    return runcode

# Code that runs the write_player_data function if the user does want to run the code.
while runcode().casefold() == 'Yes'.casefold():
    write_player_data()

# If the user does not want to run the code this will happen.
else:
     print('Code did not run. Thank You.')