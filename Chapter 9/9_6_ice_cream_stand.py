"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method."""

class Restaurant:
    
    def __init__(self,name,cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

class IceCreamStand(Restaurant):

    def __init__(self,name,cuisine,flavors):
        super().__init__(name,cuisine)
        self.flavors = flavors
    
    def display_flavors(self):
        print("Available Flavors - ")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")

new_stand = IceCreamStand('thela','ice cream', ['mango','chocolate','vanilla','strawberry'])

new_stand.display_flavors()