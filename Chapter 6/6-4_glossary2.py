glossary = {
    "variable": "A reserved memory location to store values.",
    "function": "A block of reusable code that performs a specific task.",
    "loop": "A control structure that repeats a block of code while a condition is true.",
    "dictionary": "A collection of key-value pairs in Python.",
    "list": "An ordered collection of items that can be of different types.",
    "tuple": "An immutable sequence of items.",
    "set": "An unordered collection of unique items.",
    "if-else": "A conditional statement used to execute code based on a condition.",
    "class": "A blueprint for creating user-defined objects.",
    "module": "A file containing Python code that can be imported and reused."
}

for word, meaning in glossary.items():
    print(f'{word.title()} - \n\t{meaning}')