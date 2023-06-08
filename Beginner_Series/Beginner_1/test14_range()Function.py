numbers = range(5, 10)
print(numbers) #returns range(0,5)
for number in numbers:
    print(number) # returns 5, 6, 7, 8, 9

x = range(5, 10, 2)
print(x) # returns range (5, 10, 2)
for number in x:
    print(number) # returns 5, 7, 9


for number in range(5): # do not need variable
    print(number) # returns 0, 1, 2, 3, 4