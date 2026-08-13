# Challenge 53: Refactor your entire project.
import random
import json

# Challenge 36
# 36-1. Add experience points.

# seting variables here:
player_health = 100
player_gold = 500 
player_damage = 20
inventory_list = ["sword", "shield", "heal","skill", "luck", "armor", "gold", "health"]

# enemy default stats
enemy_health = 100
enemy_damage = 20

# game default stats
increase_xp = 50
increase_gold = 100
level_up_xp = 100
level_up_xp_l2 = 200 # var needed for next level
healings = 30
# variables
x = 1
# statements
fight_won = False

# class for players, every player will have these attributes.
class Player:
    def __init__(self, name, level, xp, wins):
        self.name = name
        self.level = level
        self.xp = xp
        self.wins = wins        
p1 = Player("Ash", 0, 50, 1)      
print("Name:",p1.name,"| Level:",p1.level, "| XP:",p1.xp, "| Wins:",p1.wins, )

# Challenge 46. Add NPC characters.
class Npcs(Player):
   def __init__(self, name, level):
      super().__init__(name, level, xp=0, wins=0)
npc1 = Npcs("Mr.Victor", 3)
npc2 = Npcs("Pikachu", 5)
npc3 = Npcs("Serena", 2)
npc4 = Npcs("Leo", 6)

# Challenge 47:  NPCs can give quests.
def quests():
   print("Move Around in this High End Graphic Game Map.")
   print(f"|a)Do you want to visit: {npc1.name} ")
   print(f"|b)Do you want to visit: {npc2.name} ")
   print(f"|c)Do you want to visit: {npc3.name} ")
   print(f"|d)Do you want to visit: {npc4.name} ")
   Npc = input("Choose a weapon to equip (a/b/c/d): ")
   if Npc == "a":
    # player_damage += w1.damage
    print(f"You have visited {npc1.name}. Your Quest is to...")
   elif Npc == "b":
    # player_damage += w2.damage
    print(f"You have visited {npc2.name}. Your Quest is to....")
   elif Npc == "c":
    # player_damage += w3.damage
    print(f"You have visited {npc3.name}. Your Quest is to...")
   elif Npc == "d":
    # player_damage += w4.damage
    print(f"You have equipped {npc4.name}. Your Quest is to...") 
    


# Challenge 37. Create a Weapon class.
# class Weapon://///////// comented bcz > it is recreated in inheritance.
# Challenge 40. Create an Item class.
# class Item ():
# i commented it bcz .. we recreated it in challenge 41.....

# Challenge 41. Use inheritance.  Base class: Item,  Child classes: Potion, Weapon, Armor
class Item ():
   def __init__(self, name,):
      self.name = name # name of items
# 1.Potion
class Potion(Item):
   def __init__(self,name, cost,  heal ):
      self.name = name 
      self.cost = cost
      self.heal = heal
# 2.Weapon
class Weapon(Item):
   def __init__(self, name, cost,  damage ):
         self.name = name 
         self.cost = cost
         self.damage = damage
# 3.Armor
class Armor(Item):
   def __init__(self, name, cost,  protect ):
         self.name = name 
         self.cost = cost
         self.protect = protect
# potion         
po1 = Potion("Healing Potion", 200, 50)
po2 = Potion("Elixir", 300, 50)
# weapon colection
w1 = Weapon("Knife", 400, 50)
w2 = Weapon("Sword", 500, 100)
w3 = Weapon("Dagger", 600, 150)
w4 = Weapon("Shotgun", 700, 200)
# armor colection
a1 = Armor("helmet", 100, 30)
a2 = Armor("shield", 200, 50)

# Challenge 42: Create multiple locations.
class Locations():
   def __init__(self, name="Default", x_axis=0, y_axis=0):
      self.name = name
      self.x_axis = x_axis
      self.y_axis = y_axis
l1 = Locations("East", 1, 0) # when X increases
l2 = Locations("West", -1, 0) # when X decreases
l3 = Locations("North", 0, -1)  # when y increases
l4 = Locations("South", 0, 1) # when y decreases


# Challenge 44: Randomly spawn enemies.
class Enemy:
    def __init__(self, name, damage):
     self.name = name
     self.damage = damage  
enemy1 = Enemy("Mishima", 30) 
enemy2 = Enemy("Rogue", 25)  
enemy3 = Enemy("Alpha",15)  
enemies = [enemy1, enemy2, enemy3]
spawn_enemy = random.choice(enemies)
print(f"Spawned: {spawn_enemy.name} with {spawn_enemy.damage} damage")

# Challenge 45 :add treasure chests.
def treasure():
   global player_gold
   player_gold += increase_gold
   print("You got", increase_gold, "gold coins from Treasure chest.")

# Challenge 43. Allow player movement: north, south, east, west
def right():
   print("Player moves",l1.name, l1.x_axis, l1.y_axis)
def left():
   print("Player moves",l2.name, l2.x_axis, l2.y_axis)
def up():
   print("Player moves",l3.name, l3.x_axis, l3.y_axis)
def down():
   print("Player moves",l4.name, l4.x_axis, l4.y_axis)


# # Challenge 52: Add victory and defeat endings.
def matchEvents():
   if player_health > enemy_health:
      print(f"Victory! Enemy Defeated.")
   elif player_health < enemy_health:
      print(f"The End! Player Defeated, Try Next Time")
   else: print("Draw Fight")

    


# Challenge 48 -> Create a game menu: Start, Load, Exit
print('Game Menu')
print('1. Start a new game')
print('2. Load a game')
print('3. Exit')
menuoption = input("Type in the number of the menu option you would like;")
if menuoption == '1':
   print('The Start of the Game')
elif menuoption == '2':
   print('Load a Game')
elif menuoption == '3':
   print('Exits Game !')
else:
   print("That isn't a valid option")


input("Press Enter to signIn")
treasure()
print("Hi", p1.name)      

quests()

# Challenge 38 is Player can equip different weapons.
print("Available weapons are:")
print(f"|a)Weapon: {w1.name}, Damage: {w1.damage} ")
print(f"|b)Weapon: {w2.name}, Damage: {w2.damage} ")
print(f"|c)Weapon: {w3.name}, Damage: {w3.damage} ")
print(f"|d)Weapon: {w4.name}, Damage: {w4.damage} ")
weapon_equipped = input("Choose a weapon to equip (a/b/c/d): ")
# Challenge 39 is Weapon changes attack damage.
if weapon_equipped == "a":
    player_damage += w1.damage
    print(f"You have equipped {w1.name}. Your damage is increased to {player_damage}.")
elif weapon_equipped == "b":
    player_damage += w2.damage
    print(f"You have equipped {w2.name}. Your damage is increased to {player_damage}.")
elif weapon_equipped == "c":
    player_damage += w3.damage
    print(f"You have equipped {w3.name}. Your damage is increased to {player_damage}.")
elif weapon_equipped == "d":
    player_damage += w4.damage
    print(f"You have equipped {w4.name}. Your damage is increased to {player_damage}.")

# battle rounds count 
def round_x():
   global x
#    print("Round is:",x)
   for y in range(10):
    x += 1 
    return x  
   
# this function will shows how much xp is requireed by player to levelup
def levelup_xp_req():
    xp_needed = level_up_xp - p1.xp
    print(f"XP remains for levelup is {xp_needed}") 

# gold increse function calls after fight
def inc_gold():
   global player_gold, xp_needed
   if player_health > 0:
     player_gold += increase_gold
     print(f"Gold received after defeating enemy: {player_gold}")

# after fight xp increse function calls 
def inc_xp():
    while player_health > 0:
     fight_won = True
     if fight_won:
      p1.xp += increase_xp
      print("XP increased after defeating enemy is 50, Total:",p1.xp)
      break
    else:
     print("You lose! Try Again next time.")

# 36-2. Player levels up after enough XP
def level_up():
    global player_gold
    if p1.xp >= level_up_xp:
        p1.level += 1
        print(f"LEVEL UP!")
        print(f"{p1.name}: Lv. {p1.level - 1} -> Lv. {p1.level}")
        player_gold += increase_gold
        print(f"Gold received after levelup is 100, Total: {player_gold}") 
        p1.xp -= level_up_xp
        print(f"XP Balance reset: {p1.xp}")
    else:
        print("Still needs", levelup_xp_req(),"for levelup")  

# function which calls Fight
def fight():
   global enemy_damage, enemy_health, player_health, player_damage, x
   print("battle starts")
   print("Round no", x)
   # player attacks 
   input("Press Enter to Start Fighting")
   print(f"Player Attacks, it gives {player_damage} damage to enemy.")
   enemy_health -= player_damage
   print(f"The remaining health of enemy is : {enemy_health}")
   # if enemy died 
   if enemy_health > 0:
      # now enemy attacks back
      print(f"Now enemy attacks back. It gives {enemy_damage} damage to the player.")
      player_health = player_health - enemy_damage
      print(f"The remaining health of player is: {player_health}")
      # healing the player if its health is less then 50
      if player_health < 50:
          player_health += healings
          print(f"Player gain {healings} health points. New player health is: {player_health}")
      
      while player_health > 0 and enemy_health > 0:
            round_x()
            fight()

   else:
      print("Enemy Defeated.")
      inc_gold() 
      inc_xp()  
      levelup_xp_req()
      level_up()
          

      

# how much XP is needed to level up? Let's say 100 XP is needed to level up.


# fight()
# inc_gold()
# 
# print("Name:",npc1.name,"| Level:",npc1.level, "| XP:",npc1.xp, "| Wins:",npc1.wins, )
# print(l1.name, l1.x_axis, l1.y_axis)
# print(l1.name)

# right()


# Challenge 49: Save player data to a file.
# 1. Define your player data in a dictionary
player_data = {
    "username": p1.name,
    "level": p1.level,
    "gold": player_gold,
    "damage": player_damage,
    "health": player_health,
    "inventory": inventory_list
}
# 2. Open a new file in write mode ('w') and save the data
with open("save_game.json", "w") as file:
    json.dump(player_data, file, indent=4)

print("Player data saved successfully!")

# Challenge 50: Load saved data.
# Open and load the JSON file....syntax
with open("save_game.json", "r") as file:
    data = json.load(file)
# The data is now a standard Python dictionary or list
print(data)

# Challenge 51: Add a boss battle.
print("GET READY FOR THE BOSS BATTLE")
input("Press Enter to attack")
enemy_health -= player_damage

print(f"{spawn_enemy.name} attacks you!")

player_health -= spawn_enemy.damage
print(f"You took {spawn_enemy.damage} damage! Health is now {player_health}.")


print(x)