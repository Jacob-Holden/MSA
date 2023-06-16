#Prompt the user to enter a math expression in the format X y Z where y is a math operator (+, _, *, /)
"Expression: "
#Parse the expression to determine which operation to carry out and the value of the numbers
#Output the answer to the expression

#prompt the user for the experssion
#split the expression into: x, y, and z
    #use .split() to get the parts of the expression. Split the space
#get values from list
#determine the operation type to carry out. Using if/elif/else statements
#run the expression and print the answer(output) formated to one decimal place
# instead of .startswith, use == or is in this case
#ask the user if they want to continue. If y, continue. if n, end (THIS IS AFTER THE USER USES THE PROGRAM)

# if you want to do something multiple times, use a loop structure 
    #for loop - you know how many times you want it to run
    #while loop - conditonal (till a condition is met it moves on), do not know how many times the loop is going to go
# for string methods you MUST have to parentheses for it to function


'''
expression = (input('Enter your expression: '))
expression_part = expression.split(' ')
x = float(expression_part[0])
y = expression_part[1]
z = float(expression_part[2])
 
if expression_part[1] =='+':
    answer = (x+z)
    print(f'The answer to {x} + {z} = {answer:.1f}')
elif expression_part[1] == '-':
    answer = (x-z)
    print(f'The answer to {x} - {z} = {answer:.1f}')
elif expression_part[1]=='*':
    answer = (x*z)
    print(f'The answer to {x} * {z} = {answer:.1f}')
elif expression_part[1] == '/':
    answer = (x/z)
    print(f'The answer to {x} / {z} = {answer:.1f}')
'''
#Improved version


#ask the user if they want to continue. If y, continue. if n, end (THIS IS AFTER THE USER USES THE PROGRAM)
#problems
    #incorrect operator format
    #X or Z are not numbers 
    #user may input an incorrect expression, has more than 3 parts
# if you want your program to make a decision, use an if statement
    
def main():
    while True:
        while True:
            expression = (input('Enter your expression: '))
            expression_part = expression.split(' ')
            
            number_of_parts = len(expression_part)
            if number_of_parts != 3:
                print('Error: Please enter a valid expression ( X Y Z format)\n')
                continue
            try: 
                x = float(expression_part[0])
                z = float(expression_part[2])
            except ValueError:
                print('Erorr: X and Z must be numbers. (X Y Z)\n ')
                continue

            y = expression_part[1]
            #test for the correct operator value
            if y not in ['+', '-', '*', '/']:
                print('Error: incorrect operator, Only (+, -, *, /) allowed.\n')
                continue
            break
        
        if expression_part[1] =='+':
            answer = (x+z)
            print(f'The answer to {x} + {z} = {answer:.1f}')
        elif expression_part[1] == '-':
            answer = (x-z)
            print(f'The answer to {x} - {z} = {answer:.1f}')
        elif expression_part[1]=='*':
            answer = (x*z)
            print(f'The answer to {x} * {z} = {answer:.1f}')
        elif expression_part[1] == '/':
            answer = (x/z)
            print(f'The answer to {x} / {z} = {answer:.1f}')
        else:
            print('Please enter a correct expression')
            continue

        #ask the user if they want to continue
        another_calculation = input('Would you like to evalulate another expression? (y/n):').lower()
        if another_calculation == 'n':
            break
        elif another_calculation == 'y':
            main()
main()

'''
#Kristofferson's example
def main():
    while True:
        while True:
            expression = input('Enter your expression: ')
            expression_part = expression.split(' ')

            if len(expression_part) !=3:
                print('Error: Enter Expression in (X Y Z) format\n')
                 continue
           try: 
                x = float(expression_part[0])
                z = float(expression_part[2])
            except ValueError:
                print('Erorr: X and Z must be numbers. (X Y Z)\n ')
                continue
            y = expression_part[1]

            #test for the correct operator value
            if y not in ['+', '-', '*', '/']:
                print('Error: incorrect operator, Only (+, -, *, /) allowed.\n')
                continue
            break
                
        if y is '+':
            answer = x + z
        elif y == '-':
            answer = x - z
        elif y is '*':
            answer = x * z
        elif y == '/':
            answer = x / z
        
        print(f'{answer:.1f}')

        another_calculation = input('Would you like to evalulate another expression? Press y to continue or any other key exsit:').lower()
        if another_calculation != 'y':
            break
main()

'''




