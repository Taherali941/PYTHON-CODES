# print('hello world')
# print(1 + 2)
# print(1 == 1)
# a = 5
# b = 2
# if a > b:
#     print("a is greater than 2")
# else :
#     print("a is not greater than 2")
    
# all data types
a = 1  # integer
b = "string"  
c = 1.239  # float
d = 123j # complex

e = ['apple','ball',"cat"]  #list
f =('apples', 'balls','cats')  #tuple
for items in f:
    print(f"{items}")

g = {
    "name":"taher ali",
    "age": 18,                  #dict
    "college":"Alard college"
}
for key, value in g.items():
    print(f"{key}: {value}")

h = {"appl","ball","cat","dog"}   #set

i = None
j = True  #booolean



a = 21
b = 15
print(bin(a & b))
print(a and b)