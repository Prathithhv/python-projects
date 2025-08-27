print("welcome to the rollercoaster")
height=float(input("please enter your height in cms\n"))
if height>=120:
    print("you can ride the rollecoaster")
    age=int(input("please enter your age:\n"))
    if age<=12:
        bill=4
        print("the ticket price for  is 4$")
    elif age<=18:
        bill=7
        print("the ticket price is 7$") 
    else:
        bill=13
        print("the ticket price is 13$")
    
    bill_int=int(bill)              
    picture=input("do you want pictures taken while riding? type yes or no\n").lower()
    if picture=="yes":
        print(f"your total bill is {bill+3}$")

else:
    print("you must be 120cm or above to ride")    