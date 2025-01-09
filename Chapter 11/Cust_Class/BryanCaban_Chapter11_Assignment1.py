# Assignment 1: Customer Information System
# Program that asks the user for customer information and stores it in a Customer object
# Practice using inheritance

# Person Class
class Person:
    # initialize the object
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Sets
    def set_name(self, name):
            self.__name = name

    def set_address(self, address):
            self.__address = address

    def set_phone(self, phone):
            self.__phone = phone

    # Gets
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

# Customer Class
class Customer(Person):
    # Initialize the object
    def __init__(self, name, address, phone, cust_num, mail_list):
        # Call the superclass __init__ method
        Person.__init__(self, name, address, phone)

        # Initialoze the attributes for the subclass Customer
        self.__cust_num = cust_num
        self.__mail_list = mail_list

    # sets
    def set_cust_num(self, cust_num):
        self.__cust_num = cust_num

    def set_mail_list(self, mail_list):
        self.__mail_list = mail_list

    # gets
    def get_cust_num(self):
        return self.__cust_num

    def get_mail_list(self):
        return self.__mail_list
    
# Def that asks if the user wants to run the code
def runcode():
    runcode = str(input("\nDo you want to run this code? (Yes/No): "))
    return runcode.casefold()

# Def that gets the customer information from the user
def get_info():
    
    global name, address, phone, customer_numer, mail
    # Promt the user for customer information

    # Get the customer's name and check if it is a number
    while True:
        name = input("Name: ")
        if name.isnumeric():
            print('You entered a number. Please enter a name.')
        else:
             break

    # Get the costumer's address
    address = input("Address: ")

    # Get the costumer's phone number and check if it is not a number
    while True:
        phone = input("Phone: ")
        if not phone.isnumeric():
            print('You entered a string. Please enter a number.')
        else:
            break
    
    # Get ths costumer's customer number and check if it is not a number
    while True:
        customer_numer = input("Customer Number: ")
        if not customer_numer.isnumeric():
            print('You entered a string. Please enter a number.')
        else:
            break
        
    # Get the costumer's mailing list and check if it is a string
    while True:
        mail = (input('Include in the mailing list? (y/n): '))
        if mail.casefold().strip() != 'y' and mail.casefold().strip() != 'n':
            print('You entered an invalid response. Please enter y or n.')
        else:
            break

        
# Def that runs the logic of the program
def main():

    # Tell the user what the program does
    print('Welcome to the Customer Information System')
    print('-' * 25)
    print('Please enter the following information')
    get_info()
    
    # Make the mail variable into a boolean data type
    if mail == 'y':
        mail = True
    else:
        mail = False

    # Create instance of the Customer object 
    my_customer = Customer(name, address, phone, customer_numer, mail)

    # Get the customer's information and print it to the user
    print('\nCustomer Information')
    print('-' * 25)
    print(f"Name: {my_customer.get_name()}")
    print(f"Address: {my_customer.get_address()}")
    print(f"Phone: {my_customer.get_phone()}")
    print(f"Customer Number: {my_customer.get_cust_num()}")
    print(f"Mailing List: {my_customer.get_mail_list()}")

# Code that runs when the user wants to run the code
while runcode() == 'yes':
    main()

# If the user does not want to run the code this will happen.
else:
    print('Code did not run. Thank You.')

# Code writen by Bryan Caban on 10/11/2024