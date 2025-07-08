cities = {
    'kota' : {
        'country' : 'india',
        'population' : '100000',
        'fact' : 'coaching center of the country'
    },
    'delhi' : {
        'country' : 'india',
        'population' : '3049109',
        'fact' : 'capital of the country'
    },
    'jaipur' : {
        'country' : 'india',
        'population' : '789798',
        'fact' : 'pink city'
    }
}
for city,info in cities.items():
    print(f'{city.capitalize()} - ')
    for key,value in info.items():
        print(f'\t{key.title()} : {value.title()}')
    print('')