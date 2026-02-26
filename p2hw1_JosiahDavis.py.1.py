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
hotel= int(input(" Approximately, how much will you need for accomodation/hotel?"))
food= int(input(" Last, how much do you need for food? "))
result=budg - gas - hotel - food
# Displays the user input + calculates budget
# Width Formatting
print("---------------------Results------------------------")
print(f"{'Location:':<20}{loco:<14.2f}")
print(f"{'Initial Budget:':<20}${budg:<14.2f}")
print(f"{'Fuel':<20}${gas:<14.2f}")
print(f"{'Accomodation':<20}${hotel:<14.2f}")
print(f"{'Food':<20}${food:<14.2f}")
print("----------------------------------------------------")
print()
print(f"{'Remaining Balance: ':<20}${result:<14.2f}")

