""" 9-3. Users: Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user."""

class User:
    
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        print(f"First name : {self.first_name.title()}\nLast name : {self.last_name.title()}\nAge : {self.age}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}\n")

mahir = User('mahir','khan',19)
ameen = User('mohd','ameen',20)
manthan = User('manthan','kumar',18)

mahir.describe_user()
mahir.greet_user()

ameen.describe_user()
ameen.greet_user()

manthan.describe_user()
manthan.greet_user()

