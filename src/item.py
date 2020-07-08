class Item:
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

    name = property(__get_name, __set_name)
    description = property(__get_description, __set_description)
