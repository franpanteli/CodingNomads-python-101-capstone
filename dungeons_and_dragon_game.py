# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.
can_fight_dragon =False
pick_up_sword=""
name = input("Type your name: ")

# Display a message that greets them and introduces them to the game world.
print("Welcome,",name+", to the game world!")

# Present them with a choice between two doors.
door_choice = input("Pick between these two doors, left and right: ")

# If they choose the left door, they'll see an empty room.
if door_choice == "left":
    print("Nothing is behind this door")

# If they choose the right door, then they encounter a dragon.
if door_choice == "right":
    print("DRAGON!")

# In both cases, they have the option to return to the previous room or interact further.
return_to_previous_door = input("Would you like to return to the previous door (you can say yes)? ")

if return_to_previous_door == "no":
    print("DRAGON!")
    print("You loose the game, you were defenceless!")

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
if return_to_previous_door == "yes":
    print("You encountered a sword!")
    pick_up_sword = input("Pick up sword (you can say yes)? ")

# When encountering the dragon, they have the choice to fight it.
if pick_up_sword == "yes":
    can_fight_dragon == True

# If they have the sword from the other room, then they will be able to defeat it and win the game.
    print("You defeated the dragon!")

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
if pick_up_sword == "no":
    print("DRAGON!")
    print("You loose the game, you were defenceless!")






