class A:
    def myfun(self):
        print("this is class a function")
class B(A):
    def myfun(self):
       print("this is class B function")  
class C(B):
    def myfun(self):
       print("this is class C function")  
a1 = [A(),B(),C()]
for i in a1:
    i.myfun()