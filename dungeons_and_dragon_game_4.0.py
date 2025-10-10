import random
import requests
import json
from pathlib import Path

# GAME SETUP
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Define the valid options for door choices so we can validate player input
valid_door_choices = {"left", "right", "forward", "back"}

# Define valid yes/no responses for consistent input checking
valid_yes_no = {"yes", "no"}
# This will store items the player picks up along the way
inventory = []

# Logging function
def log_status(message):
    with open("game_log.txt", "a") as log_file: #this is a function which updates the game_log.txt file
        #the file creates a txt file in append mode (we are adding to the end of it)
    # """An example output from this file:
    #
    #     Player Fran has entered the game.
    #     Found a sword.
    #     Picked up a sword.
    #     Current inventory: ['sword']
    #     Encountered a goblin.
    #     Encountered a goblin.
    #     Rolled 6 and defeated the goblin.
    #     Current inventory: ['sword']
    #     Encountered a dragon.
    #     Encountered a dragon.
    #     Rolled 5 and defeated the dragon.
    #     Current inventory: ['sword']
    #     Encountered a goblin.
    #     Encountered a goblin.
    #     Rolled 3 and defeated the goblin.
    #     Current inventory: ['sword']
    #     Player Fran exited the game.
    #
    #         -> what we are using this function to log
    #             -> the fight of the game
    #             -> different fights in the game
    #             -> inventory changes in the game
    #             -> room exploration
    #             -> game exit
    # """
        #the file we are editing is called log_file
        #when the function is called, we write to the txt file a message, which is the function argument, and add a new line
        #this is important the next time a message is appended to the file
        log_file.write(message + "\n")

# Ask the player for their name at the start
name = input("Type your name: ")
internet_status = input("Do you have a stable internet connection? (y/n): ")

# """
#     -> we are making an API call, depending on if the user has a stable internet connection
#     -> we are making a call to the Uzby API
#     -> this generates a random name for the user, whose length is the same as their name
#     -> this takes a while to generate, which is why additional print statements are added
# """

if internet_status == "y":
    print("Generating stage name...")
    print("Making API request...")
    name = requests.get(f"https://uzby.com/api.php?min={len(name)}&max={len(name)}").text
    print(f"Your {len(name)} character stage name is: {name}")

print(f"Welcome to the game world, {name}!")
log_status(f"Player {name} has entered the game.") #This writes a message to the game_log.txt file, logging the name of the user

# DEFINING FUNCTIONS
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fight(opponent, required_item=None):
    print(f"You encounter a {opponent}!")
    log_status(f"Encountered a {opponent}.") #log to the game_log.txt file, using a function
        #we have defined a function which opens a txt file and writes what happens in the game whenever any major changes are made
        #the function writes a message to the game_log.txt file
        #the message is the argument of the function
        #we are then calling the function in the game whenever an important move is made
        #this logs that the user has made a certain move in the game
        #f strings can be used in the argument of the function

    # Check if the player is missing the required item
    if required_item and required_item not in inventory:
        print(f"You don’t have the {required_item}! The {opponent} defeats you.")
        log_status(f"Defeated by {opponent} due to missing {required_item}.") #create a log
        lose_inventory()
        return False

    # Roll a dice (1-6) to see if the player wins or loses
    roll = random.randint(1, 6)
    if roll >= 3:
        print(f"You rolled a {roll} and defeated the {opponent}!")

        #call an API for a randomly generated dog image if the user wins (this url is their prize)
        if internet_status == "y": #they have to have an internet connection for this API call to work
            img_url = dict(requests.get("https://dog.ceo/api/breeds/image/random").json())["message"]  # a string
            print(f"Congratulations, your prize is a randomly generated dog image. This can be collected at: {img_url}")

        log_status(f"Rolled {roll} and defeated the {opponent}.") #create a log
        return True
    else:
        print(f"You rolled a {roll} and the {opponent} defeated you!")
        log_status(f"Rolled {roll} and was defeated by the {opponent}.") #create a log
        lose_inventory()
        return False

def lose_inventory():
    global inventory
    print("You lost all your items!")
    log_status("Player lost all inventory items.") #create a log
    inventory = []


def explore_room(room):
    if room == "empty":
        print("This room is empty.")
        log_status("Entered an empty room.")

    elif room == "sword":
        print("You found a sword!")
        log_status("Found a sword.") #create a log
        choice = input("Pick it up? (yes/no): ").lower()
        if choice in valid_yes_no and choice == "yes":
            inventory.append("sword")
            print("Sword added to your inventory.")
            log_status("Picked up a sword.") #create a log

    elif room == "shield":
        print("You found a shield!")
        log_status("Found a shield.") #create a log
        choice = input("Pick it up? (yes/no): ").lower()
        if choice in valid_yes_no and choice == "yes":
            inventory.append("shield")
            print("Shield added to your inventory.")
            log_status("Picked up a shield.") #create a log

    elif room == "dragon":
        log_status("Encountered a dragon.") #create a log
        fight("dragon", required_item="sword")

    elif room == "goblin":
        log_status("Encountered a goblin.") #create a log
        fight("goblin")


# GAME FLOW
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

while True:
    door_choice = input("Pick a door (left/right/forward/back): ").lower()

    if door_choice not in valid_door_choices:
        print("That’s not a valid choice!")
        continue

    if door_choice == "left":
        explore_room("sword")
    elif door_choice == "right":
        explore_room("dragon")
    elif door_choice == "forward":
        explore_room("shield")
    elif door_choice == "back":
        explore_room("goblin")

    print(f"Your current inventory: {inventory}")
    log_status(f"Current inventory: {inventory}") #create a log

    cont = input("Do you want to keep exploring? (yes/no): ").lower()
    if cont in valid_yes_no and cont == "no":
        print("Thanks for playing!")
        log_status(f"Player {name} exited the game.") #create a log
        break