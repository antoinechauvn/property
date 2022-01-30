class Person:
    def __init__(self) -> None:
        self._age = 0
    
    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, value):
        self._age = value

    @age.deleter
    def del_age(self):
        del self._age
