# ==========================================================
# PYTHON LEARNING PROJECT
# Project Title: Build Your Own Text-Based Adventure Game
#
# Goal:
# Instead of solving random exercises, you'll slowly build one
# large game. Every challenge adds a new feature while teaching
# an important Python concept.
#
# Rule:
# Do NOT skip challenges.
# Every challenge should work before moving to the next one.
# ==========================================================
#Don't just guess the answer. Plan your steps and think like a strategist.
print("Azeem X") 
print("Code, glitch, grow.")
# Get Ready to build your own text-based adventure game!
# Get ready to learn Python fundamentals and object-oriented programming!
# Best of luck, and have fun buddy! 

# ==========================================================
# PHASE 1 — VARIABLES
# ==========================================================

# Challenge 1
# Create variables for:
# - player_name
player_name = "Hero"
# - player_health
player_health = 30
# - player_gold
player_gold = 1003
# - player_level
player_level = 5
# Print them in a nice format.
print (" Players Name:",player_name ,"\n", "Player's Gold:", player_gold, "\n", "Player's Level:", player_level ,"\n", "Player's Health:", player_health)


# input()
# Challenge 2
# Ask the player for their name using input().
# Store it inside a variable.
# Welcome the player.
player_name = input ("Player enter your name here :")
print ("Welcome the player: ", player_name)
print ("Hi! Your Name is: ", player_name)




# Challenge 3
# Create damage and healing variables.
player_damage = 10
enemy_damage = 20
healing = 30

# Update player_health using arithmetic operators.
# print(player_health - damage + healing)
# Print the new health.
player_health = player_health - enemy_damage + healing 
print("Remaining Health of player is :", player_health)




# Challenge 4
# Give the player gold after defeating an enemy.
enemy_health = 40
player_gold += enemy_health
print ("players gold increased to :" , player_gold)
# Use += instead of rewriting the variable.


# Challenge 5
# Practice comparison operators.
if player_health < 1 :
     print ("Player is no-more")
else :
     print ("Player is alive.")
# Print whether the player is alive.

# Print whether the player is rich (gold > 100).
if player_gold > 100 :
     print ("Player is rich")
     
else: 
     print("Poor Player plz topup")

# ==========================================================
# PHASE 2 — IF STATEMENTS
# ==========================================================

# Challenge 6
# If player_health is 0 or below:
#     Print "Game Over"
# Else:
#     Print "You survived"
if player_health <= 0 :
     print ("Game Over")
else :
     print ("You survived")


# Challenge 7
# Create a shop.
# If player_gold is enough:
#     Buy a sword.
# Otherwise:
#     Print "Not enough gold."

sword = 400
if player_gold > sword:
    print("You can Buy a Sword.", "\n", "Your current Gold is :", player_gold)
    input("press enter to buy")
    player_gold = player_gold - sword 
    print("Congrates! You has a new Sword.", "\n", "Your current Gold is :", player_gold)
else: 
     print("Oh! Not enough gold")


# Challenge 8
# Ask the player to choose:
# 1. Forest
# 2. Cave
# 3. Village

print(player_name , "please choose a place")
x = int(input("1) Forest. 2)Cave. 3)Village."))
# x = int 
# Print different messages for each.
if x == 1:
     print("You selected Forest place"),
elif x == 2:
     print("You selected Cave place"),
elif x == 3:
     print("You selected Village place"),
else:
     print("Wrong Input, Try Again Plz")



# Challenge 9
# Add difficulty levels:
# Easy
# Medium
# Hard
#
# Give different enemy damage.
print("Select your difficulty level :")
x=(input("a)Easy. b)Medium. c)Hard."))
if   x=="a":
     print("You Selected Easy Level.")
elif x=="b":
     print("You Selected Medium Level.")
elif x=="c":
     print("You Selected Hard Level.")

# =================================azeem=========================
# PHASE 3 — LOOPS
# ==========================================================

# Challenge 10
# Print numbers 1 to 10 using a for loop.
print("Print numbers 1 to 10 using a for loop.")
for i in range (1, 11):
   print(i)
     

     


# Challenge 11
# Print every item in an inventory list.
item = ["sword", "shield", "potion","skills", "luck", "armor", "gold", "health", "care", "Strength"]
print("Inventory:", item)


# Challenge 12
# Create a countdown from 10 to 1. 
for i in range (10, 0, -1):
     print(i)

print("Done")


# Challenge 13
# Create a while loop that keeps asking:
# "Attack or Run?"
while True:
     x = input("attack or run?")
     if x == "attack":
          print("Player", x)
          continue
     elif x == "run":
          break
     # ai helped me here 
# Stop only when the player types "run".


# Challenge 14
# Make a healing station.
while player_health < 100:
     print ("Your current health is ,", player_health)
# Heal the player until health reaches 100.
     input ("Press Enter to heal yourself, Survivor")
     for player_health in range(player_health, 110, 10):
          print("You are healling now", "Your curent health is ", player_health)

print("You are Healed", player_health,"% successfully ")



# Challenge 15
# Create a battle loop.
input("Press enter to Start Battle: ")
# While enemy health > 0:
print("Enemies Curent health is ",enemy_health)
print("The Battle Begins")
x = 0
while enemy_health > 0:
      
     #  print(x)
      if x<5:
          x=x+1
          print("Round no.",x)
#     attack enemy
      input("Press enter to Damage Enemy: ")
      enemy_health =enemy_health - player_damage
      print("Enemy health left is ",enemy_health)
#     enemy attacks back
      if enemy_health > 0:
       print("Now Enemy Attacks back")
       player_health = player_health-enemy_damage
      else:
        print("Enemy has 0 health.")  
# Print health after every turn.
      print("Remaining Player Health is:",player_health)
      continue
else:
     print("Enemy is Defeated")





# ==========================================================
# PHASE 4 — FUNCTIONS
# ==========================================================

# Challenge 16
# Create a function:
def greet_player():
     print("Welcome!!",player_name)
# It prints a welcome message.
greet_player()

# Challenge 17
# Create:
#
# attack()
def attack():
     print("Attack gives",player_damage,"damage to enemy")
# It returns damage.
attack()



# Challenge 18
# Create:
# heal(current_health)

def heal(player_health=50):
     print("players health before healing is:",player_health)
   # Return updated health.
     player_health += healing
     return(player_health)
print("updated health of player is:",  heal(player_health))  

          


# Challenge 19
# Create:
def battle(player_health=80, enemy_health=60):
# battle(player_health, enemy_health)
     print("the 2nd battle Begins here")
     x = 1
     # if x < 10:
     #      x+=x
     print("Round no.",x)
     print("enemy health is:", enemy_health)
     input("Press Enter to attack enemy")
     enemy_health-=player_damage
     print("enemy health left:", enemy_health)
     print("ENEMY ATTACKS BACK")
     player_health-=enemy_damage
     print("player health is", player_health)

     return(player_health, enemy_health)
print("Round one of battle ended with:", battle())
# Simulate one battle.



# Challenge 20
# Create:
def level_up(level=0):
# level_up(level)
  print("Player level was:", level)
  level= level+1
  return(level)
# Return the next level.
print("Now, player level is:", level_up())


# Challenge 21
# Move ALL repeated code into functions.
# def repeated():


# ==========================================================
# PHASE 5 — LISTS
# ==========================================================

# Challenge 22
# Create an inventory list.
def inventory():
  inventory_list = ["sword", "shield", "heal","skill", "luck", "armor", "gold", "health"]
  return(inventory_list)
print("Inventory items are:", inventory())

# Challenge 23
# Allow the player to collect items.
def collect_items(player_gold=1100):
     print("player can collect items while playing.")
     print("player gold is:", player_gold)
     player_gold += 100
     return(player_gold)
print("player earns golds", collect_items())



# Challenge 24
# Print inventory using a loop.
def inventory_items():
   x=0
   while True:
     if x<1:
      print("inventory items are:")
      x=x+1
     #  print("786")
      print(inventory() )
      break
# inventory_items() # call function for direct output.
# good approch is
# print("try-again, line by line")
for x in inventory():
    print(x)
    


# Challenge 25
# Remove used items.

print("now we are going to remove items")
print("total number of items are:", len(item))
x = int(input("enter any index number to remove an item (0 ~ 9):"))
print("your selected number is:", x)
print("we are removing this from items(list):",item[x])
#del inventory[x]
item.pop(x)  
# remove_item()
print(item)

# Challenge 26
# Create a backpack limit.
backpack = item
x = len(backpack)
# Maximum:10 items.
while x < 10:
 
 print("backpack has occopied space of ",x,"items.")
 y = str(input("add a new item here :"))
 
 if y == "":
  print("try again")
 else:
  backpack.append(y)
  x = len(backpack)
  print("item added sucessfully.")
  print("updated inventory items are :", backpack)
#   break
  continue
 
else:
 print("backpack is full buddy")
 print(backpack)
 print(x,"total maximum number of items achieved.")


# ==========================================================
# PHASE 6 — DICTIONARIES
# ==========================================================

# Challenge 27
# Store player stats inside a dictionary.
# Example:
# {
#     "health":100,
#     "gold":20,
#     "level":1
# }
player_dict = {
    "Player health":player_health,
    "Player gold":player_gold,
    "Player level":player_level,
    "Player damage": player_damage
}
print("player_dict:",player_dict)


enemy_name="jack"
# Challenge 28
# Store enemy information in another dictionary.
enemy_dict = {
    "Enemy Name": enemy_name,
    "Enemy Health": enemy_health,
    "Enemy Damage": enemy_damage,
    "Enemy of Level": player_level
}
print("enemy_dict:",enemy_dict)

# Challenge 29
# Create multiple enemies using a list of dictionaries.
enemies_list = [ 
      {1:"Enemy_1", "name":"Heihachi Mishima", "Enemy Health":20, "Enemy Damage": enemy_damage, "Enemy of Level": player_level },
      {2:"Enemy_2", "name":"Kazuya Mishima", "Enemy Health":20, "Enemy Damage": enemy_damage, "Enemy of Level": player_level },
      {3:"Enemy_3", "name":"Akuma", "Enemy Health":20, "Enemy Damage": enemy_damage, "Enemy of Level": player_level }, 
      {4:"Enemy_4", "name":"Jin", "Enemy Health":20, "Enemy Damage": enemy_damage, "Enemy of Level": player_level }, 
      {5:"Enemy_5", "name":"Devil Jin", "Enemy Health":20, "Enemy Damage": enemy_damage, "Enemy of Level": player_level }
]
for x in enemies_list:
 print(x)

# TOPIC: NESTED DICTIONARY
# enemies_dic = {
#     "enemy_1":{
#     "Enemy Name": enemy_name,
#     "Enemy Health": enemy_health,
#     "Enemy Damage": enemy_damage,
#     "Enemy of Level": player_level
#     },
#     "enemy_2":{
#     "Enemy Name": enemy_name,
#     "Enemy Health": enemy_health,
#     "Enemy Damage": enemy_damage,
#     "Enemy of Level": player_level
#     },
#     "enemy_3":{
#     "Enemy Name": enemy_name,
#     "Enemy Health": enemy_health,
#     "Enemy Damage": enemy_damage,
#     "Enemy of Level": player_level
#     },
# }
# print(enemies_dic)



# Challenge 30
# Search for a specific enemy by name.

# step no. 1: i'm finding also printing names
x=-1
while x<5:
    # print(x)
    x+=1
    # print(x)
    # print("hi buddy!!", enemies_list[x]["name"])
    enemy_names = enemies_list[x]["name"]
    print("Hello!", enemy_names)
    if x < 4:
     continue 
    elif x==4:
        print("list ends")
        break

#now start implementing it.
 
name_found = False  # flag variable to check if name is found or not
x = input("Search Full Name of Enemy Here by typing:")
print("Your intered name is:",x)
index = -1
while index < 4:
    index += 1
    # print(index)
    enemy_name = enemies_list[index]["name"]
    # print (enemy_name)
    # print (x)
    if x == enemy_name:
        print("We found ",enemy_name)
        enemy_index = enemies_list[index][index+1]
        print ("Title of enemy is:",enemy_index)
        enemy_health = enemies_list[index]["Enemy Health"]
        print ("Enemy Health is:",enemy_health)
        enemy_damage = enemies_list[index]["Enemy Damage"]
        print ("Enemy Damage is:",enemy_damage)
        enemy_level = enemies_list[index]["Enemy of Level"]
        print ("Enemy level for Player is",enemy_level)
        name_found = True
        break
    
if name_found == False :
    print("Data is not Found in list, so")
    print("Retry Next time with these names;")
    print(enemies_list[0]["name"])
    print(enemies_list[1]["name"])
    print(enemies_list[2]["name"])
    print(enemies_list[3]["name"])
    print(enemies_list[4]["name"])
        


# ==========================================================
# PHASE 7 — CLASSES
# ==========================================================

# Challenge 31
# Create a Player class.
# ...............................................this is a wrong way to create class. See below, Challenge 32 for correct way to create class with methods.
#   Attributes:
class player_attributes : 

    # name
    name = str("player_1")
    # health
    health = int(79)
    # gold
    gold = int(405)
    # level
    level = int(3)
print(player_attributes.name)






# Challenge 32
# Add methods:

class Player: #class name should be capitalized.
    
 # Note: The following line is not correct in Python. You cannot define a variable like this outside of methods in a class. It should be defined inside the __init__ method or as a class variable.
    player_health = 49

# this is the correct way to define attributes in a class using the __init__ method.     
    def __init__(self, damage, heals, level, kills, survival, wins):
        # Initialize attributes
        self.damage = damage
        self.heals = heals
        self.level = level
        self.kills = kills
        self.survival = survival
        self.wins = wins
        # Initialize player health
        self.player_health = 49
                       
# attack()
    def attack(self):
        # Simulate an attack on an enemy.
        print("Player is Attacking to Enemy. The damage it gives:", self.damage )
        # here you can implement logic to reduce enemy health based on self.damage
        self.player_health -= self.damage
        print("Player health after attack:", self.player_health)

# heal()
    def heal(self):
        # Simulate healing the player.
        print("Player is Healing now.")
        # here you can implement logic to increase player health based on self.heals
        self.player_health += self.heals
        print("player health is :", self.player_health)

# show_stats()
    def show_stats(self):
        # Display the player's stats.
        print("Stats of player are:" )
        # print all the attributes of the player
        print(self.damage)
        print(self.heals)
        print(self.level)
        print(self.kills)
        print(self.survival)
        print(self.wins)
        


# here we are creating an instance of the Player class with specific attributes.
p1 = Player(20, 30, 2, 23, 45, 13)
# here we are calling the methods on the instance
print(p1.attack())
print(p1.heal())
print(p1.show_stats())
# now you can create multiple instances of the Player class with different attributes to represent different players in the game...



# Challenge 33
# Create an Enemy class.

class Enemy:
    
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


# Challenge 34
# Create several enemy objects.
e1 = Enemy("Jack-Alpha", 70, 5)
e2 = Enemy("Mishima", 30, 15)
e3 = Enemy("Rogue G", 45, 10)
e4 = Enemy("Tekken Force", 50, 5)



# Challenge 35
# Make Player fight Enemy objects.



# Challenge 36
# Add experience points.
# Player levels up after enough XP.


# ==========================================================
# PHASE 8 — ADVANCED CLASSES
# ==========================================================

# Challenge 37
# Create a Weapon class.


# Challenge 38
# Player can equip different weapons.


# Challenge 39
# Weapon changes attack damage.


# Challenge 40
# Create an Item class.
#
# Examples:
# Potion
# Shield
# Scroll


# Challenge 41
# Use inheritance.
#
# Base class:
# Item
#
# Child classes:
# Potion
# Weapon
# Armor


# ==========================================================
# PHASE 9 — GAME WORLD
# ==========================================================

# Challenge 42
# Create multiple locations.


# Challenge 43
# Allow player movement:
# north
# south
# east
# west


# Challenge 44
# Randomly spawn enemies.


# Challenge 45
# Add treasure chests.


# Challenge 46
# Add NPC characters.


# Challenge 47
# NPCs can give quests.


# ==========================================================
# PHASE 10 — POLISH
# ==========================================================

# Challenge 48
# Create a game menu.
#
# Start
# Load
# Exit


# Challenge 49
# Save player data to a file.


# Challenge 50
# Load saved data.


# Challenge 51
# Add a boss battle.


# Challenge 52
# Add victory and defeat endings.


# Challenge 53
# Refactor your entire project.
#
# Split code into multiple files:
#
# player.py
# enemy.py
# items.py
# game.py
# world.py


# Challenge 54
# Make the code readable:
#
# - remove duplicated code
# - rename bad variable names
# - add comments
# - organize functions


# ==========================================================
# FINAL BOSS CHALLENGE
# ==========================================================

# Without looking at previous solutions, rebuild the entire
# game from scratch.
#
# Your finished game should include:
#
# ✔ Variables
# ✔ Input
# ✔ If statements
# ✔ Loops
# ✔ Functions
# ✔ Lists
# ✔ Dictionaries
# ✔ Classes
# ✔ Inheritance
# ✔ File handling
# ✔ Multiple modules
# ✔ Inventory system
# ✔ Battle system
# ✔ NPCs
# ✔ Quests
# ✔ Weapons
# ✔ Save/Load
# ✔ Boss fight
#
# If you can complete this project independently, you'll have
# a solid practical understanding of Python fundamentals and
# object-oriented programming.