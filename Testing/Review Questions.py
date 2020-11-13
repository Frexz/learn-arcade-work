class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        print("A", self.name.lower(), "entered the room.")
def main():
    barbed_devil = Monster("Barbed Devil", 110)

main()