# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=[]):
        self._name = name
        self._description = description
        self._items = items
        self._n_to = None
        self._s_to = None
        self._e_to = None
        self._w_to = None

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def items(self):
        return self._items

    @property
    def n_to(self):
        return self._n_to

    @property
    def s_to(self):
        return self._s_to

    @property
    def e_to(self):
        return self._e_to

    @property
    def w_to(self):
        return self._w_to
    
    @n_to.setter
    def n_to(self, room):
        self._n_to = room

    @s_to.setter
    def s_to(self, room):
        self._s_to = room

    @e_to.setter
    def e_to(self, room):
        self._e_to = room

    @w_to.setter
    def w_to(self, room):
        self._w_to = room

    def add_item(self, new_item):
        self._items.append(new_item)
    