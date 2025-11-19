my_dict = {'a': 1,'b' : 2,'c': 3,'d' : 4,'e': 5,'f': 6,'g': 7,'h' : 8,'i': 9,'j' : 10}
total_sum = sum(my_dict.values())
print(total_sum)

for key,values in my_dict.items() :
    print(values)

#compare to lists

list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

print(f" list1 is list2 : {list1 is list2}")
print(f" list1 is list3 : {list1 is list3}")
print(f" list1 is not list2 : {list1 is not list2}")