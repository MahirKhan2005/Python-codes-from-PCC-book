pizzas = ['cheese','paneer','chicken']
friend_pizzas = pizzas[:]
pizzas.append('mutton')
friend_pizzas.append('pepperoni')

print("My favourite pizza are - ")
for pizza in pizzas:
    print(pizza.title())

print("My friend's fvourite pizzas are - ")
for pizza in friend_pizzas:
    print(pizza.title())