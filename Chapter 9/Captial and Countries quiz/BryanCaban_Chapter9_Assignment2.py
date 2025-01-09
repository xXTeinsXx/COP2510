#State and Capitals quiz game

# Import random to get random entry from dict
import random

# Function to ask if the user wants to run the code
def runcode():
    runcode = input("\nDo you want to run this code? (Yes/No): ")
    return runcode.lower() == 'yes'

# Define states and capitals dictionary
states_and_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta"
}

# Main quiz function
def main():
    # Initialize counters for correct and incorrect responses
    correct_answers = 0
    incorrect_answers = 0

    # Welcome message
    print("Welcome to the State and Capitals Quiz Game!")
    print("This program will test your knowledge of the states and their capitals.")
    
    # Repeat the quiz 5 times
    for _ in range(5):
        # Select a random state
        state, capital = random.choice(list(states_and_capitals.items()))
        
        # Prompt the user for the capital of the selected state
        answer = input(f"What is the capital of {state}?: ").strip()
        
        # Check if the answer is correct
        if answer.lower() == capital.lower():
            correct_answers += 1
            print("Correct!")
        else:
            incorrect_answers += 1
            print(f"Incorrect! The capital of {state} is {capital}.")

    # Display the results
    total_questions = correct_answers + incorrect_answers
    print(f"\nYou got {correct_answers} correct answers and {incorrect_answers} incorrect answers.")
    print(f"Your score: {correct_answers}/{total_questions}")

# Run the code if the user agrees
while runcode():
    main()

# If the user does not want to run the code
print("Thank you for playing!")
