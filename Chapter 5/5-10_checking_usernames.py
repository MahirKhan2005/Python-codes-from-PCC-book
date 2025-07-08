current_users = ['mahir','ameen','tahir','rehan','aarish']
current_users_lower = []
for name in current_users:
    current_users_lower.append(name.lower())

new_users = ['AMEEN','TAhir','arhaan','rose','subhan']
for name in new_users:
    if name.lower() in current_users_lower:
        print(f"{name.title()} has already been taken.")
    else:
        print(f"You can use {name.title()}.")