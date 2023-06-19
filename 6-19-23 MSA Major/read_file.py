#Reading files in python
#open the file
data_file = open('file.txt', 'r')

#create an empty dictionary
menu_items = {}

#loop through data in the file
for line_of_data in data_file:
    #what we need to do to each line of data
    #split line of data at the ', '
    keys_values = line_of_data.split(', ')

    #create an entry to the dictionary. Remeber to convert price to float
    menu_items[keys_values[0]] = float(keys_values[1])

    #OR
    #key = keys_values[0]
    #value = float(keys_values[1])

#close file
data_file.close()

#you can not forget .items()
for item, price in menu_items.items():
    print(f'{item}: ${price:.2f}')