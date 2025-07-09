"""9-7. Admin: An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator's set of 
privileges. Create an instance of Admin, and call your method."""

class User:
    
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Admin(User):

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges of the Admin - ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

new_admin = Admin('mahir','khan',19)
new_admin.show_privileges()