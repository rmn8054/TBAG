class Room:

    # constructor
    def __init__ (self, room_name):
        self.name = None
        self.description = None
        self.linked_room = {}

    # creating getter and setter
    def get_description (self):
        return self.description
    
    def set_description (self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name
    
    def set_name(self, room_name):
        self.name = room_name