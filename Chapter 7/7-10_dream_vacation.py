"""7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where 
would you go? Include a block of code that prints the results of the poll."""

poll = {}
while True:
    name = input('What is your name? ')
    place = input('If you could visit one place in the world, where would you go? ')
    poll[name] = place
    exit = input('Do you want another person to take the poll(y or n)? ')
    if exit == 'n':
        break
print("Results of the poll ---")
for name,place in poll.items():
    print(f'\t{name.title()} wants to go to {place.title()}')