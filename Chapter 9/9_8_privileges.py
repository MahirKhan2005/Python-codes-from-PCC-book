""" 9-8. Privileges: Write a separate Privileges class. The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. Make a Privileges instance 
as an attribute in the Admin class. Create a new instance of Admin and use your 
method to show its privileges."""

class User:
    
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Privileges:
    
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print("Privileges of the Admin - ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()

new_admin = Admin('mahir','khan',19)
new_admin.privileges.show_privileges()
