import random

class Banisher:
    def __init__(self, name, weapon, elixirs, manna, foe):
        self.name = name
        self.weapon = weapon
        self.elixirs = elixirs
        self.manna = 10 if manna is None else manna
        self.foe = foe

    def attack(self):
        attack_choice = input(f"{self.name}, choose your attack (sword/elixir): ").strip().lower()

        if attack_choice == 'sword':
            print(f"{self.name} slashes the {self.foe.element} elemental with their sword!")
            self.foe.manna -= 1
        elif attack_choice == 'elixir' and self.elixirs > 0:
            print(f"{self.name} throws an elixir at the {self.foe.element} elemental!/n -1 Damage")
            self.foe.manna = 0
            self.elixirs -= 1
        else:
            print("Invalid choice or no elixirs left.")
        
        if self.foe.manna <= 0:
            print(f"The {self.foe.element} elemental has been defeated!")
            return True
        return False

    def defense(self):
        defense_choice = input(f"{self.name}, choose your defense (shield/armor/)")
        if defense_choice = ''

    def __repr__(self):
        return (f"Banisher(name={self.name}, weapon={self.weapon}, elixirs={self.elixirs}, "
                f"manna={self.manna}, foe={self.foe.element if self.foe else None})")


class Elemental:
    def __init__(self, element, manna, foe):
        self.element = element
        # Fixing the condition to check if manna is None
        self.manna = 10 if manna is None else manna
        self.foe = foe

    def attack(self):
        attacks = ['fire', 'water', 'earth']
        chosen_attack = random.choice(attacks)
        print(f"The {self.element} elemental attacks with {chosen_attack}!")
        
        if chosen_attack == 'fire':
            print(f"The fire elemental burns {self.foe.name}.")
            self.foe.manna -= 1
        elif chosen_attack == 'water':
            print(f"The water elemental drenches {self.foe.name}.")
            self.foe.manna -= 1
        elif chosen_attack == 'earth':
            print(f"The earth elemental shakes the ground beneath {self.foe.name}.")
            self.foe.manna -= 2
        
        if self.foe.manna <= 0:
            print(f"{self.foe.name} has been defeated!")
            return True
        return False

    def __repr__(self):
        return f"Elemental(element={self.element}, manna={self.manna}, foe={self.foe.name})"


# Game setup
def start_game():
    # Create the player (Banisher) and the foe (Elemental)
    player_name = input("Enter your name, brave Banisher: ")
    banisher = Banisher(player_name, 'sword', elixirs=3, manna=10, foe=None)
    elemental = Elemental('fire', 10, foe=banisher)
    banisher.foe = elemental
    
    print(f"\nWelcome, {banisher.name}! You are up against a {elemental.element} elemental.")
    print(f"Banisher state: {banisher}")
    print(f"Elemental state: {elemental}")
    
    while True:
        if banisher.attack():
            break
        if elemental.attack():
            break

start_game()