import os
from room import Room
from player import Player
from item import Item

# Create all Items
coins = Item("Coins", "Gold coins")
sword = Item("Sword", "Weapon to defend yourself")
treasure = Item("Treasure", "You found the treasure")

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [coins, sword]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Pickup the treasure!!!""", [treasure]),
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

name = ""

while name == "":
    os.system('cls')
    name = input("Player's name: ")

os.system('cls')

player = Player(name, room['outside'])

valid_input = True
valid_move = True
new_room = None
valid_item = True
playing = True

while playing:
    print(f"\nPlayer: {player.name}")
    print("\nYour items:")
    if player.items:
        for item in player.items:
            print(f"- {item.name} | {item.description}")
    else:
        print("No items")

    print(f"\nCurrent room: {player.current_room.name}")
    print(f"Description: {player.current_room.description}")
    print(f"\nItems in this room:" if player.current_room.items else "\nNo items in this room")
    for item in player.current_room.items:
        print(f"- {item.name} | {item.description}")

    display_message = ""

    if player.items or player.current_room.items:
        display_message = "\n-------------------------------\n"
        display_message += "What would you like to do? Options:\n[take/drop] [<item name>]\nor\n"
        display_message += "Move:\n[n] Nort\n[s] South\n[e] East\n[w] West\n\n[q] Quit\n\n"
    else:
        display_message = "\nWhere would you like to go?\n[n] Nort\n[s] South\n[e] East\n[w] West\n\n[q] Quit\n\n"
    
    if not valid_move:
        display_message += "Nothing there, try again\n\n"
    elif not valid_input:
        display_message += "Invalid input, try again\n\n"
    elif not valid_item:
        display_message += "Invalid item, try again\n\n"

    user_input = input(display_message).lower().split()

    valid_input = True
    valid_move = True
    new_room = None
    valid_item = True

    if len(user_input) == 1:
        if user_input[0] == "q":
            playing = False
        elif (user_input[0] == 'n' or user_input[0] == 's' or user_input[0] == 'e' or user_input[0] == 'w'):
            move = f"{user_input[0]}_to"
            new_room = getattr(player.current_room, move)

            if new_room:
                player.current_room = new_room
            else:
               valid_move = False
        else:
            valid_input = False
    elif len(user_input) == 2:
        u_input = user_input[0].lower()
        if (u_input == "take" or u_input == "get"):
            selected_item = next((i for i in player.current_room.items if i.name.lower() == user_input[1].lower()), None)
            if selected_item:
                player.add_item(selected_item)
                player.current_room.items.remove(selected_item)
                if (selected_item.name.lower() == "treasure"):
                    input("Congratulations!!! You WON" if playing else "")
                    playing = False
                else: input()
            else:
                valid_item = False
        elif u_input == "drop":
            selected_item = next((i for i in player.items if i.name.lower() == user_input[1].lower()), None)
            if selected_item:
                player.current_room.items.append(selected_item)
                player.remove_item(selected_item)
                input()
            else:
                valid_item = False
        else:
            valid_input = False
    
    os.system('cls')
            