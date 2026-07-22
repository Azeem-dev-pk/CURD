# Challenge 36
# 36-1. Add experience points.

# seting variables here:
player_health = 100
player_gold = 500 
player_damage = 20

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

# Challenge 37. Create a Weapon class.
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
w1 = Weapon("Knife", 5)
w2 = Weapon("Sword", 10)
w3 = Weapon("Dagger", 15)
w4 = Weapon("Shotgun", 20)

# Challenge 40. Create an Item class.
class Item ():
   def __init__(self, name, type, value, effect):
      self.name = name # name of items
      self.type = type # Gear, Consumable 
      self.value = value # (cost of item)
      self.effect = effect # heal, damage, protect (quantity)
item1 = Item("Potion", "Consumable", 100, 25)
item2 = Item("Armor", "Gear", 200, 50)
item3 = Item("Elixir", "Consumable", 300, 50)
item4 = Item("Shield", "Gear", 400, 100 )

# Challenge 41. Use inheritance.  Base class: Item,  Child classes: Potion, Weapon, Armor
      

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
      print("XP increased after defeating enemy is 100, Total:",p1.xp)
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


fight()
# inc_gold()
# 
# 

# print(x)