# Age Classifier
# It asks the users age and clasifies them into a category then displays the output.

# Error catch and gets the users age.
# Starts a loop and checks if the age is negaive and also checks if it is a numerical value; by excepting the error it gives when it's text and not a number.
while True:
    try:
        age = int((input("What is your age? ")))
        if age < 0:
            print("Please try and enter a possitive age.")
        else:
            break
    except ValueError:
        print("Please try and enter a valid number.")

# Logic used to categorize what category the user belongs to and displays said category to the user.
if age <= 1:
    print(f"Since you are {age} years old you are a infant")

elif age < 13:
    print(f"Since you are {age} years old you are a child")

elif age < 20:
    print(f"Since you are {age} years old you are a teenager")

else:
    print(f"Since you are {age} years old you are a adult")

# Code written by Bry on 21\8\24. For programing concepts class. Wrote the code in 17 minutes (the logic) and checked errors and finished the assigment in 
# 23 minutes (v1 that i turned in). Adding the error catch took me more time (like an hour or more).