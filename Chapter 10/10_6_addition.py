""" 10-6. Addition: One common problem when prompting for numerical input 
occurs when people provide text instead of numbers. When you try to convert 
the input to an int, youll get a ValueError. Write a program that prompts for 
two numbers. Add them together and print the result. Catch the ValueError if 
either input value is not a number, and print a friendly error message. Test your 
program by entering two numbers and then by entering some text instead of a 
number."""

try:
    num1 = int(input("Enter first number - "))
    num2 = int(input("Enter second number - "))
except ValueError:
    print("Enter number only, nothing else.")
else:
    sum = num1 + num2
    print(f"Sum = {sum}")

    