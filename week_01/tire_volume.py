"""
Author: Augustine Okpe Oche
Purpose: Calculate the volume of a tire
"""

#import the math module to use mathematical functions
import math

# Collect tire width
width = float(input("Enter the width of the tire in mm (ex 205): "))

# Collect aspect ratio
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))

# Collect wheel diameter
wheel_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate tire volume
volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000

# Display the result
print(f"The approximate volume of the tire is {volume:.2f} liters.")