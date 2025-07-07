guests = ['ameen','adeeb','aarish']
print(f"{guests[0].title()}! would you like to have dinner with us tonight?")
print(f"{guests[1].title()}! would you like to have dinner with us tonight?")
print(f"{guests[2].title()}! would you like to have dinner with us tonight?\n")

print(f"Unfortunately! Adeeb would not be able to come tonight.\n")
guests.remove('adeeb')
guests.append("rehan")
print(f"{guests[0].title()}! would you like to have dinner with us tonight?")
print(f"{guests[1].title()}! would you like to have dinner with us tonight?")
print(f"{guests[2].title()}! would you like to have dinner with us tonight?\n")

print("Congratulations! We found a bigger dinner table.\n")
guests.insert(0,'tahir')
guests.insert(2,'manthan')
guests.append('rohitesh')
print(f"{guests[0].title()}! would you like to have dinner with us tonight?")
print(f"{guests[1].title()}! would you like to have dinner with us tonight?")
print(f"{guests[2].title()}! would you like to have dinner with us tonight?")
print(f"{guests[3].title()}! would you like to have dinner with us tonight?")
print(f"{guests[4].title()}! would you like to have dinner with us tonight?")
print(f"{guests[5].title()}! would you like to have dinner with us tonight?")

print(f"\nNumber of guests coming are {len(guests)}")