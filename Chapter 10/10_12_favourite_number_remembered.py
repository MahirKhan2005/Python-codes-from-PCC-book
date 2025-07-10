""" 10-12. Favorite Number Remembered: Combine the two programs from 
Exercise 10-11 into one file. If the number is already stored, report the favorite 
number to the user. If not, prompt for the user's favorite number and store it in a 
file. Run the program twice to see that it works."""

import json

try:
    with open('favourite_number.txt') as f:
        fav_num = json.load(f)
except FileNotFoundError:
    fav_num = int(input("Enter you favourite number - "))
    with open('favourite_number.txt','w') as f:
        json.dump(fav_num,f)
else:
    print(f"I know your favorite number! It's {fav_num} ")