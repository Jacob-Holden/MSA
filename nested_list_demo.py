# create a list
demo_list =[15, 8, 64, 25, 9, 11, 32, 41]

# you can have a matrix of data
# matrix dimentions 3 x 4 
list_of_lists = [[2, 4, 7, 9], 
                 [3, 7, 8, 4], 
                 [1, 8, 5, 2]]

#get data from lists
print(demo_list[2])

#print the 8 in lists_of_list
#first [] is the line of the matrix, the second [] is the number in that line
print(list_of_lists[1][2])

#print all the values in my lists_of_list matrix
for number in demo_list:
    print(number)

print('\n')
#iterate over the rows 
for row in range(len(list_of_lists)):
    #iterate over the columns
    # added 1 to the row value to make it better for the user to understand
    
    print(f'\nRow {row +1} Values')
    for columns in range(len(list_of_lists[row])):
        print(list_of_lists[row][columns])





