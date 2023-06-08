list = [10, 11, 14, 10, 20, 6]

max = 0
for num in list:
    if max <= num:
        max = num
    else:
        continue
print(max)
