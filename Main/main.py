from room import Room

entrance = Room("Mansion Entrance")
stairs = Room("Stairs")
living_room = Room("Living Room")
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
bedroom = Room("Bedroom")
bathroom = Room("Bathroom")
garden = Room("Garden")


entrance.set_description("The wooden floor beneath your feet is rotten, the walls torn to shreds")
stairs.set_description("The stairs creak loudly with every step as you walk up them")
living_room.set_description("The living room is filled with what was once luxury furniture, now left worthless. The room has a faint scent of smoke from the fireplace")
kitchen.set_description("A dark and dirty room buzzing with flies")
ballroom.set_description("A vast, aged ballroom with no dancers to be seen")
dining_hall.set_description("A decaying empty dining hall")
bedroom.set_description("A master bedroom covered with blood splatters and smashed windows overlooking the garden")
bathroom.set_description("A filthy bathroom with stains all over the walls and a shattered mirror")
garden.set_description("An overgrown and muddy garden with tall wooden fences surrounding it")


print("Welcome to my game: Zombie Mansion")
print("You approach the front door of the mansion, would you like to enter?: [Y/N]")
Enter_Choice = input("> ")

if "Y":
    print (entrance.description)

elif "N":
    print("You take a few steps back and decide to leave")
    print("Thank you for playing!")

else:
    print("Please enter a valid choice")