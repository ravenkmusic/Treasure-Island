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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("On treasure Island is Bowser's castle. You are Mario and you have just entered inside. Do you want to turn left or right? Type left or right.\n").lower()

if direction == "left":
  pull_or_exit = input('You\'ve chosen left. You are now in a library. You can let your curiosity lead you and pull a book off the shelf or you can exit the room. Type "pull" or "exit".\n')
  if pull_or_exit == "pull":
    doors = input('You pull the book and it opens a secret passage. You enter it and see three doors. Which one do you enter? Type "1", "2" or "3".\n')
    if doors == "1":
      print("You get blown up by a Bob-omb. Game over.")
    elif doors == "2":
      print("This door had the treasure! You win!")
    elif doors == "3":
      print("Yoshi went rogue. He was hiding in this door and waited for you to open it and shanked you. Game over.")
    else:
      print("You got distracted while for a door that didn't exist. Koopa Kid jumped out and attacked you. Game over.")
  else:
    print("You fall through a trap door that suddenly appeared when you tried to leave. Game over.")
else:
  print("You've been spotted by a castle guard and they seize you. Game over.")