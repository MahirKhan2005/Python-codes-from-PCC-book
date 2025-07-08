person1 = {
    "first_name" : 'mahir',
    'last_name' : 'khan',
    'age' : '18',
    'city' : 'kota',
}
person2 = {
    "first_name" : 'subhan',
    'last_name' : 'khan',
    'age' : '12',
    'city' : 'kota',
}
person3 = {
    "first_name" : 'arhaan',
    'last_name' : 'ansari',
    'age' : '12',
    'city' : 'kota',
}
people = [person1,person2,person3]
for person in people:
    print('')
    for key, info in person.items():
        print(f'{key.title()} - {info.title()}')