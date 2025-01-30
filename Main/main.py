import os

from room import Room
from character import Enemy
from character import Character

entrance = Room("Entrance")
upstairs = Room("Upstairs")
living_room = Room("Living Room")
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
bedroom = Room("Bedroom")
bathroom = Room("Bathroom")
garden = Room("Garden")

entrance.link_room(garden, "north")
entrance.link_room(upstairs, "east")
entrance.link_room(living_room, "west")
upstairs.link_room(bathroom, "north")
upstairs.link_room(bedroom, "west")
upstairs.link_room(entrance, "south")
living_room.link_room(kitchen, "north")
living_room.link_room(entrance, "east")
kitchen.link_room(dining_hall, "north")
kitchen.link_room(living_room, "south")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "south")
bedroom.link_room(upstairs, "east")
bathroom.link_room(upstairs, "south")
garden.link_room(entrance, "south")

zombie = Enemy("Zombie", "A zombie with a taste for brains.")
zombie.set_conversation("*Gargling and groaning noises*")
zombie.set_weakness("Shovel")
garden.set_character(zombie)

spirit = Enemy("Spirit", "A scary and translucent human-like figure.")
spirit.set_conversation("*Screeches* Leave before it's too late!")
spirit.set_weakness("Crucifix")
bedroom.set_character(spirit)

friendly_skeleton = Character("Friendly Skeleton", "Just a chill guy sat on a chair near the fireplace.")
friendly_skeleton.set_conversation("Hey man! You must be new around here. Welcome.")
living_room.set_character(friendly_skeleton)

entrance.set_description("The wooden floor beneath your feet is rotten, the walls torn to shreds.")
upstairs.set_description("The stairs creak loudly with every step as you walk up them. At the top there are corridors leading to each room.")
living_room.set_description("The living room is filled with what was once luxury furniture, now left worthless. The room has a faint scent of smoke from the fireplace.")
kitchen.set_description("A dark and dirty room buzzing with flies.")
ballroom.set_description("A vast, aged ballroom with no dancers to be seen.")
dining_hall.set_description("A decaying empty dining hall.")
bedroom.set_description("A master bedroom covered with blood splatters and smashed windows overlooking the garden.")
bathroom.set_description("A filthy bathroom with stains all over the walls and a shattered mirror.")
garden.set_description("An overgrown and muddy garden with tall wooden fences surrounding it.")


def start_menu():
    print("\n\t\t\tWelcome to my game, Haunted Mansion\n\
          ------------------------------------------------------------------------------\n\
          You can move around by inputting the direction of the room you want to move to.\n\n\
          You must look around for items that can help you in your adventure.\n\n\
          \t\tBe warned, you might not be alone...\n\n")

    input("You approach the mansion entrance, type anything to continue..")

def clear():
    os.system("cls" if os.name == "nt" else "clear")


current_room = entrance


clear()
start_menu()

while True:
        
        print("\n")
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()

        print("What would you like to do?")
        command = input ("> ")

        if command in ["north", "south", "east", "west"]:
             
             current_room = current_room.move(command)
        
        elif command == "talk":

            if inhabitant is not None:
                 inhabitant.talk()

            elif inhabitant is None:
                print("There is nobody to talk to here.")
        
        elif command == "fight":

            if inhabitant is not None:
                print("What will you fight with?")
                fight_with = input("> ")
                inhabitant.fight(fight_with)

            elif inhabitant is None:
                 print("There are no enemies to fight here.")
        
        else:
             print("Enter valid choice.")

while False:
     break
