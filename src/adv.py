from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons
                     """),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.
"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.
"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.
"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.
"""),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare all Items

items = {
    'numchucks':        Item('Numchucks', 'Inflict high damage on close range enemies'),
    'matches':          Item('Matches', 'For lighting fires'),
    'sword':            Item('Sword', 'For battling close range enemies'),
    'rope':             Item('Rope', 'Good for climbing'),
    'knife':            Item('Knife', 'Stealthy weapon'),
    'bow':              Item('Bow', 'For distant enemies'),
    'grapple':          Item('Grapple', 'For climbing and crossing ravines'),
    'potion':           Item('Potion', 'Heals wounds') ,
    'shield':           Item('Shield', 'Defends against enemy attacks'),
    'boots':            Item('Boots', 'Travel faster'),
}

# Add Items to rooms

room['outside'].items.append(items['boots'])
room['foyer'].items.extend([items['knife'], items['matches'], items['rope']])
room['overlook'].items.extend([items['sword'], items['potion']])
room['narrow'].items.extend([items['bow'], items['grapple']])
room['treasure'].items.extend([items['numchucks'], items['shield']])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Tom', room['outside'])

print(f'\nYour quest begins at the {player.current_room.name}\n')
print(f'{player.current_room.description}')
output =  f'Available Items:'
i = 1
for item in player.current_room.items:
    output += f'\n {i}. {item.name}'
    i += 1
print(f'{output}\n')


while True:
    action_choice = input("Please enter 'move' to move to another room, 'item' to perform an item action or 'q' to quit: ")
    try:
        if action_choice == 'q':
            print("Your quest has ended")
            break
        elif action_choice == 'move':
            while True:
                direction_choice = input("Please choose a direction (n, s, e, w) or enter 'b' to choose a different action: ")
                try:
                    if direction_choice == "b":
                        break
                    elif direction_choice == "n" or direction_choice == "s" or direction_choice == "e" or direction_choice == "w":
                        direction = f"{direction_choice}_to"
                        player.current_room = getattr(player.current_room, direction)
                        print(player.current_room)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid direction")
                except AttributeError:
                    print(f"\nThere is no room in that direction. Please try again.\n")
        elif action_choice == "item":
            while True:
                item_choice = input("Please enter 'take [item name]' to pick up an item, 'drop [item name]' to drop an item or 'b' to choose a different action: " ).lower().split(" ")
                try:
                    if item_choice[0] == "b":
                        break
                    elif len(item_choice) != 2:
                        raise ValueError
                    elif item_choice[0] == "take":
                        item = items[item_choice[1]]
                        item.on_take(player, player.current_room)
                        break
                    elif item_choice[0] == "drop":
                        item = items[item_choice[1]]
                        item.on_drop(player, player.current_room)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid command")
                except KeyError:
                    print("Please select a valid item")
        else:
            raise ValueError
    except ValueError:
        print("Please enter 'move', 'item', or 'q'")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
