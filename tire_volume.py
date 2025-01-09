import math

tire_width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio_tire = float(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter_inches = float(input('Enter the diameter of the wheel in inches (ex 15): '))

using_pi = math.pi * (tire_width ** 2) * aspect_ratio_tire
using_constant = tire_width * aspect_ratio_tire + 2540 * wheel_diameter_inches
nummerator_multiplying = using_pi *using_constant
denominator = 10000000000
division = nummerator_multiplying / denominator
division=round(division, 2)
print(f'The approximate volume is {division} liters')

from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
# Use an f-string to print only the date
# part of the current date and time.
print(f"{current_date_and_time:%Y-%m-%d}")

open(volumes.txt, mode="rt")





