import math

# collect user input for number of items and number of items per box
number_of_items = int(input("Enter the number of items: "))
number_of_items_per_box = int(input("Enter the number of items per box: "))

# calculate the number of boxes needed
number_of_boxes = math.ceil(number_of_items / number_of_items_per_box)

# display the result
print(f"For {number_of_items} items, packing {number_of_items_per_box} items in each box, you will need {number_of_boxes} boxes.")