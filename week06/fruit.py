def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(f"Reversed: {fruit_list}")
  fruit_list.append("orange")
  print(f"Append orange: {fruit_list}")
  fruit_list.insert(1, "cherry")
  print(f"Insert cherry: {fruit_list}")
  fruit_list.remove("banana")
  print(f"Remove Banana: {fruit_list}")
  fruit_list.pop(4)
  print(f"Pop orange: {fruit_list}")
  fruit_list.sort()
  print(f"Sorted: {fruit_list}")
  fruit_list.clear()
  print(f"Cleared: {fruit_list}")


if __name__ == "__main__":
    main()