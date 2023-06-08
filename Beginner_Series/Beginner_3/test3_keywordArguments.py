def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")

# positional arguments
print("Start")
greet_user("Smith", "John") # returns Hi Smith John!
print("Finish")

# keyword arguments:
print("Start")
greet_user(last_name = "Smith", first_name = "John") # returns Hi John Smith!

# always use positional arguments first and then keyword arguments