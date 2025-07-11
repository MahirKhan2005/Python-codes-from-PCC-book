"""Used for question 11-1"""

def city_country(city,country,population=0):
    if population:
        complete = f"{city.title()}, {country.title()}, Population - {population}"
    else:
        complete = f"{city.title()}, {country.title()}."
    return complete