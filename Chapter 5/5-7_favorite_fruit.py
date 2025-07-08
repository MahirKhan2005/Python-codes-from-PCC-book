favorite_fruits = ['mango','pineapple','orange']
favorite_fruits_check = ['mango','apple','pineapple','peach','orange']
for fruit in favorite_fruits_check:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}s!")