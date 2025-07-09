"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance."""

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
maheshwari = Restaurant('maheshwari','indian')
asli_zaika = Restaurant('asli zaika','indian')

firdous.describe_restaurant() 
maheshwari.describe_restaurant()
asli_zaika.describe_restaurant()