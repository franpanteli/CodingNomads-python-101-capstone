"""
    Required task / game updates, compared to the first version
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

#import modules
import random

# GAME SETUP
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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

# DEFINING FUNCTIONS
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fight(opponent, required_item=None): #define functions to fight the dragon
                                        #this is the same dragon as in the previous version of the game

    """
        -> this function fights the opponent (the dragon)
        -> the sword fights the dragon
        -> the second argument to this function is the status of whether the user has the weapon to fight their opponent type
        -> this is randomised using a dice roll from 1-6
    """

    print(f"You encounter a {opponent}!")

    # Check if the player is missing the required item
    if required_item and required_item not in inventory: #the player needs the required item to fight their opponent,
                                                        #to be able to defeat them
        print(f"You don’t have the {required_item}! The {opponent} defeats you.")

    """Weapons
        -> if the user has the weapons to defeat their opponent, then they stand a chance at defeating them
        -> if they don't have the weapon, then they will always loose the fight against their opponent
            -> this is what this section of the code does
        -> the next section of the code implies that they have the weapon
            -> in which case we want to add a random element into the game
            -> there exists a case where they have the weapon to defeat the opponent, but they still loose the game
                because of its random element
    """

        lose_inventory()
        return False

    # Roll a dice (1-6) to see if the player wins or loses
    roll = random.randint(1, 6) #define a random integer between 1 and 6 - this is the dice roll
    if roll >= 3:
        print(f"You rolled a {roll} and defeated the {opponent}!")
        return True
    else:
        print(f"You rolled a {roll} and the {opponent} defeated you!")
        lose_inventory()
        return False

    """Loosing or winning the game randomly
        -> they win the game if the dice roll is above 3 (maximum 6) and they have the weapon to beat their opponent
        -> they lost the game above if they did not have the weapon to beat the opponent
        -> they also loose the game if they have the weapon to beat the opponent, but theyroll the dice below 3 (up to 6)
        -> the fight function returns True or False, depending on if the use lost or won the game
            -> this also depends on the type of opponent which they are facing
            -> the previous version of the game only had dragons
    """

def lose_inventory():
    """
        -> if the player looses a fight, then their entire inventory is wiped
        -> this prints out the message that their inventory is now empty
        -> to reset the inventory, a blank list is defined
        -> this function is made global, so that changes to variables which it makes then apply everywhere in the code
    """
    global inventory
    print("You lost all your items!")
    inventory = []


def explore_room(room):
    """To explore a room
        -> this function is for exploring a room
        -> the previous game only had two rooms
        -> when the user first starts the game, they are offered an option of doors - left / right / forwards / backwards

        -> different outcomes depending on the type of room the player is in:
            -> they can find nothing
            -> they can find a sword or shield (an item)
                -> the only item they could find in the previous version of the game was a sword
                -> the shield is a new item that can be picked up here

            -> they can encounter an enemy
                -> the previous enemies which they could encounter were only a dragon
                -> in this version of the game, they can encounter a golblin
                -> this has to be fought with the shield, and the dragon still with the sword
                -> the goblin is fought with the shield and the dragon with the sword

            -> each of these different case scenarios are coded into this function with if blocks

            -> either, the user encounters an enemy (a dragon or golblin), they can pick up a weapon (sword / shield), or they find
                an empty room
    """

    if room == "empty": #case #1, the room is empty
        print("This room is empty.") #print out that the room is empty

    elif room == "sword": #case #2, the user finds a sword
        print("You found a sword!") #print the result
        choice = input("Pick it up? (yes/no): ").lower() #give the user a choice of picking up the item
        if choice in valid_yes_no and choice == "yes": #if the user entered yes or no and they want to pick up the sword,
                                                        #add it to the list which contains the inventory of the items they picked up
            inventory.append("sword")
            print("Sword added to your inventory.")

    elif room == "shield": #case #3, the user finds a shield
        print("You found a shield!")
        choice = input("Pick it up? (yes/no): ").lower() #we perform the same operation as in the previous code block, but with
                                                        #the shield and not the sword
        if choice in valid_yes_no and choice == "yes":
            inventory.append("shield")
            print("Shield added to your inventory.")

    elif room == "dragon": #case #4, the user finds a dragon
        # Fighting a dragon requires having a sword
        fight("dragon", required_item="sword") #call the fight function we previously defined to fight the dragon
                                                #they then either loose or do not
                                                #if they loose, then their inventory is wiped

    elif room == "goblin":
        # Goblin fight is easier; no required item
        fight("goblin") #the previous code block is repeated, but for the goblin and not the dragon

    """Changes
        -> whereas the previous version of the game had two doors (left and right), this version of the game has doors which go
            left, right, back and front
        -> this version of the game uses an inventory in the form of a list, to store the weapons that the user has
            -> it also offers the ability to wipe the inventory if the user looses a fight, by defining a function for this
        -> the previous version of the game only had a sword and a dragon
        -> this version of the game adds a goblin, which is defeated with a shied and a random dice score above3 (up to 6)
        -> the dragon was defeated in the previous version of the game if the user had the sword. In this version of the game, the
            user must have the sword, and also a random dice score above 3 (up to 6)
    """

# GAME FLOW
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#we now have functions defined, which we can leverage when the user plays the game
#main game loop that continues until the player chooses to quit
while True: #use an infinite loop
    #ask the player to pick a door
    door_choice = input("Pick a door (left/right/forward/back): ").lower() #as the user for their choice of door

    #validate player input
    if door_choice not in valid_door_choices:
            #from before, valid_door_choices = {"left", "right", "forward", "back"}
            #they must enter a valid door choice, if this is not the case continue moves the user back to the input stage
            #of the while loop
        print("That’s not a valid choice!")
        continue

    #handle the different doors
    if door_choice == "left": #there are four door choices, left right, forward and backward
                                #the explore_room function is called for each of them
                                #the argument of this function is the room
                                #depending on the status of the room, different functions are called
        explore_room("sword") #the user picks up the sword and it's added to their inventory
    elif door_choice == "right":
        explore_room("dragon") #the user fights the dragon
                                #this uses the embedded fight function
    elif door_choice == "forward":
        explore_room("shield") #we repeat the process with the other two doors
    elif door_choice == "back":
        explore_room("goblin")

    #show inventory after each action
    print(f"Your current inventory: {inventory}") #this uses an f string literal to print the inventory status

    #we are iterating through this in an infinite while loop
    #ask if the player wants to continue
    cont = input("Do you want to keep exploring? (yes/no): ").lower()
    if cont in valid_yes_no and cont == "no": #break the while loop if the user wants to exit the game
        print("Thanks for playing!")
        break