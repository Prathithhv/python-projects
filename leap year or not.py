year=(int(input("which year do u want to check\n")))
if (year%4==0 or (year%100!=0) and (year%400==0)):
    print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")    