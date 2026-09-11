class SpiderMan:
    def attack(self) -> str:
        print("Web Shooter!")
    
    def defend(self) -> str:
        print("Spider Sense!")

# TODO: Create the BlackWidow class with attack() and defend() methods
class BlackWidow:
    def attack(self):
        print("Widow's Bite!")
    def defend(self):
        print("Acrobatic Dodge!")

# TODO: Create the battle_sequence() function
def battle_sequence(bw):
    bw.attack()
    bw.defend()


# Don't modify the code below
spider_man = SpiderMan()
black_widow = BlackWidow()

battle_sequence(spider_man)
battle_sequence(black_widow)
