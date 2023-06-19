#prompt the user for name
#prompt the user for age
#take the age and add 100
#return the user their name 
#return the user their age 100 years in the future

def name():

    print(f'hello I am the age wizard' '\n' 'I take your age and add how ever much you want to add to it!''\n')
    name = input('But first, let me get to know you a little bit. What is your name?' '\n')
    print(f'Nice to meet you {name}!''\n')

    while True:
        choice = input('Now that I got to know you a little, are you ready to begin (type y if you are ready or any other key if you are not )').lower()
        if choice != "y":
            break
        else:
            age() 
name()

def age():
    print('Great let us being!')
    age = input(f'How old are you?')
    age = int(age)
    
    while True:
        ask = input(f'Are you {age} years old?').lower()
        if ask != 'y':
            break
        else:
            print(f'Ok let us continue!')
            

age()