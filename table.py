num = int(input("Enter the number for which you want the multiplication table: "))
for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")