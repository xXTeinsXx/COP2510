# Lottery number generator
# Get 7 numbers that are random in the range of 1 through 60

# Importing the random function
import random

# Function that generates the lottery numbers
def lottery_num_generator():
    
    # Getting the random numbers and assigning them to a list
    
    # Initializing the list
    lottery_list = [0,0,0,0,0,0,0]

    for x in range (0, 7):
        num = random.randint(1, 60)
        lottery_list[x] = num
    
    print('These are your lottery numbers: ')

    for x in range (0, 7):
        print(lottery_list[x], end=' ')

# Function that asks the user if they want to run the code
def runcode():
    runcode = str(input('\nDo you want to run this code?(Yes/No): '))
    return runcode

# Code that runs the write_player_data and read_golf_scores function if the user does want to run the code.
while runcode().casefold() == 'yes':
    lottery_num_generator()
    
# If the user does not want to run the code this will happen.
else:
     print('Code did not run. Thank You.')