"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

constant_number = 220
user_age = int(input('Please enter your age: '))
mhr = constant_number - user_age
lower_bound = 0.65 * mhr
upper_bound = 0.85 * mhr
print(f"""When you exercise to strengthen your heart, you should 
      keep your heart rate between {lower_bound:.2f} and {upper_bound:.2f} beats per minute.""")
