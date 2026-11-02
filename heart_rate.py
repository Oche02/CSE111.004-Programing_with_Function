"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# take user input for age
age = int(input("Please enter your age: "))

# calculate maximum heart rate
max_heart_rate = 220 - age

# calculate target heart rate range
min_target_rate = int(max_heart_rate * 0.65)
max_target_rate = int(max_heart_rate * 0.85)

print(f"When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {min_target_rate} and {max_target_rate}")
print("beats per minute.")