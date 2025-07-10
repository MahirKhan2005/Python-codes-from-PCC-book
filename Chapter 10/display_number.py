"""Used for question 10-11"""

import json

with open('favourite_number.txt') as f:
    fav_num = json.load(f)
print(f"I know your favorite number! It's {fav_num}")