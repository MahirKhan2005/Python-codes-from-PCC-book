fav_nums = {
    'mahir' : [7],
    'rose' : [10],
    'subhan' :[20],
    'arhaan' : [3,5,8],
    'haider' : [9,40],
}
for key,value in fav_nums.items():
    print(f'{key.title()} - ')
    for num in value:
        print(f'\t{num}')