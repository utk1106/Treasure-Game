print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input('You\'re at crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if first == "left":
  second = (input('You\'ve come to a sacred lake. Do you want to swim across or wait. Type "swim" or "wait"\n')).lower()
  if second == "wait":
   third = input("You arrived at the Himalayas unharmed. There is the mountain with 3 huge caves. One is north door, one east door and one west door. Which door do you choose ? \n").lower()
   if third == "north door":
     print("This cave is full of massive spiders. You are dead! Game Over")
   elif third == "east door":
     print("You found the treasure. It's within YOU. You Win!")
   elif third == "west door":
     print("You have entered in the cave full of snakes. You are dead! Game Over")
   else:
     print("This cave doesn't exist")
  else:
   print("You are attacked by the an aligator, GAME OVER")
else:
  print("You fall into the hole, GAME OVER!")






#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload