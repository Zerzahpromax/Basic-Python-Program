name=input("Enter your name=")
per=int(input("Enter your percentage="))
if(per>=90):
    grade="A+"
elif(per>=80 and per<=90):
    grade="B"
elif(per>=70 and per<=80):
    grade="C"
elif(per>=60 and per<=70):
    grade="D"
elif(per>=50 and per <=60):
    grade="E"
else:
    grade="F"

print(name)
print(per)
print(grade)