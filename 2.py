class Person:
    def __init__(self) -> None:
        self._age = 0
        
    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    def del_age(self):
        del self._age
   
    age = property(get_age, set_age, del_age, "Propriété age")
