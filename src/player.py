# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self._name = name
        self._current_room = current_room
        self._items = []

    @property
    def name(self):
        return self._name

    @property
    def current_room(self):
        return self._current_room
    
    @property
    def items(self):
        return self._items

    @current_room.setter
    def current_room(self, new_room):
        if new_room:
            self._current_room = new_room
        else:
            print("Nothing there, try again")

    def add_item(self, item):
        self._items.append(item)