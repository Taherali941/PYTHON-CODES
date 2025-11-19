# class student:
#     def __init__(self,name,age):
#         print(self)
#         print("this is a default constructor")
#         self.name = name
#         self.age = age
# s1 = student("hello",39)
# print(s1)
# class student:
#     def __init__(self,name):
#         print("this is a default constructor")
#         self.name = name
#         print(name)
# s1 = student("taher ali")
# s2 = student("swdfghj")
class student:
    def __init__(self,name):
        print("this is a default constructor")
        self.name = name

    def show(self,name,age):
        print("this is  show method")
        print("name :",name)
        print("age :",age)

s1 = student("taher ali")
s1.show("taher ali shaikh",19)
