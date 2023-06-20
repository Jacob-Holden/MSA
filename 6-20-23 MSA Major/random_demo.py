#import the random library
import random

#generate a random number
random_number = random.randint(0,10)

print(random_number)
#(returns a random integer between the a, start, and b, the stop value,)

#if you want to generte a series of random numbers you can use a for loop
#range(10) means that you are generating 10 numbers
for rand_number in range(10):
    print(random.randint(0, 100))