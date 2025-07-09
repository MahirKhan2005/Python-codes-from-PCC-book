""" 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two 
attributes individually, and then call both methods."""

class Restaurant:
    
    def __init__(self,name,cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        print(f"Our restaurant name is {self.restaurant_name.title()}")
        print(f"Our restaurant serves {self.cuisine_type.title()} cuisine")
    
    def open_restaurant(self):
        print(f"The restaurant is now open.")

firdous = Restaurant('firdous','indian')
firdous.describe_restaurant()
firdous.open_restaurant()