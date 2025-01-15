import math
items_number = int(input('Enter the number of items: '))
items_number_per_box = int(input('Enter the number of items per box: '))

number_of_boxes = math.ceil(items_number / items_number_per_box)
r=round(number_of_boxes)

print(f'For {items_number} items, packing {items_number_per_box} items in each box, you will need {r} boxes.')