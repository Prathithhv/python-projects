import random
names=input("enter your names seperated by a comma ")
names_=names.split(",")
print (", ".join(names_))
random_name=random.choice(names_)
print(f"{random_name} will be paying the bill today")