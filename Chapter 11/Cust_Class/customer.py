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
        if mail.casefold() != 'y' and mail.casefold() != 'n':
            print('You entered an invalid response. Please enter y or n.')
        else:
            break

        