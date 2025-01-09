# Number Analysis Program
# Get 10 numbers from the user and calculate the lowest, highest, total, and average

# Defenition that checks if the user wants to run the code
def runcode():
    runcode = str(input('\nDo you want to run this code?(Yes/No): '))
    return runcode

# Main function that gets the user input and calculates the average
def main():
  numbers = []

  # Get 10 numbers from the user
  for i in range(10):
    number = float(input("Enter number " + str(i + 1) + ": "))
    numbers.append(number)

  # Find the lowest, highest, total, and average
  lowest = min(numbers)
  highest = max(numbers)
  total = sum(numbers)
  average = total / len(numbers)

  # Display the results
  print("Lowest number:", lowest)
  print("Highest number:", highest)
  print("Total:", total)
  print("Average:", average)

# Code that runs the write_player_data and read_golf_scores function if the user does want to run the code.
while runcode().casefold() == 'yes':
    main()
    
# If the user does not want to run the code this will happen.
else:
     print('Code did not run. Thank You.')