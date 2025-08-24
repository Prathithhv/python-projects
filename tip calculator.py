print("welcome to hr tip calculator")
bill=input("what is the total bill?\n")
tip=input("what percentage tip would you like to give? 10, 12, or 15? ")
people=input("how many people to split the bill? ")
bill_as_float=float(bill)
tip_as_int=int(tip)
people_as_int=int(people)
tip_as_percent=tip_as_int/100
total_tip_amount=bill_as_float*tip_as_percent
total_bill=bill_as_float+total_tip_amount   
bill_per_person=total_bill/people_as_int
print(f"each person should pay:{bill_per_person:}")