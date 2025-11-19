a = input("enter your age: ")
b = int(a)
if b<18:
    print("YOU ARE a child")
elif b>18 or b<40:
    print("you are mature person")
elif b>40 or b<60:
    print("you are a senoir person")
elif b>60 or b<100:
    print('you are grand senior')
else :
    print("please enter only numbers")