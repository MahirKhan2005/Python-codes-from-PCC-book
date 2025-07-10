"""10-4. Guest Book: Write a while loop that prompts users for their name. When 
they enter their name, print a greeting to the screen and add a line recording 
their visit in a file called guest_book.txt. Make sure each entry appears on a 
new line in the file."""

active=True
while(active):
    response = input("Wanna take part in the poll (y or n) - ")
    if response == 'y':
        name = input('Enter your name - ')
        with open('guest_book.txt','a') as file:
            file.write(f"{name.title()}\n")
    elif response=='n':
        active = False
    else:
        print("Wrong response. Quitting...")
        active = False
