
class Space:
    space_id = None
    occupied = False
    adjacentSpaces = []
    type = None

    def __init__(self, space_id, type):
        self.space_id = space_id
        self.type = type
        self.get_adjacent_spaces = None

    def set_occupied(self):
        self.occupied = True
    ##this method needs help. Before, the space class was asking the board class which was asking the space class and 
    ##none actually gave adjacent spaces.
    def get_adjacent_spaces(space_id):
        return space_id
 


class Room(Space):
    associated_card = None
    secret_passage = None

    def __init__(self, space_id, type, associated_card, secret_passage=False):
        Space.__init__(space_id, type)
