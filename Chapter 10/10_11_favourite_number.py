"""10-11. Favorite Number: Write a program that prompts for the user’s favorite 
number. Use json.dump() to store this number in a file. Write a separate pro
gram that reads in this value and prints the message, “I know your favorite 
number! It's _____.”"""

import json

num = int(input("Enter you favourite number - "))
with open('favourite_number.txt','w') as f:
    json.dump(num,f)