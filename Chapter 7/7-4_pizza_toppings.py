while True:
    prompt = 'What kind of topping would you like on your pizza '
    prompt += '\nEnter quit to exit. '
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:    
        print(f"We'll add {toppings} on your pizza.")

