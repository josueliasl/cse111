import csv
 
INDEX = 0
NAME = 1
def main():
   id_search = input("Please enter an I-Number (xxxxxxxxx): ")
   id_dict = read_dictionary("students.csv", INDEX)
   if id_search in id_dict:
       s_name = id_dict[id_search]
       print(s_name[NAME])
   
   else:
        print("No such student")
   
def read_dictionary(filename, key_column_index):
    List = {}
 
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                List[key] = row_list
    return List
 
if __name__ == "__main__":
    main()