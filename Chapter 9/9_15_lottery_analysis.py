"""9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
Write a loop that keeps pulling numbers until your ticket wins. Print a message 
reporting how many times the loop had to run to give you a winning ticket."""

from random import choice

#Lottery generator
def ticket_generator():
    numbers_characters = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d']

    first = choice(numbers_characters)
    second = choice(numbers_characters)
    third = choice(numbers_characters)
    fourth = choice(numbers_characters)
    ticket = f"{first}{second}{third}{fourth}"
    return ticket


#Prints the lottery
lottery = ticket_generator()
print(f"Any ticket matching these four numbers or letters wins a prize - {lottery}")

#Checks how many times the loop had to run to match my ticket to lottery
initial_count = 1
while(True):
    my_ticket = ticket_generator()
    if lottery==my_ticket:
        print(f"Number of times the loop had to run to match my ticket to lottery - {initial_count}")
        break
    initial_count+=1

