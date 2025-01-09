# Assignment: Class and Object Practice 2

# Write a class named Person with data attributes for a person’s name, address, and telephone number. 
# Next, write a class named Customer that is a subclass of the Person class. 
# The Customer class should have a data attribute for a customer number and a Boolean data attribute indicating 
# whether the customer wishes to be on a mailing list. Demonstrate an instance of the Customer class in a simple program 
# and display all data attributes.

class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Telephone: {self.telephone}")


class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

    def display(self):
        super().display()  # Display attributes from the Person class first
        print(f"Customer Number: {self.customer_number}")
        print(f"Mailing List: {'Yes' if self.mailing_list else 'No'}")


# Creating an instance of the Person class
person1 = Person("John Smith", "123 Main St.", "555-1234")
print("Person Details:")
person1.display()
print()

# Creating an instance of the Customer class
customer1 = Customer("Jane Doe", "456 Elm St.", "555-5678", "987654321", True)
print("Customer Details:")
customer1.display()
