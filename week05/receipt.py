
import csv
def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  try: 
    with open(filename, "r") as csvfile:
       reader = csv.reader(csvfile)
       next(reader)
       products = {}
        
       for row in reader:
            product_number = row[key_column_index]
            product_name = row[1]
            price = float(row[2])
            products[product_number] = [product_number, product_name, price]
       return products 
  except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
        exit()

def main():
 try:  
   reading_dictionary = read_dictionary('products.csv', 0)
   print(f'Inkom Emporium')
   from datetime import datetime
   current_date_and_time = datetime.now()
   with open('request.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    total_items = 0
    total_subtotal = 0
    sales_tax_rate = 0.06
    for row in reader:
       product_number = row[0]
       quantity = int(row[1])
       try:
           product_info = reading_dictionary[product_number]
           total_items += quantity

           price = product_info[2]
           if product_number == 'D083' and quantity > 1:
                        
                        full_price_items = 1  
                        discounted_items = quantity - full_price_items  
                        discount_price = price * 0.5 

                        
                        total_subtotal += full_price_items * price
                        total_subtotal += discounted_items * discount_price

                        print(f'{product_info[1]}: {quantity} @ {price} each - Price with discount: {full_price_items * price} + {discounted_items} @ {discount_price} each')
           else:      
              total_subtotal += price * quantity      
              print(f'{product_info[1]}: {quantity} @ {product_info[2]}')
       except KeyError: 
           print(f'Error unknown product ID "{product_number}" in the request .CSV file')
           continue
    sales_tax = total_subtotal * sales_tax_rate
    total = total_subtotal + sales_tax
    print(f'Number of Items: {total_items}')
    print(f'Subtotal: {total_subtotal:.2f}')
    print(f'Taxes: {sales_tax:.2f}')
    print(f'Total: {total:.2f}')
    print('Thank you for shopping at the Inkom Emporium')
    print(f'Date and Time: {current_date_and_time:%Y-%m-%d %A %I:%M %p}')
 except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
        exit()
if __name__ == "__main__":
    main()