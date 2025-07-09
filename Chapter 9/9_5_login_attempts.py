"""9-5. Login Attempts: Add an attribute called login_attempts to your User 
class from Exercise 9-3 (page 162). Write a method called increment_login 
_attempts() that increments the value of login_attempts by 1. Write another 
method called reset_login_attempts() that resets the value of login_attempts 
to 0.
Make an instance of the User class and call increment_login_attempts() 
several times. Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts(). Print login_attempts again to 
make sure it was reset to 0."""

class User:
    
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 1
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

new_user = User('mahir','khan',19)
print(f"Initial login attempts : {new_user.login_attempts}\n")

# Increment login attempts 5 times
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

print(f"Revised login attempts : {new_user.login_attempts}\n")

new_user.reset_login_attempts()
print(f"Login attempts after reset : {new_user.login_attempts}")
