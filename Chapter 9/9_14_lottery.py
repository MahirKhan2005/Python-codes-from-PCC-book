""" 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
five letters. Randomly select four numbers or letters from the list and print a 
message saying that any ticket matching these four numbers or letters wins a 
prize."""

from random import choice

#Lottery generator
numbers_characters = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d']
first = choice(numbers_characters)
second = choice(numbers_characters)
third = choice(numbers_characters)
fourth = choice(numbers_characters)
ticket = f"{first}{second}{third}{fourth}"

#Prints the lottery
print(f"Any ticket matching these four numbers or letters wins a prize - {ticket}")

