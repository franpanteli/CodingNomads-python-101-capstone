"""Pseudocode
    Save the user input options you allow, e.g., in a set that you can check against
        when your user makes a choice.
    Create an inventory for your player, where they can add and remove items.
    Players should be able to collect items they find in rooms and add them to their inventory.
    If they lose a fight against the dragon, then they should lose their inventory items.
    Add more rooms to your game and allow your player to explore.
    Some rooms can be empty, others can contain items, and yet others can contain an opponent.
    Implement some logic that decides whether or not your player can beat the opponent depending
        on what items they have in their inventory
    Use the random module to add a multiplier to your battles, similar to a dice roll in a real
        game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.
    """

import random

# --- Game Setup ---
# Define the valid options for door choices so we can validate player input
valid_door_choices = {"left", "right", "forward", "back"}
    #compared to the previous version of the game, we are adding doors which do back and forward
    #(not just left and right)
    #these are stored in the form of sets (they contain no duplicates)

# Define valid yes/no responses for consistent input checking
valid_yes_no = {"yes", "no"}
# This will store items the player picks up along the way
inventory = [] #we want to store the user's inventory, this is initially empty

# Ask the player for their name at the start
name = input("Type your name: ") #ask the user for their name
print("Welcome,", name + ", to the game world!")

# --- Functions ---
def fight(opponent, required_item=None): #define functions to fight the dragon
                                        #this is the same dragon as in the previous version of the game
    """
    Handles fighting logic against an opponent.
    If a required item is specified (like a sword for a dragon), the player must have it.
    Uses a dice roll mechanic (1-6) to add randomness to the fight outcome.
    """
    print(f"You encounter a {opponent}!")

    # Check if the player is missing the required item
    if required_item and required_item not in inventory:
        print(f"You don’t have the {required_item}! The {opponent} defeats you.")
        lose_inventory()
        return False

    # Roll a dice (1-6) to see if the player wins or loses
    roll = random.randint(1, 6)
    if roll >= 3:
        print(f"You rolled a {roll} and defeated the {opponent}!")
        return True
    else:
        print(f"You rolled a {roll} and the {opponent} defeated you!")
        lose_inventory()
        return False


def lose_inventory():
    """
    Clears the player’s inventory when they lose a fight.
    """
    global inventory
    print("You lost all your items!")
    inventory = []


def explore_room(room):
    """
    Handles exploring a room. Depending on the room type, the player may:
    - Find nothing
    - Find an item they can pick up (sword/shield)
    - Encounter an enemy (dragon/goblin)
    """
    if room == "empty":
        print("This room is empty.")

    elif room == "sword":
        print("You found a sword!")
        choice = input("Pick it up? (yes/no): ").lower()
        if choice in valid_yes_no and choice == "yes":
            inventory.append("sword")
            print("Sword added to your inventory.")

    elif room == "shield":
        print("You found a shield!")
        choice = input("Pick it up? (yes/no): ").lower()
        if choice in valid_yes_no and choice == "yes":
            inventory.append("shield")
            print("Shield added to your inventory.")

    elif room == "dragon":
        # Fighting a dragon requires having a sword
        fight("dragon", required_item="sword")

    elif room == "goblin":
        # Goblin fight is easier; no required item
        fight("goblin")

# --- Game Flow ---
# Main game loop that continues until the player chooses to quit
while True:
    # Ask the player to pick a door
    door_choice = input("Pick a door (left/right/forward/back): ").lower()

    # Validate player input
    if door_choice not in valid_door_choices:
        print("That’s not a valid choice!")
        continue

    # Handle the different doors
    if door_choice == "left":
        explore_room("sword")
    elif door_choice == "right":
        explore_room("dragon")
    elif door_choice == "forward":
        explore_room("shield")
    elif door_choice == "back":
        explore_room("goblin")

    # Show inventory after each action
    print(f"Your current inventory: {inventory}")

    # Ask if the player wants to continue
    cont = input("Do you want to keep exploring? (yes/no): ").lower()
    if cont in valid_yes_no and cont == "no":
        print("Thanks for playing!")
        break







