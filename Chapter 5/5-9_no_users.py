usernames = []
if usernames:
    for name in usernames:
        if name.lower() == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again.")
else:
    print('We need to find some users!')