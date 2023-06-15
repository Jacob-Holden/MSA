my_name= "jaocb"
#Capitalize method
print(my_name.capitalize())
        #this will capitalize the first letter of the variable
print("\n")

#Upper method
print(my_name.upper())
#this will make every letter uppercase
print("\n")

    #Starwith method
print(my_name.startswith("jac"))
print("\n")

    #Endwith method
print(my_name.endswith("ob"))
print("\n")

#Find method
print(my_name.find("b"))
print("\n")

sentence = "I have a dog. My dog is cute. Do you want a dog."

#loop through a string
for letter in my_name:
    print(letter)

#These strings do the same thing (in this situation)
    print("\n")
    #get the length of the string
    length_of_string = len(my_name)
    #loop throught the string
        #[] represent the index value (start at 0-till the last value)
    for index in range(length_of_string):
        print(my_name[index])


print("\n")
sentence = "I have a dog. My dog is cute. Do you want a dog."

dog_count = 0

#loop
more_dogs = True
start_index = 0
while more_dogs:
    #find the first instance of dog
    found_index = sentence.find("dog", start_index)
    if found_index != -1:
        #increment dog_count by 1, #dog_count = dog_count + 1 
        dog_count += 1
        #update index to the character after dog
        start_index = found_index +1
    else: 
        more_dogs=False

print(f"Number of dogs: {dog_count}")

more_dogs = True
start_index = 0
while more_dogs:
    found_index = sentence.find("dog", start_index)
    if found_index != -1:
         dog_count += 1
         start_index = found_index +1
    else: 
        more_dogs=False

print(f"Number of dogs: {dog_count}")