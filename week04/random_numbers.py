import random

def append_random_numbers(number_list, quantity = 1):
    print(f"Appending {quantity} random numbers.") 
    for _ in range(quantity):
        number = random.uniform(0.0, 100.0)
        q = round(number, 1)
        
        number_list.append(q)

def main():
    numbers_list = [16.2, 75.1, 52.3]
    print(numbers_list)
    append_random_numbers(numbers_list)
    print(numbers_list)
    append_random_numbers(numbers_list, 3)
    print(numbers_list)


if __name__ == "__main__":
     main()