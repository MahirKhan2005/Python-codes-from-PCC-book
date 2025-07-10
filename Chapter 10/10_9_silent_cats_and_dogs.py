""" 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail 
silently if either file is missing."""

files = ['dogs.txt','cats.txt']
for file in files:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)