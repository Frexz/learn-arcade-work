# Creates the Room class with title, description, and which rooms it connects to
class Room:
    def __init__(self, title, descr, n, ne, w, s, e):
        self.title = title
        self.description = descr
        self.north = n
        self.northeast = ne
        self.west = w
        self.south = s
        self.east = e


def create_rooms():
    # Builds a list containing instances of every room in the dungeon
    room_list = []
    room = Room(title="THE CELLAR",
                descr="The door opens onto a five-foot-wide landing fifteen feet above a large cellar, with stone\n"
                      "steps descending to the floor in two short flights. Another door stands beneath the stairs to\n"
                      "the north. A large stone cistern occupies the western part of the room, whose walls are lined\n"
                      "with kegs and barrels. Another door leads west.",
                n=2,
                ne=None,
                w=1,
                s=None,
                e=None)
    room_list.append(room)
    room = Room(title="BARRACKS",
                descr="This appears to be a storeroom pressed into service as living quarters. Two double bunks\n"
                      "stand against the wall near the door, while barrels and crates fill the southern half of the\n"
                      "chamber. The only door in this room is to the east where you came from.",
                n=None,
                ne=None,
                w=None,
                s=None,
                e=0)
    room_list.append(room)
    room = Room(title="HALL",
                descr="Thick dust covers the flagstones of this somber hallway. The walls are decorated with faux\n"
                      "columns every ten feet, and the double doors at the west end of the hall are sheathed in\n"
                      "copper plate, now green with age. A relief carving of a mournful angel graces the doors.\n"
                      "The door you came from returns to the south.",
                n=None,
                ne=None,
                w=3,
                s=None,
                e=None)
    room_list.append(room)
    room = Room(title="TRESENDAR CRYPTS",
                descr="Three large stone sarcophagi stand within this dusty crypt, and propped up against each\n"
                      "sarcophagus is a human skeleton clad in bits of rusty mail. False columns along the walls are\n"
                      "carved in the image of spreading oak trees. The double doors to the east corner are\n"
                      "sheathed in tarnished copper plate. Another door leads north and another northeast.",
                n=5,
                ne=4,
                w=None,
                s=None,
                e=2)
    room_list.append(room)
    room = Room(title="SLAVE PENS",
                descr="This long room is partitioned into three areas, with iron bars walling off the north and\n"
                      "south. Filthy straw lines the floors of those cells, the hinged doors of which are secured by\n"
                      "chains and padlocks. A pair of disheveled human women are held in the cell to the south,\n"
                      "while a human boy is confined to the north. All are dressed in plain gray tunics and have\n"
                      "iron collars fitted around their necks. A heap of discarded clothing is piled carelessly\n"
                      "against the far wall. The door you came from leads west.",
                n=None,
                ne=None,
                w=3,
                s=None,
                e=None)
    room_list.append(room)
    room = Room(title="HALLWAY",
                descr="A small, short hallway features a door to the east. The door you came from returns south.",
                n=None,
                ne=None,
                w=None,
                s=3,
                e=6)
    room_list.append(room)
    room = Room(title="ARMORY",
                descr="Racks of weapons line the walls of this chamber, including spears, swords, crossbows,\n"
                      "and bolts. A dozen dirty red cloaks hang from hooks by the door. The door you came from\n"
                      "returns west.",
                n=None,
                ne=None,
                w=5,
                s=None,
                e=None)
    room_list.append(room)
    return room_list


def game_loop(room_list):
    # Creates a variable for the current room and set it to 0
    current_room = 0

    # Creates a game loop
    while True:
        print()
        print(room_list[current_room].title)
        print(room_list[current_room].description)
        print()

        # Asks the user for input on which direction to proceed
        choice = input("Which direction would you like to proceed? Type \"Q\" or \"Quit\" to exit the program ")

        # Checks if user wants to quit the game
        if choice.lower() == "q" or choice.lower() == "quit":
            exit()

        # Checks if north is available direction and moves north
        if choice.lower() == "n" or choice.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        # Checks if norteast is available direction and moves northeast
        elif choice.lower() == "ne" or choice.lower() == "northeast":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        # Checks if west is available direction and moves west
        elif choice.lower() == "w" or choice.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        # Checks if south is available direction and moves south
        elif choice.lower() == "s" or choice.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        # Checks if east is available direction and moves east
        elif choice.lower() == "e" or choice.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        # This prints if the input is not valid input
        else:
            print()
            print("Invalid choice.")


def main():
    # Creates the rooms and returns the list of room instances
    room_list = create_rooms()

    # Initiates the game loop
    game_loop(room_list)


main()
