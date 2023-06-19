#List demo
names = ['John', 'Mary', 'Alice', 'Bob']
demo_list = [10, 16, 24, 77, 2, 14, 9]

#add values to the list
#.append() is a string method
demo_list.append(5)
demo_list.append(63)

#removing numbers from the list
#.remove() is a string method
#       demo_list.remove(16)

#showing the demo list
print(demo_list)
print('\n')

#get number of items in list 
#len is a function in the python standard library not a string method
number_of_items = len(demo_list)
print(f'Number of items: {number_of_items}')
print('\n')
#get the first value from the list
print(demo_list[0])
print('\n')

#EX: get the fourth value from the list
print(demo_list[3])

#get the tenth value from the list (we do not have a tenth value)
#could make an except clause a list out of range
#print(demo_list[9])

#print all items in the list
print('\n')
# in this case you can use a for-loop
# the item variable is defined in the loop heeader so it will store the value of each number in the lis one at a time
#give variables meaningful names
# all three of these have the same output

for item in demo_list:
    print(item)
print('\n')

for index in range(number_of_items):
    print(demo_list[index])
print('\n')

for index in range(len(demo_list)):
    print(demo_list[index])
print('\n')

#print items at even indexes
print('\n')
for index in range (0, number_of_items, 2):
    print(demo_list[index])

print('\n')

#print items at odd indexes
for index in range(1, number_of_items, 2):
    print(demo_list[index])