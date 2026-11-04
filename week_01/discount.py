"""
Author: Augustine Okpe Oche
purpose: This program calculates the discount, sales tax, and total amount due based on the subtotal and the day of the week.

"""
# import module so it function can be use
from datetime import datetime
TUE = 1
WED = 2
discount_rate = 0.10
sales_tax_rate = 0.06

# ask user for the subtotal
subtotal = float(input("Enter the subtotal: "))

# get the day of the week
current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

# compute and print the discount amount
if weekday == TUE or weekday == WED:
    if subtotal >= 50:
        discount = subtotal * discount_rate
        subtotal = subtotal - discount
        print(f"Discount amount: ${discount:.2f}")


# compute and print the sales tax amount
sales_tax = subtotal * sales_tax_rate
print(f"Sales tax amount: ${sales_tax:.2f}")

# compute and print the total amount due
total = subtotal + sales_tax
print(f"Total amount due: ${total:.2f}")
