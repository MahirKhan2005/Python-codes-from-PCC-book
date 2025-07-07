guests = ['ameen','adeeb','aarish']
print(f"{guests[0].title()}! would you like to have dinner with us tonight?")
print(f"{guests[1].title()}! would you like to have dinner with us tonight?")
print(f"{guests[2].title()}! would you like to have dinner with us tonight?\n")

print(f"Unfortunately! Adeeb would not be able to come tonight.\n")
guests.remove('adeeb')
guests.append("rehan")
print(f"{guests[0].title()}! would you like to have dinner with us tonight?")
print(f"{guests[1].title()}! would you like to have dinner with us tonight?")
print(f"{guests[2].title()}! would you like to have dinner with us tonight?")