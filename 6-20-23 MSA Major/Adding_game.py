#import random
#prompt user for level
#prompt for question amount
#define the funtcion to generate questions
#prompt the user to answer the question
#check answer
#if answer is wrong prompt user to reanswer up to 3 times, if they get it right break
#print how many they got right 
#ask them if they want to go again


import random

while True:
    level = int(input('Enter the level you would like to play (1, 2, or 3):'))
    if level in [1, 2, 3]:
        break
    else:
        print("Error: Invalid Input!"'\n')
        continue

while True:
    number_of_questions = int(input('Enter the number of question you would like to answer(3-10):'))
    if number_of_questions in [3, 4, 5, 6, 7, 8, 9, 10]:
        break
    else:
        print("Error: Please enter an integer value between 3 and 10")
        continue

def get_answer():
    b=1
    number1 = generate_number(x, y)
    number2 = generate_number(x, y)
    answer = number1 + number2
    for a in range(3):
        try:
            user_answer = int(input(f'{number1} + {number2} ='))
        except(ValueError):
            print('Error: Please enter a valid input')
            continue
        if answer == user_answer:
            wrong_answer = 0
            print('Correct, Good Job!')
            break
        elif b<= 2:
            print('Incorrect')
            b = b +1
            continue
        elif b ==3:
            print('Incorrect''\n')
            print(f'Correct Answer: {answer}''\n')
            wrong_answer = 1
            break
    return wrong_answer


def generate_number(x, y):
    number1 = random.randint(x, y)
    return number1

if level == 1:
    x = 0
    y = 9
    
elif level == 2:
    x = 10
    y = 99
    
elif level == 3:
    x = 100
    y = 999
        

def main():
    wrong_answer = 0
    for c in range(number_of_questions):
        amount_wrong = get_answer()
        wrong_answer = wrong_answer + amount_wrong
    amount_right = number_of_questions - wrong_answer
    percent_right = amount_right / number_of_questions * 100
    print(f' You got {amount_right} out of {number_of_questions} questions correct: {percent_right:.2f}%')

main()
