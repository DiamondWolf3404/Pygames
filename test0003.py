class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []


class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def add_points(self, points_to_add):
        self.points += points_to_add

    def get_multiplier(self):
        multiplier = 1
        for item in self.inventory:
            if hasattr(item, 'multiplier'):
                multiplier *= item.multiplier
        return multiplier


class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable


class Game(object):
    def __init__(self):
        # Create items
        # Closet items
        self.shelf = Item("shelf", "The shelf is empty.", False)
        self.uniform = Item("uniform", "The uniform is blue and drab.", True)

        # Control room items
        self.guard = Item("guard", "The guard looks mean and menacing.", False)
        self.electronic_lock = Item("lock", "The lock is in front of a large door to the east.", "False")
        self.id = Item("id", "The id is silver with a barcode on it.", True)

        # Airlock items
        self.spacesuit = Item("spacesuit", "The spacesuit looks old, but safe.", True)
        self.button = Item("button", "The big red button has a warning symbol on it.", False)

        # Create rooms
        # Closet
        self.closet = Room("The Closet",
                           "You are in a small, nondescript closet. There is a shelf and a uniform inside.")
        self.closet.items.append(self.shelf)
        self.closet.items.append(self.uniform)

        # Control room
        self.control_room = Room("The Control Room",
                                 "You are in a small room that looks like it controls something. There is an airlock to the east and a guard standing in the corner.")
        self.control_room.items.append(self.guard)
        self.control_room.items.append(self.electronic_lock)
        self.control_room.items.append(self.id)

        # Airlock
        self.airlock = Room("The Airlock",
                            "You are in a small room that is clearly an airlock. There is a window to space in the east. There is an airlock door to the west.")
        self.airlock.items.append(self.spacesuit)
        self.airlock.items.append(self.button)

        # Create exits
        self.closet.exits["east"] = self.control_room
        self.control_room.exits["west"] = self.closet
        self.control_room.exits["east"] = self.airlock
        self.airlock.exits["west"] = self.control_room

        # Create the player
        self.player = Player("The Player", self.closet)

    def start(self):
        print("Welcome to My Space Adventure")
        print("\nYou wake up on a space station.")

        while True:
            print("\nYou are currently in {}.".format(self.player.location.name))
            print(self.player.location.description)
            print("\nHere are the exits: ")
            for direction, room in self.player.location.exits.items():
                print("  {}: {}".format(direction, room.name))
            print("\nYou see the following items: ")
            for item in self.player.location.items:
                print("  {}".format(item.name))
            command = input("\nEnter a command (or 'help' for a list of commands): ")

            words = command.split()
            if len(words) > 0:
                verb = words[0]
            if len(words) > 1:
                noun = words[1]

            self.process_command(verb, noun)

    def process_command(self, verb, noun):
        # Help
        if verb == "help":
            print("\nCommands:")
            print("  go <direction>")
            print("  examine <item>")
            print("  get <item>")
            print("  drop <item>")
            print("  inventory")

        # Go
        elif verb == "go":
            if noun in self.player.location.exits:
                self.player.location = self.player.location.exits[noun]
                print("\nYou go {}.".format(noun))
            else:
                print("\nYou can't go that way.")

        # Examine
        elif verb == "examine":
            if noun in [item.name for item in self.player.location.items]:
                for item in self.player.location.items:
                    if item.name == noun:
                        print("\n{}".format(item.description))
            else:
                print("\nThere is no item called '{}' in this room.".format(noun))

        # Get
        elif verb == "get":
            if noun in [item.name for item in self.player.location.items]:
                for item in self.player.location.items:
                    if item.name == noun:
                        # Check if it's movable
                        if item.is_movable:
                            print("\nYou take the {}".format(item.name))
                            # Remove from room
                            self.player.location.items.remove(item)
                            # Add to player's inventory
                            self.player.inventory.append(item)
                        else:
                            print("\nSorry, you can't move that.")
            else:
                print("\nThere is no item called '{}' in this room.".format(noun))

        # Drop
        elif verb == "drop":
            if noun in [item.name for item in self.player.inventory]:
                for item in self.player.inventory:
                    if item.name == noun:
                        print("\nYou drop the {}".format(item.name))
                        # Remove from inventory
                        self.player.inventory.remove(item)
                        # Add to room
                        self.player.location.items.append(item)
            else:
                print("\nYou don't have an item called '{}' in your inventory.".format(noun))

        # Inventory
        elif verb == "inventory":
            if len(self.player.inventory) > 0:
                print("\nYou have the following items in your inventory:")
                for item in self.player.inventory:
                    print("  {}".format(item.name))
            else:
                print("\nYour inventory is empty.")

        else:
            print("\nI'm sorry, I didn't understand that command.")


# Create the game
game = Game()

# Start the game
game.start()