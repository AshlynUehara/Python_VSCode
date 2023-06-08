try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError: # if the program comes across a ValueError, instead of crashing it will print
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")

# Exception: type of error that crashes our program

