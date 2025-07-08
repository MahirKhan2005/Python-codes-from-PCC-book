sandwich_orders = ['chicken', 'cheese', 'paneer']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)
print('These are the sandwiches I made - ')
for sandwich in finished_sandwiches:
    print(sandwich.title())
