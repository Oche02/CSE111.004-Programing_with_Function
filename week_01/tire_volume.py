"""
Author: Augustine Okpe Oche
Purpose: Calculate the volume of a tire and store the results in a text file.
creativity: Ask whether the user wants to buy tires and if yes, ask for their phone number and store it in the text file.
"""

# import the modules to use it functions
import math
import datetime

# open the file in append mode to preserve previous tire volume calculations
with open("volumes.txt", "at") as file:
    # Today date display
    todays_date = datetime.date.today()

    # Collect tire width
    width = float(input("Enter the width of the tire in mm (ex 205): "))

    # Collect aspect ratio
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))

    # Collect wheel diameter
    wheel_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate tire volume
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000

    # Display the result
    print(f"the approximate volume is {volume:.2f} liters.")

    # Ask whether the user wants to buy tires with these dimensions
    wants_to_buy = input("Would you like to buy tires with these dimensions? ")
    wants_to_buy = wants_to_buy.strip().lower()
    if wants_to_buy == "yes":
        phone_number = input("Enter your phone number: ")
        print(f"{todays_date}, {width}, {aspect_ratio}, {wheel_diameter}, "f"{volume:.2f}, {phone_number}", file=file,)
    else:
        print(f"{todays_date}, {width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}", file=file,)
