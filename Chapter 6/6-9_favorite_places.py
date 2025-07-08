fav_places  = {
    'mahir' : ['mecca', 'new york', 'medina'],
    'rose' : ['london', 'italy'],
    'subhan' : ['delhi'],
    'arhaan' : ['france'],
}
for name, places in fav_places.items():
    print(f'{name.title()} - ')
    for place in places:
        print(f'\t{place.title()}')