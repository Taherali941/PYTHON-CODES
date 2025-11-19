numbers = [10, 24, 76, 23, 12]

largest_number = numbers[0]  
for num in numbers:
    if num > largest_number:
        largest_number = num
print(largest_number)