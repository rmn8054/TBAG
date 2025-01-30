from room import Room
from character import Enemy

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

zombie = Enemy("Zombie", "A zombie with a taste for brains")
zombie.set_conversation("*Gargling and groaning noises*")
zombie.set_weakness("Shovel")
garden.set_character(zombie)

entrance.set_description("The wooden floor beneath your feet is rotten, the walls torn to shreds.")
upstairs.set_description("The stairs creak loudly with every step as you walk up them. At the top there are corridors leading to each room")
living_room.set_description("The living room is filled with what was once luxury furniture, now left worthless. The room has a faint scent of smoke from the fireplace.")
kitchen.set_description("A dark and dirty room buzzing with flies.")
ballroom.set_description("A vast, aged ballroom with no dancers to be seen.")
dining_hall.set_description("A decaying empty dining hall.")
bedroom.set_description("A master bedroom covered with blood splatters and smashed windows overlooking the garden.")
bathroom.set_description("A filthy bathroom with stains all over the walls and a shattered mirror.")
garden.set_description("An overgrown and muddy garden with tall wooden fences surrounding it.")


current_room = entrance
while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input ("> ")
    current_room = current_room.move(command)





'''
print("Welcome to my game: Zombie Mansion")
print("---------------------------------------")

while True:

    print("You approach the front door of the mansion, would you like to enter?: [Y/N]")
    Enter_Choice = input("> ")

    if Enter_Choice.upper() == "Y":
        entrance.get_details()
        print("Where would you like to go?: ")
        Entrance_Choice = input("> ")
        
        if Entrance_Choice == "Garden":
            garden.get_details()
            print("There is a shovel sticking out of a patch of dirt, would you like to take it?: [Y/N]")
            Garden_Item_Choice = input("> ")

            if Garden_Item_Choice.upper() == "Y":
                print("You take")




        elif Entrance_Choice == "Upstairs":
            upstairs.get_details()

        elif Entrance_Choice == "Living Room":
            living_room.get_details()

        else:
            print("Please select a valid option or check for typo.")








        break
    elif Enter_Choice.upper() == "N":
        print("You take a few steps back and decide to leave.")
        print("Thank you for playing!")
        break
    else:
        print("Please enter a valid choice.")
'''