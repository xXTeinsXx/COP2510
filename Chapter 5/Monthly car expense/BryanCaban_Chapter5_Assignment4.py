# Monthly And Annual cost of a car
# This program will ask the user the monthly costs of different aspects of car ownership and then 

# Main function that asks the user fr all of the necesary variables and then prints the total
def main():
    # Asks for the value of loan
    while True:
            try:
                loan = round(float(input('What is the current cost of your loan payment?: ')), 2)
                if loan < 0:
                    print("Please try and enter a possitive value.")
                else:
                    break
            except ValueError:
                print("Please try and enter a valid number.")

    # Asks for the value of insurance
    while True:
            try:
                insurance = round(float(input('What is the current cost of your car insurance?: ')), 2)
                if insurance < 0:
                    print("Please try and enter a possitive value.")
                else:
                    break
            except ValueError:
                print("Please try and enter a valid number.")

    # Asks for the value of gas
    while True:
            try:
                gas = round(float(input('What was this months gas total?: ')), 2)
                if gas < 0:
                    print("Please try and enter a possitive value.")
                else:
                    break
            except ValueError:
                print("Please try and enter a valid number.")

    # Asks for the value of oil
    while True:
            try:
                oil = round(float(input('What was this months oil total?: ')), 2)
                if oil < 0:
                    print("Please try and enter a possitive value.")
                else:
                    break
            except ValueError:
                print("Please try and enter a valid number.")

    # Asks for the value of tire
    while True:
            try:
                tire = round(float(input('What was this months tire cost: ')), 2)
                if tire < 0:
                    print("Please try and enter a possitive value.")
                else:
                    break
            except ValueError:
                print("Please try and enter a valid number.")

    # Asks for the value of tire
    while True:
            try:
                maintanence = round(float(input('What was this month maintanance cost?: ')), 2)
                if maintanence < 0:
                    print("Please try and enter a possitive value.")
                else:
                    break
            except ValueError:
                print("Please try and enter a valid number.")

    # Sets all of the values to be the same as "monthlyexpenses"
    monthlyexpenses = [loan, insurance, gas, oil, tire, maintanence]
    totalmonthlycost, totalyearlycost = calcExpenses(monthlyexpenses)

    print(f"This months total cost is ${totalmonthlycost} at this monthly rate it'll be ${totalyearlycost} in 12 months.")

# Adds all of the monthly car expenses into one and returns the value.
def calcExpenses(monthlyexpenses):
    totalmonthlycost = sum(monthlyexpenses)
    totalyearlycost = totalmonthlycost * 12
    return totalmonthlycost, totalyearlycost

# Function that asks if the user wants to run the code or not
def reruncode():
    runcode = str(input('Do you want to run this code?(Yes/No): '))
    return runcode

# While reruncode is true it will continue to run the code
while reruncode().casefold() == 'Yes'.casefold():
    main()
    
# Since the user does not want to run the code it will run the following:
else:
    print('Code did not run. Thank You.')
    