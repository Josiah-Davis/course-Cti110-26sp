# Josiah Davis
# February 12, 2026
# P1HW2
# Ask user to enter budget,destination,amount spent on gas, accommodation, and food.
# Add the expenses together and subtract to the budget and display them.

# Sets the variables and prompts user
print("This program calculates anf displays travel expenses")
budg= int(input("Enter Budget: "))
loco= (input("Enter your travel destination: "))
gas= int(input(" How much do you think you wll spend on gas?"))
hotel= int(input(" Approximately, how much will you need for accomodation/hotel? "))
food= int(input(" Last, how much do you need for food? "))
result=budg - gas - hotel - food
# Displays the user input + calculates budget
print(" -------Travel Expenses-------")
print(f"Location: {loco}")
print(f"Initial budget: {budg}")
print(f"Fuel: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}")
print(f"Remaining Balance: {result}")