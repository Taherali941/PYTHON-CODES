N = int(input("enter the number you want to take input: "))

list = []

for i in range(N):
    num = float(input(f"enter the number {i +1}: "))
    list.append(num)

maximum = max(list)
minimum = min(list)
sum = sum(list)
average = sum/N

print(f"maximum number is: {maximum}")
print(f"minimum number is: {minimum}")
print(f"sum of list is: {sum}")
print(f"average of sum is: {average}")
