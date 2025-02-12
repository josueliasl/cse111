opening_file = open('provinces.txt', mode="rt")

reading = opening_file.readlines()
new_list = []
for _ in reading:
   listing = _.strip()
   new_list.append(listing)
new_list.pop(0)
new_list.pop()

for i, value in enumerate(new_list):
   if  value == 'AB':
      new_list [i]='Alberta'
counting = new_list.count('Alberta')
print(new_list)
print(f' Alberta appears {counting}')
opening_file.close()

