a = int(input("enter the age : "))
if a<18:
    print("YOU ARE a child")
elif a>18 and a<40:
    print("you are mature person")
elif a>40 and a<60:
    print("you are a senoir person")
elif a>60 and a<100:
    print('you are grand senior')
else :
    print("please enter only numbers")