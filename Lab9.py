# ******************************************************************************
# Author:           Shonte Swope
# Lab:              Lab 7
# Date:             Nov 26, 2023
# Description:      This program take users input to calculate BMI compared to
#                   a random integer.
# Input:            Number for users weight and number for users height
# Output:           printed statement base on input calculation for BMI and Distance  results
# Sources:          https://runestone.academy , https://www.w3schools.com/python/
#                   python_while_loops.asp
# ******************************************************************************
#Sample run
#Story prompts
#What is your weight in pounds?: 240
#What is your height in inches?: 71
#Do you want to continue?: " "
#You did not give the right answer
#Do you want to continue?: Yes
#"The king calls his guards as they drag you to the tower 💀"
#Stoy2 prompts
# Enter distance: 56
# Enter time: 7
# Speed: 8.00 miles per hour
# More data (y/n)? y
# Enter distance: 67
#Enter time: 7
# Speed: 9.57 miles per hour
# More data (y/n)? n
# Results prompt

import random

import valid as v


def main():
    story()


def story():
    """
    Prints the introduction story of the program.
    """
    print("King Henry the 8th recently started hitting the gym. After "
          "only three days asked you (his stewart) to guess his BMI.")
    print("You are nervous, for you knows the King is famous for his "
          "outbursts and that could mean your life.")
    print("Guess the kings weight and height to give him a BMI number he will be"
          " please with but be weary.")
    print("If you give him an answer he doesnt like you will be thrown "
          "in the tower to rot.")


    # Input
    weight = get_weight()
    height = get_height()
    king = random_bmi()
    yes_no = input("Do you want to continue ")

    # Calculation
    BMI = calculated_bmi(weight, height)
    while yes_no == "":
        print("You did not give the right answer:")
        yes_no = input("Do you want to continue: ")

    # Conditional statement
    if BMI <= king:
        print("The king is happy with your answer so you and you live happy ever after 🥳")

        return story()
    else:
        print("The king calls his guards and they drag you to the tower 💀")
        return story2()


def story2():
    """
    Prints part 2 of the story of the program.
    """
    print("At the tower you are thrown into a cell. In your cell you have a single window.")
    print("You look outside an notice a horse and plan your escape.")
    print ("You calculate how many miles can you go on horse back till your safe from the king.")
    speed_list()
    # Input

def calculate_speed(distance, time):
    """
    Prompts and returns weight.
    :return: input of integer for weight

    """
    speed = distance/time
    return speed

def speed_list():
    distances = []
    times = []

    print("Speed Calculator\n")

    more_data = 'y'

    while more_data.lower() == 'y':
        distance = v.get_integer("Enter distance: ")
        time = v.get_integer("Enter time: ")
        speed = calculate_speed(distance, time)

        distances.append(distance)
        times.append(time)
        print(f"Speed: {speed:.2f} miles per hour\n")

        more_data = v.get_string("More data (y/n)? ")

    print("\nResults")
    print("Distance (miles)   Time (hours)   Speed (mph)")
    print("--------------------------------------------")

    for i in range(len(distances)):
        speed = calculate_speed(distances[i], times[i])
        print(f"{distances[i]:<18}{times[i]:<15}{speed:.2f}")
    # Conditional statement
    if distance >= 50:
        print("You can make it to safety🏃‍🏃‍")
    elif distance <= 50 or distance == 40:
        print ("You are not going to make it to safety 🙇‍")
    print(f"you can travel {distance} miles ")



def get_weight():
    """
    Prompts and returns weight.
    :return: input of integer for weight
    """
    weight = v.get_integer("What do you think is his weight in pounds? ")
    return weight

def get_height():
    """
    Prompts and returns height.
    :return: input of integer for height
    """
    height = float(input("What do you think is your height in inches? "))
    return height

def get_time():
    """
    Prompts and returns time.
    :return: input of integer for time.
    """
    time = v.get_integer("provide a integer to for how many hours ")
    return time

def get_speed():
    """
    Prompts and returns speed.
    :return: input of real number for speed.
    """
    speed = v.get_real("provide a real number 5 - 20 for miles per hour ")
    return speed

def calculated_bmi(weight, height):
    """
    Calculates weight and height inputs
    :param weight integer
    :param height integer
    :return: BMI
    """
    bmi = (weight / (height ** 2)) * 703
    return bmi
def calculate_speed(distance, time):
    """
    Calculates speed.
    :param distance: distance in miles
    :param time: time in hours
    :return: speed in miles per hour
    """
    speed = distance / time
    return speed

def random_bmi():
    """
    Issues a random integer for King
    :return: random integer
    """
    ran = random.randint(10,40)
    return ran



if __name__ == "__main__":
    main()