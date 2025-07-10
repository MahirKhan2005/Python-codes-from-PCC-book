"""10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
so the user can continue entering numbers even if they make a mistake and 
enter text instead of a number."""
print("Enter numbers and I'll add them.")
print("Enter 'q' to quit.")
sum = 0
while(True):
    num = input("Enter a number - ")
    try:    
        if num=='q':
            break
        else:
            num = int(num)
            sum+=num
    except ValueError:
        continue

print(f"Sum = {sum}")