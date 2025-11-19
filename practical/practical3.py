marks=[]
for i in range(5):
    m = float(input(f"enter the makrs of subject {i+1}: "))
    marks.append(m)
if any(m < 40 for i in marks):
    print("Result is fail")
else:
    total = sum(marks)
    aggregate = (total/500)*100

    if aggregate >= 75:
       grade =  "distinction"
    elif aggregate >= 60:
        grade = "First division"
    elif aggregate >= 50:
        grade = "second division"
    elif aggregate >= 40:
         grade = "third division"
    else:
        grade = "fail"
print(f"total marks is {total}")
print(f"aggregate percentage id {aggregate}%")
print(f"grade is {grade}")
