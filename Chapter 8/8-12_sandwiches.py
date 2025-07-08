def sandwiches(*items):
    """ Takes arbitrary number of items one wants on his sandwiches as arguments"""
    print(f'\nThe items you want on your sandwiche are - ')
    for item in items:
        print(f'\t - {item}')

sandwiches('cheese', 'mayo')
sandwiches('fries')
sandwiches('chicken', 'paneer', 'jalapeno')