# Alex Coffman 29/JUN/23
# CMIS 102/6980 Week 3 Assignment
# This program is designed to take in user inputs for number of rooms and type of cleaning
# it will then send inputs to the function to calculate total cost to clean based off the fixed cleaning costs and size of house(certain home sizes will be upcharged)

def totalcost_calculate(numberofRooms, typeofCleaning):
    light_cleaning = 15.00    # fixed pricing variables for the types of cleaning available
    deep_cleaning = 40.00
    total_cost = 0 
    # intialize a menu off of the two string options 
    menu1 = 'light cleaning' # I chose to group the cleaning offerings into menu options becuase I could not get the formula to work when entering typeofCleaning separated by a comma (e.g., floors, windows)
    menu2 = 'deep cleaning' 
    # if/elif statements for the function to calculate the correct costs for the cleaning based on number of rooms and type of cleaning
    if typeofCleaning == menu1:
        total_cost = light_cleaning * numberofRooms
    elif typeofCleaning == menu2:
        total_cost = deep_cleaning * numberofRooms
    else:
        print("We don't provide that service option")
        return 
    
    if 3 < numberofRooms <= 7: # this is where the function calculates the applicable surcharges for homes in the medium and large categories
        total_cost *= 1.5
    elif numberofRooms > 7:
        total_cost *= 2
    
    return total_cost

def main(): # welcome message for the user and some instruction on what to do when prompted
    print("\nWelcome to Alex's house cleaning service; we provide cleaning services for small, medium, and large homes.")
    print("When prompted, please enter the amount of rooms that require cleaning and the types of cleaning needed.")
    print("\nOur list of services:\nlight cleaning: $15\ndeep cleaning: $40")
    
    numberofRooms = int(input("\nHow many rooms need to be cleaned: "))
    if numberofRooms > 3:
        print("There is a cleaning fee surcharge for medium and large homes.") # up front notice there is an upcharge for medium and large homes
    
    print("\nCleaning Menu:\nlight cleaning\ndeep cleaning")
    typeofCleaning = input("\nEnter the type of cleaning from the menu: ") # menu restated so the user knows how to input the preferred cleaning needed
          
    total_cost = totalcost_calculate(numberofRooms, typeofCleaning) # calls the function so it can be displayed 
    print("\nThe cost of house cleaning is: $",round(total_cost, 2)) # displays the total cost the user will be charged for number of rooms, type of cleaning, and home upcharge if applicable

        
main()