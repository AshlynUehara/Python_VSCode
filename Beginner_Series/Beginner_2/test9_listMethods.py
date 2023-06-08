numbers = [5, 2, 1, 7, 4]

numbers.append(20)
print(numbers)

numbers.insert(0, 1)
print(numbers)

numbers.remove(5) # removes first occurence of this item
print(numbers)

numbers.pop() # removes last number in list
print(numbers)

print(numbers.index(2)) # returns index of number

print(50 in numbers) # returns boolean value

numbers.sort() # sorts a list
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

numbers.clear()
print(numbers)