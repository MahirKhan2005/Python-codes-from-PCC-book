pet1 = {'cat' : 'mahir'}
pet2 = {'parrot' : 'rose'}
pet3 = {'rabbit' : 'subhan'}
pet4 = {'horse' : 'arhaan'}
pets = [pet1,pet2,pet3,pet4]
for pet in pets:
    for animal,owners_name in pet.items():
        print(f'{animal.title()} - {owners_name.title()}')
    