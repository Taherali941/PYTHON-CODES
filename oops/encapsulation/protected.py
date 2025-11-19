class student:
    def __init__(self):
        self._age = 20

    def get_age(self):
        return self._age

s1 = student()
# print(s1._age)
print("age : ",s1.get_age())