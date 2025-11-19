class calc:
    def calculation(self,a=20,b=80,*allargs):
        print("hello",a+b)
        print(allargs)

c1 = calc()
c1.calculation()
c1.calculation(50,100)
c1.calculation(50,100,50,40,49,49)