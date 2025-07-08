# Program using a conditional statement in the while loop
age = ''
while age != 'quit':
    prompt = 'What is your age'
    prompt += '\nEnter quit to exit. '
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3 :
            print('The ticket is free for you.')
        elif 3 <= age <= 12 :
            print('Your ticket is 10$')
        else:
            print('Your ticket costs 15$')



# Program using a flag
'''active = True
while active:
    prompt = 'What is your age'
    prompt += '\nEnter quit to exit. '
    age = input(prompt)
    if age == 'quit':
        active = False
    else: 
        age = int(age)
        if age < 3 :
            print('The ticket is free for you.')
        elif 3 <= age <= 12 :
            print('Your ticket is 10$')
        else:
            print('Your ticket costs 15$')

'''
# Program using break statement
'''while True:
    prompt = 'What is your age'
    prompt += '\nEnter quit to exit. '
    age = input(prompt)
    if age == 'quit':
        break
    else: 
        age = int(age)
        if age < 3 :
            print('The ticket is free for you.')
        elif 3 <= age <= 12 :
            print('Your ticket is 10$')
        else:
            print('Your ticket costs 15$')'''

