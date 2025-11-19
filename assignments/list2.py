a = [1,2,3,4,5,6,7,8,9,10]
# firts method

largest = max(a)
smallest = min(a)
print(f"largest number is {largest}\nsmallest number is {smallest}")

#second method

largest_num = a[0]
smallest_num = a[0]
for items in a:
    if items > largest_num :
        largest_num = items
    if items < smallest_num :
        smallet_num = items
print(largest_num,smallest_num)