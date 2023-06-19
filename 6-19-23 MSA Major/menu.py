'''
In a program called menu.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user types the word "end". After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Ignore any input that is not an item. You should create the menu as a dictionary.

Prompt user for an item
Display the total cost of all items inputted prefixed with a dollar sign ($) formatted to two decimal places
Ignore any input that is not an item. The case will matter; for example "Taco" is a valid key but "taco" is not. So the user must enter the item as it is stored in the dictionary
End the program when user types "end". Case should not matter. If the user types "end", "END", "End", "eND"...etc the program should still end.
Create the menu as a dictionary.
'''

menu_items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
total = 0

for item in menu_items:
    print(f'{item}: {menu_items[item]:.2f}')


while True:
    items_selected = input("What item would you like:")
    if items_selected in menu_items.keys():
        total = menu_items[items_selected] + total
    elif items_selected.lower() == "end":
        break
    try:
        total += menu_items[item.title()]
    except:
        continue
    print(f'Total: ${total:.2f}')

'''
#Kristofferson's Example

def main():

    menu_items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
    
    total = 0
    while True:
        #prompt the user of a menu item
        item = input('Item: ')
        
        #determine if we need to end the program
        if item.lower() == 'end':
            break

        #determine the ordered item and add the total. If item not in the dictionary then reprompt user
        try: 
            total += menu_items[item.title()]

        except:
            continue

#display order total
        print(f'Total: ${total:.2f}')
main()
'''

    
