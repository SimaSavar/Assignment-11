enter_year=int(input("enter a year"))
result={}
if enter_year%4==0 and enter_year%100!=0:
   print(enter_year,":Leap Year")
elif enter_year%400==0:
   print(enter_year,"Leap Year")
else:
  print(enter_year,":not Leap Year") 