# Chapter 14 #1
# Population_database

import sqlite3

#main fuction
def main():
    # Menu Choice
    choice = 0

    # Connect to the database
    conn = sqlite3.connect('cities.db')

    # Get a database cursor
    cur = conn.cursor()

    # Get the user's menu choice
    while choice != 8:
        choice = get_menu_choice()
        execute_choice(choice, cur)
    
    # Close the connection
    conn.close()


# The display_menu function displays the menu
def display_menu():
    print('               MENU')
    print('-'*35)
    print('1 - Display cities sorted by population, assending order')
    print('2 - Display cities sorted by population, descending order')
    print('3 - Display cities sorted by name')
    print('4 - Display total population of all the cities')
    print('5 - Display average population of all the cities')
    print('6 - Display city with the highest population')
    print('7 - Display city with the lowest population')
    print('8 - EXIT') 


# The get_menu_choice function displays the menu and gets the user's choice
def get_menu_choice():
    display_menu()
    choice = int(input('Enter your choice: '))
    
    # Check if the user's choice is valid
    while choice < 1 or choice > 8:
        print('Invalid choice. Please try again.')
        choice = int(input('Enter your choice: '))
    return choice


# Preform the action that the user selected
def execute_choice(choice, cur):
    if choice == 1:
        citites_sorted_ascending(cur)
    elif choice == 2:
        citites_sorted_descending(cur)
    elif choice == 3:
        citites_sorted_by_name(cur)
    elif choice == 4:
        total_population(cur)
    elif choice == 5:
        average_population(cur)
    elif choice == 6:
        highest_population(cur)
    elif choice == 7:
        lowest_population(cur)


# Display the cities sorted by population, ascending order
def citites_sorted_ascending(cur):
    # Execute the SELECTED statement on the database
    cur.execute('''SELECT CityName, Population
                FROM Cities 
                ORDER BY Population''')
    
    # Fetch all of the results.
    results = cur.fetchall()

    # Display the results
    print('\nCities Sorted By Population in Ascending Order:')
    print('-'*35)
    display_results(results)


# Display the cities sorted by population, descending order
def citites_sorted_descending(cur):
    # Execute the SELECTED statement on the database
    cur.execute('''SELECT CityName, Population
                FROM Cities 
                ORDER BY Population DESC''')
    
    # Fetch all of the results.
    results = cur.fetchall()

    # Display the results
    print('\nCities Sorted By Population in Descending Order:')
    print('-'*35)
    display_results(results)


# Display the cities sorted by name
def citites_sorted_by_name(cur):
    # Execute the SELECTED statement on the database
    cur.execute('''SELECT CityName, Population
                FROM Cities 
                ORDER BY CityName''')
    
    # Fetch all of the results.
    results = cur.fetchall()

    # Display the results
    print('\nCities Sorted By Name:')
    print('-'*35)
    display_results(results)


# Display the total population of all the cities
def total_population(cur):
    # Execute the SELECTED statement on the database
    cur.execute('''SELECT SUM(Population) 
                FROM Cities''')
    
    # Fetch all of the results.
    results = cur.fetchone()

    # Display the results
    print(f'\nTotal Population of All Cities: {results[0]:,.0f}\n')


# Display the average population of all the cities
def average_population(cur):
    # Execute the SELECTED statement on the database
    cur.execute('''SELECT AVG(Population) 
                FROM Cities''')
    
    # Fetch all of the results.
    results = cur.fetchone()

    # Display the results
    print(f'\nAverage Population: {results[0]:,.0f}\n')


# Display the city with the highest population
def highest_population(cur):
    # Execute the SELECTED statement on the database
    cur.execute('SELECT MAX(Population) FROM Cities')
    
    # Fetch all of the results.
    max_results = cur.fetchone()

    # Get the entire row that gets the population
    cur.execute('''SELECT CityName, Population FROM Cities
                WHERE Population = ?''', (max_results[0],))
    
    # Fetch the results
    results = cur.fetchone()

    # Display the results
    print(f'\n{results[0]} has the Highest Population:{results[1]:,.0f}\n')


# Display the city with the lowest population
def lowest_population(cur):
    # Execute the SELECTED statement on the database
    cur.execute('SELECT MIN(Population) FROM Cities')
    
    # Fetch all of the results.
    min_results = cur.fetchone()

    # Get the entire row that gets the population
    cur.execute('''SELECT CityName, Population FROM Cities
                WHERE Population = ?''', (min_results[0],))
    
    # Fetch the results
    results = cur.fetchone()

    # Display the results
    print(f'\n{results[0]} has the Lowest Population:{results[1]:,.0f}\n')


# Display the results
def display_results(results):
    print(f'{"City":20}{"Population":}')
    for row in results:
        print(f'{row[0]:20}{row[1]:,.0f}')
    print()


#Execute the main fuction
if __name__ == '__main__':
    main()

# Finished the last assignment for COP2510 taught by professor Melichar during the Fall Term on 26/11/2024 
# -Bry