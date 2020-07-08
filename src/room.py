# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.__set_name(name)
        self.__set_description(description)
    
    def __get_name(self):
        return self._name
    
    def __set_name(self, name):
        self._name = name

    def __get_description(self):
        return self._description
    
    def __set_description(self, description):
        self._description = description
    
    def __get_n_to(self):
        return self._n_to

    def __set_n_to(self, room):
        self._n_to = room

    def __get_s_to(self):
        return self._s_to

    def __set_s_to(self, room):
        self._s_to = room
    
    def __get_e_to(self):
        return self.e_to

    def __set_e_to(self, room):
        self._e_to = room

    def __get_w_to(self):
        return self._w_to

    def __set_w_to(self, room):
        self._w_to = room

    name = property(__get_name, __set_name)
    description = property(__get_description, __set_description)
    n_to = property(__get_n_to, __set_n_to)
    s_to = property(__get_s_to, __set_s_to)
    e_to = property(__get_e_to, __set_e_to)
    w_to = property(__get_w_to, __set_w_to)