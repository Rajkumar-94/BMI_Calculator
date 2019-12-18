"""
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters

Excercise 1
Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user comes in underweight ,normal weight or obesity by creating a class. Read the CSV files which contains player data and compare your BMI with a player. Create functions for getting input from the user,calculating BMI and check the user category.While getting input check the value you entered is of correct type if not  and your program should not get crashed.       
        . Get user weight in kg 
        . Get user height in meter
        . Use this formula to calculate the BMI
        . BMI = weight_of_the_user/(height_of_the_user * height_of_the_user)

Use this level to check user category
        1. Less than or equal to 18.5 is represents underweight
        2. Between 18.5 -24.9 indicate normal weight
        3. Between 25 -29.9 denotes overweigh
        4. Greater than 30 denotes obese
Hint:
  Create a function to get the input from the user(check the input type)

        1. Use try...except 
        2. Use exceptional handling to check user input type
        3. Calculate the BMI
        4. Check the BMI with player BMI by reading the CSV file
"""

import csv

def compare_user_bmi_with_player(user_bmi):
    "This functions reads the csv file and compare the BMI value with players and prints the players name"

    with open('all_players_data.csv') as csvfile:
        readCSV = csv.reader(csvfile)

        #Created the empty list to load the csv data
        players_name = []
        player_bmi = []

        for row in readCSV:
            #Loads the required csv data in the lists.
            name = row[0]
            bmi = row[3]
            players_name.append(name)
            player_bmi.append(bmi)
        
        #Converts the flaot BMI value to str to compare the csv BMI.
        user_bmi = str(user_bmi)

        #compares the BMI value with players. If present it prints the player name else it prints as no match player.
        try:
            bmi_index = player_bmi.index(user_bmi)
            matched_player = players_name[bmi_index]
            print('The matched Player from the csv file for your BMI is: ',matched_player)
        except ValueError:
            print('There is no matched player in the csv file for your BMI')

def body_mass_index(w,h):
    "This function calculates the BMI of the user"

    #Calculate the BMI of the user according to weight and height, rounds of the value with single decimal and retun the calculated BMI.
    bmi=round(w/(h*h),1)
    return bmi

def weight_categogy(bmi):
    if bmi<=18.5:
        return "Under Weight"
    elif bmi>18.5 and bmi<25:
        return "Normal Weight"
    elif bmi>=25 and bmi<=29.9:
        return "Over Weight"
    elif bmi>30:
        return "Obese"

def get_user_data():
    "This function gets the input from the user"
    # Getting input will be repeated until the user provides the proper input 
    while True:
        try:
            #Accepts the input and converts into float value
            weight = float(input('Enter your weight in kilograms: '))
            height = float(input('Enter your height in meters: '))

            #Checks whether the given values are valid and if valid, it returns the weihght and height
            if weight>0 and height>0:
                return weight, height
            else:
                raise ValueError()

        #If any invalid inputs are provided, it except catches the error and it asks to provide valid input.
        except ValueError:
            print('Invalid input for weight or height. Please provide the valid details')
            continue

def wants_to_start():
    """This function asks whether the user wants to start.
    Returns: bool
    """
    #Want to start function will be repeated until the user enters the valid input
    while True: 
        answer = input("Press Y to start or Press N to exit: ").upper()
        # Prompts the use to provide is y or no and checks the provided input, if not y or n, the loop repeats untill the user provides y or n.
        if answer == 'Y':
            return True
        elif answer == 'N':
            return False
        else:
            print('Please try again.\n')

def main():
    "This function holds the control to call the other functions"

    #This  calling function checks whether user wants to start 
    if wants_to_start():

        # This calling function gets the input from the user
        weight,height = get_user_data()

        # This calling function calculates the BMI of the user
        bmi=body_mass_index(weight,height)
        
        # This calling function is used to calculate the user's criteria
        category=weight_categogy(bmi)

        print("Your BMI is ",bmi)
        print("You are",category)

        # This function is used to read the CSV file and compare the BMI value
        compare_user_bmi_with_player(bmi)
    else:
        quit()

# Program starts here
if __name__=='__main__':
    # This calling function calls the main function
    main()