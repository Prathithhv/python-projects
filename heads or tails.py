import random
choice=input('heads or tails?\n').lower()
while choice not in ("heads", "tails"):
 print("invalid input. please choose heads or tails")
 choice=input('heads or tails?\n').lower()
 if choice=="heads" or choice="tails:
 random_choice=random.choice(("heads" ,"tails"))
print(random_choice)



