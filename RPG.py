import random

class Character:

    def __init__(self,name,health,allive):
        self.name = name
        self.health = health
        self.allive = True

    def basic_moment(self):
        direction = random.choice(["Nort","South","East","West"])
        print(f"The Warrtior {self.name} moves to {direction}")

    def Stats(self):
        print(f"------{self.name}------")
        print(f"Health {self.health}")
        print(f"Status {'Alive' if self.allive else 'Dead'}")

class Warrior:
    pass


# --- Testing the code ---
player1 = Warrior("Aragon", 100, 50)
player1.show_stats()     # Inherited from Character
player1.basic_movement() # Inherited from Character
player1.attack()         # Unique to Warrior