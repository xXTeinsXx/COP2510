# Import the Customer class
import customer.

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

# Def that runs the logic behind the program
def main():

    # Tell the user what the program does
    print('Welcome to the Customer Information System')
    print('-' * 25)
    print('Please enter the following information')
    get_info()
    
    # Make the mail variable into a boolean data type
    if mail.strip().casefold() == 'y':
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
