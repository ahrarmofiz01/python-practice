year=int(input("enter year:"))
if year % 400 ==0:
    print(year , "is leap year")
elif year%100==0:
    print(year ,"is not a leap year")
elif year%4==0:
    print(year,"is a leap year")
else:
    print("not a leap year")
unit=int(input("enter the unit:"))
if unit <=100:
    print(unit*5)
elif unit>100 and unit<=200:
    print(unit*7)
elif unit>200 and unit >=1000:
    print(unit*10)
else:
    print("go to goverment office your bill is too high")
    
