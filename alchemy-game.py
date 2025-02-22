import random

class Banisher:
    def __init__(self, name, weapon, defense, foe, elixirs=3, manna=10):
        self.name = name
        self.weapon = weapon
        self.defense = defense
        self.elixirs = elixirs
        self.manna = manna
        self.foe = foe

    def attack(self):
        attack_choice = input(f"{self.name}, choose your attack ({self.weapon}/elixir): ").strip().lower()

        if attack_choice == self.weapon:
            damage = 2  # Example fixed damage for weapon attack
            if self.weapon == 'sword':
                print(f"{self.name} slashes the {self.foe.element} elemental with their sword!\n")
            else:
                print(f"{self.name} shoots an arrow at the {self.foe.element} elemental! \n")
            self.foe.manna -= damage
        elif attack_choice == 'elixir' and self.elixirs > 0:
            print(f"{self.name} throws an elixir at the {self.foe.element} elemental! -1 Damage\n")
            self.foe.manna -= 2 
            self.elixirs -= 1
        else:
            print("Invalid choice or no elixirs left.\n")
            return False
        
        if self.foe.manna <= 0:
            print(f"The {self.foe.element} elemental has been defeated!\n")
            return True
        return False

    def defend(self):
        if self.defense == 'armor':
            print(f"{self.name} defends with armor, reducing damage!\n")
            self.manna += 1
        elif self.defense == 'shield':
            print(f"{self.name} defends with a shield, blocking the attack!\n")
            self.manna += 1
        else:
            print("Invalid defense choice.\n")

    def __repr__(self):
        return (f"Banisher(name={self.name}, weapon={self.weapon}, elixirs={self.elixirs}, \n"
                f"manna={self.manna}, foe={self.foe.element if self.foe else None})")


class Elemental:
    def __init__(self, element, foe, manna=10):
        self.element = element
        self.manna = manna
        self.foe = foe

    def attack(self):
        attacks = ['fire', 'water', 'earth', 'air']
        chosen_attack = random.choice(attacks)
        print(f"The {self.element} elemental attacks with {chosen_attack}! \n")

        damage = 1  # Example fixed damage for elemental attacks
        self.foe.manna -= damage
        print(f"The {self.element} elemental causes {damage} damage to {self.foe.name}. \n")
        self.foe.defend()
        if self.foe.manna <= 0:
            print(f"{self.foe.name} has been defeated! \n")
            return True
        return False

    def __repr__(self):
        return f"Elemental(element={self.element}, manna={self.manna}, foe={self.foe.name}) \n"


# Game setup
def start_game():
    player_name = input("Enter your name, brave Banisher: ")
    random_element = random.choice(["earth", "fire", "air", "water"])
    
    weapon = ''
    while weapon not in ['sword', 'longbow']:
        weapon = input("Choose your weapon, brave Banisher (sword/longbow): ").strip().lower()
    
    defense = ''
    while defense not in ['shield', 'armor', 'elixir']:
        defense = input(f"Choose your defense (shield/armor): ").strip().lower()
    
    banisher = Banisher(player_name, weapon, defense, foe=None)
    elemental = Elemental(random_element, foe=banisher)
    banisher.foe = elemental
    
    print(f"\nWelcome, {banisher.name}! You are up against a {elemental.element.title()} elemental. \n")
    
    while True:
        if banisher.attack():
            break
        if elemental.attack():
            break
        
        # Print current states after each round
        print(f"\nCurrent state:\n{banisher}\n{elemental} \n")

start_game()
