numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # returns [1, 2, 3, 4, 5, 6]

numbers.insert(2, -1)
print(numbers) # returns [-1, 1, 2, 3, 4, 5, 6]

numbers.remove(3)
print(numbers) # returns [-1, 1, 2, 4, 5, 6]

print(1 in numbers) # returns True
print(10 in numbers) # returns False

print(len(numbers)) #len returns number of elements in a list

numbers.clear()
print(numbers) # returns []