'''
Day 85: Text-based RPG game.
Develop a simple text-based RPG game.
'''

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 20
        self.defense = 5
    
    def is_alive(self):
        return self.health > 0
    
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def is_alive(self):
        return self.health > 0 

    def take_damage(self, damage):
        self.health -= damage
        
def battle(hero, enemy):
    print(f"A wild {enemy.name} appears!")

    while hero.is_alive() and enemy.is_alive():
        print(f"\n{hero.name}'s Health: {hero.health}, {enemy.name}")
        print("1. Attack\n2. Defend\n3. Run")

        choice = input("What will you do? (1/2/3): ")

        if choice == "1":
            damage = max(hero.attack - enemy.attack, 0)
            enemy.take_damage(damage)
            print(f"You attack the {enemy.name} for {damage} damage.")

        elif choice == "2":
            print(f"You defend and take less damage this turn.")
            enemy.attack -= 2

        elif choice == "3":
            print("You attempt to flee...")
            if random.choice([True, False]):
                print("You successfully escape!")
                break
            else:
                print("You failed to escape!")
                
        if enemy.is_alive():
            damage = max(enemy.attack - hero.defense, 0)
            hero.health -= damage
            print(f"The {enemy.name} attacks you for {damage} damage.")
                
        if not hero.is_alive():
            print(f"You defeated the {enemy.name}!\n")
        
def explore(hero):
        print("\nYou venture deeper into the dungeon...")
        enemy_name = random.choice(["Goblin", "Orc", "Troll"])
        enemy_health = random.randint(30,60)
        enemy_attack = random.randint(10,20)
        enemy = Enemy(enemy_name, enemy_health, enemy_attack)
        battle(hero, enemy)

def rest(hero):
        healing = random.randint(10,30)    
        hero.health += healing
        print(f"You rest and regain {healing} health. Current Health: {hero.health}")

def game():
        print("Welcome to the Dugeon Quest RPG!")
        hero_name = input("Enter your hero's name: ")
        hero = Hero(hero_name)

        while hero.is_alive():
            print("\n1. Explore \n2. Rest\n3. Exit Game")
            choice = input("What will you do? (1/2/3): ")

            if choice == "1":
                explore(hero)
            elif choice == "2":
                rest(hero)
            elif choice == "3":
                print("You exit the dungeon. Game over.")
                break

            if not hero.is_alive():
                print("Game Over. You have perished in the dungeon.")

if __name__ == "__main__":
    game()         