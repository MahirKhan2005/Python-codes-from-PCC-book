def city_country(name,country='india'):
    return f"{name.title()}, {country.title()}"
print(city_country('delhi','india'))
print(city_country('new york','us'))
print(city_country('chennai','india'))