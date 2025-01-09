# Assignment 5: Retail Store
# Write a program that creates RetailItem objects and displays their details.

# Define the RetailItem class
class RetailItem:
    # Initialize the class with the following parameters
    def __init__(self, description, units_in_inventory, price):
        self.__description = description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    # Setters for data attributes
    def set_description(self, description):
        self.__description = description

    def set_units_in_inventory(self, units_in_inventory):
        self.__units_in_inventory = units_in_inventory

    def set_price(self, price):
        self.__price = price

    # Getters for data attributes
    def get_description(self):
        return self.__description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

    # Method to display the item details
    def display_item(self):
        print(f"Description: {self.__description}")
        print(f"Units in Inventory: {self.__units_in_inventory}")
        print(f"Price: ${self.__price:.2f}")
        print("-" * 20)


# Main function to create and display the RetailItem objects
def main():
    # Create the three RetailItem objects with hardcoded values
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Display the details of each item
    print("Item #1")
    item1.display_item()

    print("Item #2")
    item2.display_item()

    print("Item #3")
    item3.display_item()


# Prompt to ask the user if they want to run the code
def runcode():
    choice = input("\nDo you want to run this code? (Yes/No): ").strip().lower()
    return choice


# Run the program if the user chooses "yes"
while runcode().casefold() == "yes":
    main()
else:
    print("Code did not run. Thank you.")
