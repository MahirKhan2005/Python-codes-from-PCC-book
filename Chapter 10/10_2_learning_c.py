"""10-2. Learning C: You can use the replace() method to replace any word in a 
string with a different word.
Read in each line from the file you just created, learning_python.txt, and 
replace the word Python with the name of another language, such as C. Print 
each modified line to the screen."""

with open('learning_python.txt') as file:
    for line in file:
        line = line.replace('Python','C')
        print(line.rstrip())

    # Can be done like this as well
    # for line in file:
    #     print(line.replace('Python','C').strip())