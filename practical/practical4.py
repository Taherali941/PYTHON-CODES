import math
print("simple calculator")
print("enter the operator from below to perform operation")
print('+, -, /,*, ^, !')

choice = input("enter your choice: ")
if choice in ['+','-','*','/','^']:
    x = float(input('enter the fisrt number 1: '))
    y = float(input("enter the second number 2: "))

    if choice == '+':
        result = x + y
    elif choice == '-':
        result = x - y
    elif choice == '*':
        result = x * y
    elif choice == '/':
        if y!=0:
            result = x / y
        else:
            print("error division by zero")
    elif choice == '^':
        result = x ** y
elif choice == '!':
    x = int(input("enter the number: "))
    if x >=0:
        result = math.factorial(x)
    else:
        result = print("factorial not defined for negative numbers")
else:
    result = "invalid choioce"
print(f"result is: {result}")
















































































































