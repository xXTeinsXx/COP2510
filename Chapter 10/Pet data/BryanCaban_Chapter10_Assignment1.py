# Animal Info Assignment
# Write a class named  Pet , which should have the following data attributes:
#  •  __name (for the name of a pet)
#  •  __animal_type (for the type of animal that a pet is. Example values are 'Dog', 'Cat', and 'Bird')
#  •  __age (for the pet's age)


# Class that holds the pet information
class Pet:
    # Intialize the class with the following parameters:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Sets for data attributes
    def get_name(self, name):
        return self.__name

    def get_animal_type(self, animal_type):
        return self.__animal_type

    def get_age(self, age):
        return self.__age

    # Gets for data attributes
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
    def __str__(self):
        return f"The pet's name is {self.__name}, the pet's animal type is {self.__animal_type}, and the pet's age is {self.__age}"

# Def that asks if the user wants to run the code
def runcode():
    runcode = str(input("\nDo you want to run this code? (Yes/No): "))
    return runcode.casefold()

# Def that gets the animal information from the user
def get_animal_info():
    # Promt the user for animal information
    pet_name = input("What is the name of the pet? ")
    pet_animal_type = input("What type of animal do you have? ")
    pet_age = input("What is the age of the pet? ")
    
    pet_info = Pet(pet_name, pet_animal_type, pet_age)

    # Get the pet's information and print it to the user
    # print(f"The pet's name is {pet_info.get_name()}")
    # print(f"The pet's animal type is {pet_info.get_animal_type()}")
    # print(f"The pet's age is {pet_info.get_age()}")
    print(pet_info)

# Code that runs when the user wants to run the code
while runcode() == 'yes':
    get_animal_info()

# If the user does not want to run the code this will happen.
else:
    print('Code did not run. Thank You.')
