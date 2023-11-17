emp_id=int(input("Enter employee ID="))
emp_name=input("Enter employee NAME=")
basic_salary=int(input("Enter employee BASIC SALARY="))
hra=basic_salary*40/100
ta=basic_salary*30/100
da=basic_salary*40/100
esi=basic_salary*2/100
pf=basic_salary*12.5/100
gross=basic_salary+hra+ta+da
net=gross-esi-pf
print("Employee ID=",emp_id)
print("Employee NAME=",emp_name)
print("Employee BASIC SALARY=",basic_salary)
print("HRA=",hra)
print("TA=",ta)
print("DA=",da)
print("ESI=",esi)
print("PF=",pf)
print("GROSS=",gross)
print("NET=",net)

