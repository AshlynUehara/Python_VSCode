customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"]) # returns John Smith
print(customer.get("name")) # returns John Smith

print(customer.get("birthdate")) # returns None

print(customer.get("birthdate", "Jan 1 1980")) # returns Jan 1, 1980

customer["name"] = "Jack Smith" # changes name
print(customer["name"]) # returns Jack Smith

customer["birthdate"] = "Mar 1 1980" # changes birthdate
print(customer["birthdate"]) # returns Mar 1 1980
