# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.__set_name(name)

    def __get_name(self):
        return self._name
    
    def __set_name(self, name):
        self._name = name

    def __get_current_room(self):
        return self._current_room
    
    def __set_current_room(self, current_room):
        self._current_room = current_room

    name = property(__get_name, __set_name)
    current_room = property(__get_current_room, __set_current_room)