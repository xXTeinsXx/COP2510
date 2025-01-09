# Vowels and Consonants counter
# Program that counts the number of vowels and consonants in a string of characters the user enters.
# Idk man i kinda gave up for now. i have written like 5 programs in the span of 3 days and i dont even know what im doing anymore. 

# Def that asks if the user wants to run the code
def runcode():
    runcode = str(input('\nDo you want to run this code?(Yes/No): '))
    return runcode

def main():
    # Get String from user and also catch any errors.
    while True:
        user_str = input("Enter a string of characters: ")
        if user_str.isnumeric():
            print('You entered a number. Please try again and enter a name.')
        else:
            break

    # Report the vowels and consonants to the user.
    print(f'That string has {num_vowels(user_str)} vowels and {num_consonants(user_str)} consonants.')

# The num_ vowels function returns the number of vowels in the string passed as an argument.
def num_vowels(s):
    # Make a list of the vowels
    vowels = ['a','e','i','o','u']

    # Initialize the accumulator for vowels :D
    v_count = 0

    # Count the vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return the vowel count.
    return v_count

# The num_ consonants function returns the number of consonants in the string passed as an argument.
def num_consonants(s):
    # Make a list of the consonants
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    # Initialize the accumulator for consonants :D
    c_count = 0

    # Count the consonants in s.
    for ch in s:
        if ch.lower() in consonants:
            c_count += 1

    # Return the consonant count.
    return c_count

# Code that runs when the user wants to run the code
while runcode().casefold() == 'yes':
    main()

# If the user does not want to run the code this will happen.
else:
    print('Code did not run. Thank You.')

# Code written by Bry on Oct 17, 2024. Started writing code around 8:33pm and finished around 9:53pm.(prob later)