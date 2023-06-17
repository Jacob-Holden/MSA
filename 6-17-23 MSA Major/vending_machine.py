'''
A vending machine sells snacks for 50 cents. In a project named vending_machine.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. The user should only be able to input integers. Accepted denominations for coins are (1, 5, 10, 25). The program should ignore any integer that isn’t an accepted denomination.

Display the amount due
Prompt the user to enter a coin
Accepted denominations for coins are (1, 5, 10, 25)
Program should ignore any input that is not a valid input and re prompt the user to input a coin
Process the input and display the updated amount due
Once the user has inputted at least 50 cents, output how many cents in change the user is owed
End program
'''



print('Welcome to The Vending Machine! Everything we have is 50¢!')

def main1():

    amount_due = int(50)

    while True:
        print(f'Amount due: {amount_due}¢')
        try:
            cent_amount = int(input('Please insert a coin!''\n'))
        except(ValueError):
            continue
        if cent_amount not in [1, 5, 10, 25]:        
            continue
        else:
            amount_due = amount_due - cent_amount
        if amount_due<= 0:
            amount_due = amount_due * -1
            print(f'Amount owed: {amount_due}¢')
            break
main1()

'''
#kristofferson's example

def main():
    
    amount_due = 50

    while True:
        #display amount due
        print(f'Amount Due: {amount_due}')

        #prompt the user to enter a coin
        coin = input('Enter Coin:')

        #validate coin amount and repromt user if not valid value
        if coin not in ["1", '5', '10', '25']:
            continue

        #covert coin to integer
        coin = int(coin)

        #update amount due value, -= mean amount_due = amount_due - coin
        amount_due -= coin

        #check amount due and determin if user owes more
        #if amount due <= 0. break loop
        if amount_due <= 0:
            break
    
    print(f'Change Owed: {amount_due * -1}')
main()
'''
    # or

'''
def main2()

    amount_due = 50
    
    while amount_due > 0:
        #display amount due
        print(f'Amount Due: {amount_due}')

        #prompt the user to enter a coin
        coin = input('Enter Coin:')

        #validate coin amount and repromt user if not valid value
        if coin not in ["1", '5', '10', '25']:
            continue

        #covert coin to integer
        coin = int(coin)

        #update amount due value, -= mean amount_due = amount_due - coin
        amount_due -= coin

    print(f'change Owed: {amount_due*1}')
'''