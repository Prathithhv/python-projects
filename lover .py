name1=input("what is  your name\n").lower()
name2=input("what is their name \n").lower()
names=name1 + name2
t=names.count("t")
r=names.count("r")
u=names.count("u")
e=names.count("e")

true=t + r + u + e

l=names.count("l")
o=names.count("o")
v=names.count("v")
e=names.count("e")

love=l + o + v + e
lovescore=str(true) + str(love)
if int(lovescore)<=10 or int(lovescore)>=90:
    print(f"your love score is {lovescore}. you both are like coke and mentos")
if int(lovescore)<=50 or int(lovescore)>=40:
    print(f"your love score is {lovescore}.you are alright together")
else :
    print(f"your love score is {lovescore}") 