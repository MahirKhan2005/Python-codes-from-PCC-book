"""9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
Add an attribute called number_served with a default value of 0. Create an 
instance called restaurant from this class. Print the number of customers the 
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number 
of customers that have been served. Call this method with a new number and 
print the value again.
Add a method called increment_number_served() that lets you increment 
the number of customers who’ve been served. Call this method with any num
ber you like that could represent how many customers were served in, say, a 
day of business."""

class Restaurant:
    def __init__(self,name,cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0
    
    def set_number_served(self,servings):
        self.number_served = servings
    
    def increment_number_served(self,increment):
        self.number_served+=increment

restaurant = Restaurant('firdous','indian')
print(f"Initial servings - {restaurant.number_served}\n")

restaurant.number_served = 20
print(f"New servings - {restaurant.number_served}\n")

restaurant.set_number_served(50)
print(f"Changed servings through method - {restaurant.number_served}\n")

restaurant.increment_number_served(50)
print(f"Servings after increment - {restaurant.number_served}")