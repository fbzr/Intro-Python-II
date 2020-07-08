# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.__set_name(name)
        self.__set_current_room(current_room)
        self.__set_items([])

    def __get_name(self):
        return self._name
    
    def __set_name(self, name):
        self._name = name

    def __get_current_room(self):
        return self._current_room
    
    def __set_current_room(self, current_room):
        self._current_room = current_room

    def __get_items(self):
        return self._items
    
    def __set_items(self, items):
        self._items = items

    def add_item(self, item):
        self._items.append(item)

    name = property(__get_name, __set_name)
    current_room = property(__get_current_room, __set_current_room)
    items = property(__get_items, __set_items)