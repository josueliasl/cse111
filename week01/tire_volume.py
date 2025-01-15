import math

tire_width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio_tire = float(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter_inches = float(input('Enter the diameter of the wheel in inches (ex 15): '))

using_pi = math.pi * (tire_width ** 2) * aspect_ratio_tire
using_constant = tire_width * aspect_ratio_tire + 2540 * wheel_diameter_inches
nummerator_multiplying = using_pi * using_constant
denominator = 10000000000
division = nummerator_multiplying / denominator
division=round(division, 2)
print(f'The approximate volume is {division} liters')

if tire_width >= 450:
    print("The cost of your tire is $85")
    will_you_buy_it = input('Do you want to buy tires with these dimensions? (yes/no):')
    if will_you_buy_it == 'yes':
        client_phone_number = input('Please type your phone number: ')
        print('Thank you we will soon contact you!')
    else:
        print('Thank you for your interest')
        client_phone_number ='None'

elif aspect_ratio_tire >20 and tire_width <=240:
    print('The cost of your tire is $95')
    will_you_buy_it = input('Do you want to buy tires with these dimensions? (yes/no):')
    if will_you_buy_it == 'yes':
        client_phone_number = input('Please type your phone number: ')
        print('Thank you we will soon contact you!')
    else:
        print('Thank you for your interest')
        client_phone_number ='None'

elif wheel_diameter_inches >60 and tire_width >=150:
    print('The cost of your tire is $60') 
    will_you_buy_it = input('Do you want to buy tires with these dimensions? (yes/no):')
    if will_you_buy_it == 'yes':
        client_phone_number = input('Please type your phone number: ')
        print('Thank you we will soon contact you!')
    else:
        print('Thank you for your interest')
        client_phone_number ='None'

if wheel_diameter_inches <= 14:
    print('The cost of your tire is $40')
    will_you_buy_it = input('Do you want to buy tires with these dimensions? (yes/no):')
    if will_you_buy_it == 'yes':
        client_phone_number = input('Please type your phone number: ')
        print('Thank you we will soon contact you!')
    else:
        print('Thank you for your interest')
        client_phone_number ='None'

from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
# Use an f-string to print only the date
# part of the current date and time.

with open("volumes.txt", 'a') as my_file:
    my_file.write(f'{current_date_and_time:%Y-%m-%d}, {tire_width}, {aspect_ratio_tire}, {wheel_diameter_inches}, {division}     {client_phone_number}\n') 





