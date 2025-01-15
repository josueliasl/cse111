import datetime

current_date = datetime.datetime.now(tz=None)

current_day = current_date.weekday()

#subtotal = float(input('Please enter the subtotal: '))

#First exercise

#if (current_day == 1 or current_day == 2) and subtotal >= 50 :
#discount_ten_percent = subtotal / 10
#discount_applied = subtotal - discount_ten_percent
#taxes_with_discount = discount_applied * 6/100
#discount_subtotal_plus_tax = discount_applied + taxes_with_discount
#new_total = discount_subtotal_plus_tax

#print(f'The sales tax amount is: {taxes_with_discount:.2f}')
#print(f'The total Amount is: {new_total:.2f}')


#else:
#tax_sales = subtotal * 6 /100
#total = subtotal + tax_sales

#print(f'The sales tax amount is: {tax_sales:.2f}')
#print(f"The total Amount is: {total:.2f}")

#Stretch 1

#if (current_day == 1 or current_day == 2) and subtotal >= 50 :
#discount_ten_percent = subtotal / 10
#discount_applied = subtotal - discount_ten_percent
#taxes_with_discount = discount_applied * 6/100
#discount_subtotal_plus_tax = discount_applied + taxes_with_discount
#new_total = discount_subtotal_plus_tax
#print(f'The sales tax amount is: {taxes_with_discount:.2f}')
#print(f'The total Amount is: {new_total:.2f}')


#elif subtotal < 50:
#less_subtotal = subtotal
#missing = 50 - less_subtotal
#tax_sales = subtotal * 6 /100
#total = subtotal + tax_sales
#print(f'The sales tax amount is: {tax_sales:.2f}')
#print(f"The total Amount is: {total:.2f}")
#print(f'You would need to purchase at least: {missing}')

#else:
#tax_sales = subtotal * 6 /100
#total = subtotal + tax_sales

#print(f'The sales tax amount is: {tax_sales:.2f}')
#print(f"The total Amount is: {total:.2f}")


#Stretch 2

subtotal = 0
price = 1
while price !=0:

   price = float(input('What is the cost per unit of the items you are interested on? '))
   quantity = int(input('How many of this products do you want? '))
   subtotal += price * quantity

if (current_day == 1 or current_day == 2) and subtotal >= 50 :
        discount_ten_percent = subtotal / 10
        discount_applied = subtotal - discount_ten_percent
        taxes_with_discount = discount_applied * 6/100
        discount_subtotal_plus_tax = discount_applied + taxes_with_discount
        new_total = discount_subtotal_plus_tax
        print(f'The sales tax amount is: {taxes_with_discount:.2f}')
        print(f'The total Amount is: {new_total:.2f}')


elif subtotal < 50:
        less_subtotal = subtotal
        missing = 50 - less_subtotal
        tax_sales = subtotal * 6 /100
        total = subtotal + tax_sales
        print(f'The sales tax amount is: {tax_sales:.2f}')
        print(f"The total Amount is: {total:.2f}")
        print(f'You would need to purchase at least: {missing}')
else: 
    print('')
