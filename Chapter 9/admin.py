"""Contains Privileges and admin class, used for question 9-12"""

from user import User

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