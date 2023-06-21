
#for multiple words in a class you can use sanke case or camel case
class Automobile():
    #Define a constructor.
    #The constructior defines what happens when you create an automobile
    #whenever we create an object this function is called
    def __init__(self, make, model, vin, engine_size, owner):
        #assign parameter values
        #we are defineing what an automobile looks like
        #the self.____
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
