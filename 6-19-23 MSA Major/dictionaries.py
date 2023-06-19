#create a dictionary of names and scores
#when you see {} you should automatically assume it will be a dictionary
#When you see [] you should automatically assume it will be a list
#dictionary = a named index rather than a list which = a numerical index
student_scores = {"Alice": 87, "Bob":79, 'Jerry':94, 'Sara': 90}

#Print Bob's score
print(student_scores['Bob'])
print(student_scores['Sara'])

#decalre a car dictionary 
car = {'make': "Mercury", 'model': "Sable", 'year':1998, "value":10000, "engine":3.0}

#Get all the keys, values from the students score dictionary
print('\n')
for student in student_scores:
    print(f'{student}: {student_scores[student]}')

#get all the keys and values from the cars dictionary
print('\n')
for key, value in car.items():
    print(f'{key}; {value}')
    
