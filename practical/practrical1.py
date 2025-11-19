basic_pay = int(input("enter the basic pay: "))
hra = (basic_pay*10)/100
Ta = (basic_pay*5)/100
gross_salary = basic_pay+ hra + Ta
Professional_tax = (gross_salary*2)/100
Net_salary = gross_salary - Professional_tax
print(f"gross salary is: {gross_salary}, Net salary is: {Net_salary} ")