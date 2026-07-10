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
damage = 20
healing = 30

# Update player_health using arithmetic operators.
# print(player_health - damage + healing)
# Print the new health.
player_health = player_health - damage + healing 
print("Remaining Health of player is :", player_health)




# Challenge 4
# Give the player gold after defeating an enemy.
enemy = 40
player_gold += enemy
print ("players gold :" , player_gold)
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
if x=="a":
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
item = ["sword", "shield", "potion","skills", "luck", "armor", "gold", "health"]
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
     x = input("Attack or Run?")
     if x == "Attack":
          print("Player", x)
          continue
     elif x == "Run":
          break
     # ai helped me here 
# Stop only when the player types "Run".


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
print("Enemies Curent health is ", enemy)
print("The Battle Begins")
x = 0
while enemy > 0:
      
     #  print(x)
      if x<5:
          x=x+1
          print("Round no.",x)
#     attack enemy
      input("Press enter to Damage Enemy: ")
      enemy=enemy - damage
      print("Enemy health left is ",enemy)
#     enemy attacks back
      print("Now Enemy Attacks back")
      player_health = player_health-damage
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
     print("Attack gives",damage,"damage to enemy")
# It returns damage.
attack()



# Challenge 18
# Create:
# heal(current_health)

def heal(player_health=50):
     print("players curent health is:", player_health)
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
     enemy_health-=damage
     print("enemy health left:", enemy_health)
     print("ENEMY ATTACKS BACK")
     player_health-=enemy
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
inventory_items()

# Challenge 25
# Remove used items.
# def remove():
    

# Challenge 26
# Create a backpack limit.
# Maximum:
# 10 items.


# ==========================================================
# PHASE 6 — DICTIONARIES
# ==========================================================

# Challenge 27
# Store player stats inside a dictionary.


# Example:
#
# {
#     "health":100,
#     "gold":20,
#     "level":1
# }


# Challenge 28
# Store enemy information in another dictionary.


# Challenge 29
# Create multiple enemies using a list of dictionaries.


# Challenge 30
# Search for a specific enemy by name.


# ==========================================================
# PHASE 7 — CLASSES
# ==========================================================

# Challenge 31
# Create a Player class.
#
# Attributes:
# name
# health
# gold
# level


# Challenge 32
# Add methods:
#
# attack()
# heal()
# show_stats()


# Challenge 33
# Create an Enemy class.


# Challenge 34
# Create several enemy objects.


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