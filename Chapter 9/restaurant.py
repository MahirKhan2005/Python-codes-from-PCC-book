"""Contains restaurant class, used in question 9-10"""
class Restaurant:
    
    def __init__(self,name,cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        print(f"Our restaurant name is {self.restaurant_name.title()}")
        print(f"Our restaurant serves {self.cuisine_type.title()} cuisine")
    
    def open_restaurant(self):
        print(f"The restaurant is now open.")