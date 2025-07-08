def build_profile(first,last,**user_profile):
    user_profile['first name'] = first
    user_profile['last name'] = last
    return user_profile

print(build_profile('mahir', 'khan', city='kota', language='c', game='chess'))