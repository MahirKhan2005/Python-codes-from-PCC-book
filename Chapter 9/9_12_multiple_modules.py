""" 9-12. Multiple Modules: Store the User class in one module, and store the 
Privileges and Admin classes in a separate module. In a separate file, create 
an Admin instance and call show_privileges() to show that everything is still 
working correctly."""

from admin import Admin

new_admin = Admin('mahir','khan',19)
new_admin.privileges.show_privileges()
