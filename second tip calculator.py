print("welcome to the tip calculator")
bill=float(input("what is your total bill?\n"))
tip=int(input("enter the amount of tip u would like to give:0,10,15,20\n"))
tipinbill=bill*tip/100
tip_bill=bill+tipinbill
wanna_split=input("do you want to split the bill? choose 'yes' or 'no'\n").lower()
if wanna_split=="yes":
 people=int(input("enter the total amount of people\n"))
total_bill=tip_bill/people
tip_in_bill=tip_bill-bill
print(f"bill each person is:{total_bill}")
print(f"the entir bill is{tip_bill}")
print(f"you have tipped {tip_in_bill}")