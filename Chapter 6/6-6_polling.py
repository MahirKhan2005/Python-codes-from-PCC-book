favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
yet_to_poll = ['sarah','mahir','edward','subhan']
for name in yet_to_poll:
    if name in favorite_languages:
        print(f'Thank you {name.title()} for taking our poll.')
    else:
        print(f'{name.title()}, you should take our poll.')