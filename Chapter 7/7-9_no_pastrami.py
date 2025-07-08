sandwich_orders = ['chicken', 'pastrami','cheese','pastrami', 'paneer','pastrami']
finished_sandwiches = []

while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        sandwich = sandwich_orders.pop()
        print(f'I made your {sandwich} sandwich.')
        finished_sandwiches.append(sandwich)

print('These are the sandwiches I made - ')
for sandwich in finished_sandwiches:
    print(sandwich.title())
