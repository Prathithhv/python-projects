
import random
choice=input('heads or tails?\n').lower()
if choice == "heads" or choice == "tails":
 random_choice=random.choice(("heads" ,"tails"))
print(random_choice)