import datetime
class Automobile():
    #3 principles of OOP (Object-oriented-programming)
        #1. Polymorphism
        #2. Inheritance
        #3 Encapsulation
    #Define a constructor.
    #The constructor  defines what happen when we create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year):
        #assign parameter values
        #__ makes the variable private (not avaiable for the public)
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year

#create Getter and Setter methods for class attributes
# these are methods
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_vin(self):
        return self.__vin
    def get_engine_size(self):
        return self.__engine_size
    def set_engine_size(self, new_size):
        self.__engine_size = new_size
    def get_owner(self):
        return self.__owner
    def set_owner(self, new_owner):
        self.__owner = new_owner
    def get_year(self):
        return self.__year
    #get Automobile age
    def get_age(self):
        #get the current year
        the_date = datetime.datetime.now()
        # .year is a property, or method no () needed
        this_year = the_date.year
        #return the difference between the current year and auto year as the age
        return this_year - self.__year
    
#create a method tp print Automobile data
#methods and functions are functionally the same 
    def print_data(self):
        print(f'{self.__year} {self.__make} {self.__model}')
        print(f'vin: {self.__vin}, engine size: {self.__engine_size}')
        print(f'Owner: {self.__owner}\n')