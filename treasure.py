print('''
******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______    
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
#triple quotes is used for multi line strings
print("welcome to the treausre island")
print("your mission is to find the treasure")
choice=input("you're are at a cross road. choose which way you want to go.'left' or 'right'\n")

if choice=="right":
    print("you fell into a hole. game over")
elif choice=="left":
    choice1=input("you've come to a lake.there is an island in the middle of the lake. type 'wait' to wait for a boat or type 'swim' to swimacross the lake\n").lower()
    if choice1=="swim":
       print("you got eaten by a crocodile. game over")
    elif choice1=="wait":
     choice2=input("game continues. a ship has given u a ride to a island and u face three doors.yellow,brown and red. choose either of the three\n").lower() 
    if choice2=="red":
      print("game over u fell into a volcano")
    elif choice2=="yellow":
      print("congratulations u found the treasure")  
    else:
      print("game over . u drown in a pool of acid")           