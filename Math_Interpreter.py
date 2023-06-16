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

