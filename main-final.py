# ------------------------------------------------------------------> PHASE 0 - RULES
# PYTHON LEARNING PROJECT
# Project Title: Build Your Own Text-Based Adventure Game

# Goal:
# Instead of solving random exercises, you'll slowly build one large game. 
# Every challenge adds a new feature while teaching an important Python concept.

# Rule:
# Do NOT skip challenges.
# Every challenge should work before moving to the next one.


# ------------------------------------------------------------------> PHASE 1 — VARIABLES  (Challenges 1–5)
# Challenge 1: Create variables for player_name, player_health, player_gold, player_level and print them in a nice format.
player_name = "Hero"
player_health = 30
player_gold = 1003
player_level = 5
print(" Players Name:", player_name, "\n", "Player's Gold:", player_gold, "\n", "Player's Level:", player_level, "\n", "Player's Health:", player_health)

# Challenge 2:
# Ask the player for their name using input(), store it and welcome them.
player_name = input("Player enter your name here :")
print("Welcome the player: ", player_name)
print("Hi! Your Name is: ", player_name)

# Challenge 3:
# Create damage and healing variables, update player_health with arithmetic.
player_damage = 10
enemy_damage = 20
healing = 30
player_health -= enemy_damage 
player_health += healing
print("Remaining Health of player is :", player_health)

# Challenge 4:
# Give the player gold after defeating an enemy using +=
enemy_health = 40
player_gold += enemy_health
print("players gold increased to :", player_gold)

# Challenge 5:
# Practice comparison operators – check if player is alive and if rich.
if player_health < 1:
    print("Player is Dead")
else:
    print("Player is alive.")

if player_gold > 100:
    print("Player is rich")
else:
    print("Poor Player plz topup")

# ------------------------------------------------------------------> PHASE 2 — IF STATEMENTS  (Challenges 6–9)
# Challenge 6: If player_health is 0 or below print "Game Over", else "You survived"
if player_health <= 0:
    print("Game Over")
else:
    print("You survived")

# Challenge 7:
# Create a shop: buy a sword if gold is enough.
sword = 400
if player_gold > sword:
    print("You can Buy a Sword.", "\n", "Your current Gold is :", player_gold)
    input("Press enter to buy")
    player_gold = player_gold - sword
    print("Congrates! You has a new Sword.", "\n", "Your current Gold is :", player_gold)
else:
    print("Oh! Not enough gold")

# Challenge 8:
# Ask the player to choose a place: Forest, Cave, or Village.
print(player_name, "please choose a place")
x = int(input("1) Forest. 2)Cave. 3)Village."))
if x == 1:
    print("You selected Forest place")
elif x == 2:
    print("You selected Cave place")
elif x == 3:
    print("You selected Village place")
else:
    print("Wrong Input, Try Again Plz")

# Challenge 9:
# Add difficulty levels (Easy, Medium, Hard) with different enemy damage.
print("Select your difficulty level :")
x = (input("a)Easy. b)Medium. c)Hard."))
if x == "a":
    print("You Selected Easy Level.")
elif x == "b":
    print("You Selected Medium Level.")
elif x == "c":
    print("You Selected Hard Level.")


# ------------------------------------------------------------------> PHASE 3 — LOOPS  (Challenges 10–15)
# Challenge 10: Print numbers 1 to 10 using a for loop.
print("Print numbers 1 to 10 using a for loop.")
for i in range(1, 11):
    print(i)

# Challenge 11:
# Print every item in an inventory list.
item = ["sword", "shield", "potion", "skills", "luck", "armor", "gold",
        "health", "care", "Strength"]
print("Inventory:", item)

# Challenge 12:
# Create a countdown from 10 to 1.
for i in range(10, 0, -1):
    print(i)
print("Done")

# Challenge 13:
# Create a while loop that keeps asking "Attack or Run?" until "run".
while True:
    x = input("attack or run?")
    if x == "attack":
        print("Player", x)
        continue
    elif x == "run":
        break

# Challenge 14: Make a healing station – heal player until health reaches 100.
while player_health < 100:
    print("Your current health is ,", player_health)
    input("Press Enter to heal yourself, Survival")
    for player_health in range(player_health, 110, 10):
        print("You are healling now", "Your curent health is ", player_health)
print("You are Healed", player_health, "% successfully ")

# Challenge 15: Create a battle loop – while enemy health > 0, attack and enemy attacks back.
input("Press enter to Start Battle: ")
print("Enemies Curent health is ", enemy_health)
print("The Battle Begins")
x = 0
while enemy_health > 0:
    if x < 5:
        x = x + 1
        print("Round no.", x)
    input("Press enter to Damage Enemy: ")
    enemy_health = enemy_health - player_damage
    print("Enemy health left is ", enemy_health)
    if enemy_health > 0:
        print("Now Enemy Attacks back")
        player_health = player_health - enemy_damage
    else:
        print("Enemy has 0 health.")
    print("Remaining Player Health is:", player_health)
    continue
else:
    print("Enemy is Defeated")


# ------------------------------------------------------------------> PHASE 4 — FUNCTIONS  (Challenges 16–21)
# Challenge 16: Create a function that prints a welcome message.
def greet_player():
    
    print("Welcome!!", player_name)
greet_player()

# Challenge 17:
# Create attack() that returns damage.
def attack():
    print("Attack gives", player_damage, "damage to enemy")
attack()

# Challenge 18:
# Create heal(current_health) that returns updated health.
def heal(player_health=50):
    print("players health before healing is:", player_health)
    player_health += healing
    return (player_health)
print("updated health of player is:", heal(player_health))

# Challenge 19:
# Create battle(player_health, enemy_health) that simulates one round.
def battle(player_health=80, enemy_health=60):
    print("the 2nd battle Begins here")
    x = 1
    print("Round no.", x)
    print("enemy health is:", enemy_health)
    input("Press Enter to attack enemy")
    enemy_health -= player_damage
    print("enemy health left:", enemy_health)
    print("ENEMY ATTACKS BACK")
    player_health -= enemy_damage
    print("player health is", player_health)
    return (player_health, enemy_health)
print("Round one of battle ended with:", battle())

# Challenge 20: Create level_up(level) that returns the next level.
def level_up(level=0):
    print("Player level was:", level)
    level = level + 1
    return (level)
print("Now, player level is:", level_up())

# Challenge 21: Move ALL repeated code into functions

# ------------------------------------------------------------------> PHASE 5 — LISTS  (Challenges 22–26)
# Challenge 22: Create an inventory list and return it from a function.
def inventory():
    inventory_list = ["sword", "shield", "heal", "skill", "luck",
                      "armor", "gold", "health"]
    return (inventory_list)
print("Inventory items are:", inventory())

# Challenge 23: Allow the player to collect items (e.g., gold).
def collect_items(player_gold=1100):
    print("player can collect items while playing.")
    print("player gold is:", player_gold)
    player_gold += 100
    return (player_gold)
print("player earns golds", collect_items())

# Challenge 24: Print inventory using a loop.
def inventory_items():
    x = 0
    while True:
        if x < 1:
            print("inventory items are:")
            x = x + 1
            print(inventory())
            break
# inventory_items()   
for x in inventory():
    print(x)

# Challenge 25: Remove used items by index.
print("now we are going to remove items")
print("total number of items are:", len(item))
x = int(input("enter any index number to remove an item (0 ~ 9):"))
print("your selected number is:", x)
print("we are removing this from items(list):", item[x])
item.pop(x)
print(item)

# Challenge 26: Create a backpack limit (max 10 items).
backpack = item
x = len(backpack)
while x < 10:
    print("backpack has occopied space of ", x, "items.")
    y = str(input("add a new item here :"))
    if y == "":
        print("try again")
    else:
        backpack.append(y)
        x = len(backpack)
        print("item added sucessfully.")
        print("updated inventory items are :", backpack)
        continue
else:
    print("backpack is full buddy")
    print(backpack)
    print(x, "total maximum number of items achieved.")

# ------------------------------------------------------------------> PHASE 6 — DICTIONARIES  (Challenges 27–30)
# Challenge 27: Store player stats inside a dictionary.
player_dict = {
    "Player health": player_health,
    "Player gold": player_gold,
    "Player level": player_level,
    "Player damage": player_damage
}
print("player_dict:", player_dict)

# Challenge 28: Store enemy information in another dictionary.
enemy_name = "jack"
enemy_dict = {
    "Enemy Name": enemy_name,
    "Enemy Health": enemy_health,
    "Enemy Damage": enemy_damage,
    "Enemy of Level": player_level
}
print("enemy_dict:", enemy_dict)

# Challenge 29: Create multiple enemies using a list of dictionaries.
enemies_list = [
    {1: "Enemy_1", "name": "Heihachi Mishima", "Enemy Health": 20,
     "Enemy Damage": enemy_damage, "Enemy of Level": player_level},
    {2: "Enemy_2", "name": "Kazuya Mishima", "Enemy Health": 20,
     "Enemy Damage": enemy_damage, "Enemy of Level": player_level},
    {3: "Enemy_3", "name": "Akuma", "Enemy Health": 20,
     "Enemy Damage": enemy_damage, "Enemy of Level": player_level},
    {4: "Enemy_4", "name": "Jin", "Enemy Health": 20,
     "Enemy Damage": enemy_damage, "Enemy of Level": player_level},
    {5: "Enemy_5", "name": "Devil Jin", "Enemy Health": 20,
     "Enemy Damage": enemy_damage, "Enemy of Level": player_level}
]
for x in enemies_list:
    print(x)

# Challenge 30: Search for a specific enemy by name.
x = -1
while x < 5:
    x += 1
    enemy_names = enemies_list[x]["name"] 
    print("Hello!", enemy_names)
    if x < 4:
        continue
    elif x == 4:
        print("list ends")
        break

# Now implement the search.
name_found = False
x = input("Search Full Name of Enemy Here by typing:")
print("Your intered name is:", x)
index = -1
while index < 4:
    index += 1
    enemy_name = enemies_list[index]["name"]
    if x == enemy_name:
        print("We found ", enemy_name)
        enemy_index = enemies_list[index][index + 1]
        print("Title of enemy is:", enemy_index)
        enemy_health = enemies_list[index]["Enemy Health"]
        print("Enemy Health is:", enemy_health)
        enemy_damage = enemies_list[index]["Enemy Damage"]
        print("Enemy Damage is:", enemy_damage)
        enemy_level = enemies_list[index]["Enemy of Level"]
        print("Enemy level for Player is", enemy_level)
        name_found = True
        break

if name_found == False:
    print("Data is not Found in list, so")
    print("Retry Next time with these names;")
    print(enemies_list[0]["name"])
    print(enemies_list[1]["name"])
    print(enemies_list[2]["name"])
    print(enemies_list[3]["name"])
    print(enemies_list[4]["name"])


# ------------------------------------------------------------------> PHASE 7 — CLASSES  (Challenges 31–36)
# Challenge 31: Create a Player class (simple – attributes only).
class player_attributes:
    name = str("player_1")
    health = int(79)
    gold = int(405)
    level = int(3)
print(player_attributes.name)

# Challenge 32:
# Add methods to the Player class (attack, heal, show_stats).
class Player:
    # Class variable (not used directly)
    player_health = 49

    def __init__(self, damage, heals, level, kills, survival, wins):
        self.damage = damage
        self.heals = heals
        self.level = level
        self.kills = kills
        self.survival = survival
        self.wins = wins
        self.player_health = 49

    def attack(self):
        print("Player is Attacking to Enemy. The damage it gives:", self.damage)
        self.player_health -= self.damage
        print("Player health after attack:", self.player_health)

    def heal(self):
        print("Player is Healing now.")
        self.player_health += self.heals
        print("player health is :", self.player_health)

    def show_stats(self):
        print("Stats of player are:")
        print(self.damage)
        print(self.heals)
        print(self.level)
        print(self.kills)
        print(self.survival)
        print(self.wins)

p1 = Player(20, 30, 2, 23, 45, 13)
print(p1.attack())
print(p1.heal())
print(p1.show_stats())

# Challenge 33: Create an Enemy class.
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

# Challenge 34: Create several enemy objects.
e1 = Enemy("Jack-Alpha", 70, 5)
e2 = Enemy("Mishima", 30, 15)
e3 = Enemy("Rogue G", 45, 10)
e4 = Enemy("Tekken Force", 50, 5)

# Challenge 35: Make Player fight Enemy objects – using inheritance and a Fight class.
class Fight:
    @staticmethod
    def start():
        print("Battle Begins..")

    @staticmethod
    def stop():
        print("Battle ended..")

class Player(Fight):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

player1 = Player("Ash", 20)

Fight.start()

class Enemy(Fight):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

enemy1 = Enemy("Mishima", 30)
enemy2 = Enemy("Rogue", 25)
enemy3 = Enemy("Alpha", 15)

print("Round no. 1")
print(player1.name, "is Attacking Now.")
print("it gives ", player1.damage, "damage")
print("Now Enemy", enemy1.name, "attacks back")
print("It gives", enemy1.damage, "damage to player.")

print("Round no. 2")
print(player1.name, "is Attacking Now.")
print("it gives ", player1.damage, "damage")
print("Now Enemy", enemy2.name, "attacks back")
print("It gives", enemy2.damage, "damage to player.")

print("Round no. 3")
print(player1.name, "is Attacking Now.")
print("it gives ", player1.damage, "damage")
print("Now Enemy", enemy3.name, "attacks back")
print("It gives", enemy3.damage, "damage to player.")

Fight.stop()

# Challenge 36:
# Add experience points – Player levels up after enough XP.

# ------------------------------------------------------------------> PHASE 8 — ADVANCED CLASSES  (Challenges 37–41)
# Challenge 37: Create a Weapon class.
# Challenge 38: Player can equip different weapons.
# Challenge 39: Weapon changes attack damage.
# Challenge 40: Create an Item class.
# Challenge 41: Use inheritance (Item, Potion, Weapon, Armor).

# ------------------------------------------------------------------> PHASE 9 — GAME WORLD  (Challenges 42–47)
# Challenge 42: Create multiple locations.
# Challenge 43: Allow player movement (north, south, east, west).
# Challenge 44: Randomly spawn enemies.
# Challenge 45: Add treasure chests.
# Challenge 46: Add NPC characters.
# Challenge 47: NPCs can give quests.

# ------------------------------------------------------------------> PHASE 10 — POLISH  (Challenges 48–54)
# Challenge 48: Create a game menu (Start, Load, Exit).
# Challenge 49: Save player data to a file.
# Challenge 50: Load saved data.
# Challenge 51: Add a boss battle.
# Challenge 52: Add victory and defeat endings.
# Challenge 53: Refactor your entire project.
# Challenge 54: Final boss – rebuild from scratch.

# ------------------------------------------------------------------> FINAL PHASE - Full implementation of Challenges 36–54
# This section contains a more advanced, compact version of
# the game, with NPCs, quests, a full battle system, leveling,
# save/load, and a boss battle.
import random
import json

# ------------------------------------------------------------------
# Challenge 36-1: Add experience points.
# Re‑initialise core game variables (these override the earlier ones
# for this second part of the script).
# ------------------------------------------------------------------
player_health = 100          
player_gold = 500            
player_damage = 20          
inventory_list = ["sword", "shield", "heal", "skill", "luck",
                  "armor", "gold", "health"]

# Enemy default stats (used as fallback)
enemy_health = 100
enemy_damage = 20

# Game constants
increase_xp = 50             
increase_gold = 100          
level_up_xp = 100            
level_up_xp_l2 = 200         
healings = 30                

# Internal counters
x = 1                        
fight_won = False            

# Challenge 36-2: Player class with name, level, XP, and wins.
class Player:
    def __init__(self, name, level, xp, wins):
        self.name = name      
        self.level = level    
        self.xp = xp          
        self.wins = wins      

# Create the player with starting values.
p1 = Player("Ash", 0, 50, 1)
print("Name:", p1.name, "| Level:", p1.level,
      "| XP:", p1.xp, "| Wins:", p1.wins)


# Challenge 46: Add NPC characters.
class Npcs(Player):
    def __init__(self, name, level):
        super().__init__(name, level, xp=0, wins=0)

npc1 = Npcs("Mr.Victor", 3)  
npc2 = Npcs("Pikachu", 5)    
npc3 = Npcs("Serena", 2)     
npc4 = Npcs("Leo", 6)        


# Challenge 47: NPCs can give quests.
def quests():
    print("Move Around in this High End Graphic Game Map.")
    print(f"|a)Do you want to visit: {npc1.name} ")
    print(f"|b)Do you want to visit: {npc2.name} ")
    print(f"|c)Do you want to visit: {npc3.name} ")
    print(f"|d)Do you want to visit: {npc4.name} ")
    Npc = input("Choose a weapon to equip (a/b/c/d): ")
    if Npc == "a":
        print(f"You have visited {npc1.name}. Your Quest is to...")
    elif Npc == "b":
        print(f"You have visited {npc2.name}. Your Quest is to....")
    elif Npc == "c":
        print(f"You have visited {npc3.name}. Your Quest is to...")
    elif Npc == "d":
        print(f"You have visited {npc4.name}. Your Quest is to...")


# Challenge 37, 40, 41: Item hierarchy using inheritance.| Base class: Item.| Child classes: Potion, Weapon, Armor.
class Item:
    def __init__(self, name):
        self.name = name
class Potion(Item):
    def __init__(self, name, cost, heal):
        self.name = name
        self.cost = cost
        self.heal = heal
class Weapon(Item):
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage
class Armor(Item):
    def __init__(self, name, cost, protect):
        self.name = name
        self.cost = cost
        self.protect = protect

# Create specific item instances.
po1 = Potion("Healing Potion", 200, 50)  
po2 = Potion("Elixir", 300, 50)          

w1 = Weapon("Knife", 400, 50)            
w2 = Weapon("Sword", 500, 100)           
w3 = Weapon("Dagger", 600, 150)          
w4 = Weapon("Shotgun", 700, 200)         

a1 = Armor("helmet", 100, 30)           
a2 = Armor("shield", 200, 50)           

# Challenge 42: Create multiple locations.
class Locations():
    def __init__(self, name="Default", x_axis=0, y_axis=0):
        self.name = name
        self.x_axis = x_axis
        self.y_axis = y_axis

l1 = Locations("East", 1, 0)    # Increase x
l2 = Locations("West", -1, 0)   # Decrease x
l3 = Locations("North", 0, -1)  # Decrease y
l4 = Locations("South", 0, 1)   # Increase y

# Challenge 43: Allow player movement (north, south, east, west).

def right():
    print("Player moves", l1.name, l1.x_axis, l1.y_axis)

def left():
    print("Player moves", l2.name, l2.x_axis, l2.y_axis)

def up():
    print("Player moves", l3.name, l3.x_axis, l3.y_axis)

def down():
    print("Player moves", l4.name, l4.x_axis, l4.y_axis)

# Challenge 44: Randomly spawn enemies.
class Enemy:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

enemy1 = Enemy("Mishima", 30)   
enemy2 = Enemy("Rogue", 25)     
enemy3 = Enemy("Alpha", 15)     
enemies = [enemy1, enemy2, enemy3]

spawn_enemy = random.choice(enemies)   # Pick a random enemy
print(f"Spawned: {spawn_enemy.name} with {spawn_enemy.damage} damage")

# Challenge 45: Add treasure chests.
def treasure():
    global player_gold
    player_gold += increase_gold
    print("You got", increase_gold, "gold coins from Treasure chest.")

# Challenge 52: Add victory and defeat endings.
def matchEvents():
    if player_health > enemy_health:
        print(f"Victory! Enemy Defeated.")
    elif player_health < enemy_health:
        print(f"The End! Player Defeated, Try Next Time")
    else:
        print("Draw Fight")

# Challenge 48: Create a game menu (Start, Load, Exit).
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

# Begin the game sequence. STARTs HEre
input("Press Enter to signIn")   
treasure()                      
print("Hi", p1.name)            
quests()    #signIn reward call                      

# Challenge 38 & 39: Player can equip different weapons, increases the player's damage.
print("Available weapons are:")
print(f"|a)Weapon: {w1.name}, Damage: {w1.damage} ")
print(f"|b)Weapon: {w2.name}, Damage: {w2.damage} ")
print(f"|c)Weapon: {w3.name}, Damage: {w3.damage} ")
print(f"|d)Weapon: {w4.name}, Damage: {w4.damage} ")
weapon_equipped = input("Choose a weapon to equip (a/b/c/d): ")
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

# Battle system helper functions.
def round_x():
    global x
    x += 1
    return x

def levelup_xp_req():
    xp_needed = level_up_xp - p1.xp
    print(f"XP remains for levelup is {xp_needed}")

def inc_gold():
    global player_gold
    if player_health > 0:
        player_gold += increase_gold
        print(f"Gold received after defeating enemy: {player_gold}")

def inc_xp():
    global fight_won
    while player_health > 0:
        fight_won = True
        if fight_won:
            p1.xp += increase_xp
            print("XP increased after defeating enemy is 50, Total:", p1.xp)
            break
    else:
        print("You lose! Try Again next time.")

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
        xp_needed = level_up_xp - p1.xp
        print(f"Still needs {xp_needed} XP for levelup")

# Challenge 36 & 51: Main fight and boss battle.
def fight():
    global enemy_damage, enemy_health, player_health, player_damage, x
    print("battle starts")
    print("Round no", x)

    # Player attacks
    input("Press Enter to Start Fighting")
    print(f"Player Attacks, it gives {player_damage} damage to enemy.")
    enemy_health -= player_damage
    print(f"The remaining health of enemy is : {enemy_health}")

    # Enemy attacks back if alive
    if enemy_health > 0:
        print(f"Now enemy attacks back. It gives {enemy_damage} damage to the player.")
        player_health = player_health - enemy_damage
        print(f"The remaining health of player is: {player_health}")

        # Auto‑heal if health < 50
        if player_health < 50:
            player_health += healings
            print(f"Player gain {healings} health points. New player health is: {player_health}")

        # Continue fighting while both are alive
        while player_health > 0 and enemy_health > 0:
            round_x()
            fight()
    else:
        # Enemy defeated – award gold, XP, and check for level‑up
        print("Enemy Defeated.")
        inc_gold()
        inc_xp()
        levelup_xp_req()
        level_up()

# Challenge 51: Boss battle. A random enemy is spawned as the boss.
print("GET READY FOR THE BOSS BATTLE")
input("Press Enter to attack")
enemy_health -= player_damage
print(f"{spawn_enemy.name} attacks you!")
player_health -= spawn_enemy.damage
print(f"You took {spawn_enemy.damage} damage! Health is now {player_health}.")

# Challenge 49 & 50: Save / Load game data using JSON.
player_data = {
    "username": p1.name,
    "level": p1.level,
    "gold": player_gold,
    "damage": player_damage,
    "health": player_health,
    "inventory": inventory_list
}
# Challenge 49: Save player data to a file.
with open("save_game.json", "w") as file:
    json.dump(player_data, file, indent=4)
print("Player data saved successfully!")
# Challenge 50: Load saved data.
with open("save_game.json", "r") as file:
    data = json.load(file)
print("Loaded data:", data)

# If you can complete this project independently, you'll have a solid practical understanding of Python fundamentals and object-oriented programming.