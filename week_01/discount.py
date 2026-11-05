"""
Author: Augustine Okpe Oche
purpose: This program calculates the discount, sales tax, and total amount due based on the subtotal and the day of the week.

"""

# import module so it function can be use
from datetime import datetime

tuesday = 1
wednesday = 2
discount_rate = 0.10
sales_tax_rate = 0.06
subtotal = 0

print()
# continuesly ask user for the price and quantity until quantity is 0
print("Enter the price and quantity of items. Enter 0 in quantity to continue.")
print("with the weekday discount check, sales tax calculation, and final total.")
print()
while True:
    price = float(input("Enter the price per item: "))
    quantity = int(input("Enter the quantity: "))

    if quantity == 0:
        break

    subtotal += price * quantity

# get the day of the week
current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

# compute and print the discount amount
if weekday == tuesday or weekday == wednesday:
    if subtotal >= 50:
        discount = subtotal * discount_rate
        subtotal = subtotal - discount
        print(f"Discount amount: ${discount:.2f}")
    else:
        difference = 50 - subtotal
        print(
            f"Discount not applied. You need to spend ${difference:.2f} more to qualify for the discount."
        )
else:
    print(
        "No discount applied today. discount are only applied on tuesday or wednesday."
    )

# compute and print the sales tax amount
sales_tax = subtotal * sales_tax_rate
print(f"Sales tax amount: ${sales_tax:.2f}")

# compute and print the total amount due
total = subtotal + sales_tax
print(f"Total amount due: ${total:.2f}")
