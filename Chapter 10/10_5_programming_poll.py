"""10-5. Programming Poll: Write a while loop that asks people why they like 
programming. Each time someone enters a reason, add their reason to a file 
that stores all the responses."""


active=True
while(active):
    response = input("Wanna take part in the poll (y or n) - ")
    if response == 'y':
        reason = input('Why do you like programming?  ')
        with open('programming_poll.txt','a') as file:
            file.write(f"{reason.title()}\n")
    elif response=='n':
        active = False
    else:
        print("Wrong response. Quitting...")
        active = False
