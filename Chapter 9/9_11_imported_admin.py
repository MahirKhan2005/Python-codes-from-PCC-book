"""9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). 
Store the classes User, Privileges, and Admin in one module. Create a sepa
rate file, make an Admin instance, and call show_privileges() to show that 
everything is working correctly."""

from user_admin import Admin

new_admin = Admin('mahir','khan',19)
new_admin.privileges.show_privileges()
