class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    # getters and setters
    @property
    def name(self):
        return self._name
    @name.setter
    def nom(self, nom):
        self._name = name 
    @property
    def age(self):
        return self.__age 
    @age.setter
    def age(self, age):
        if not isinstance(agem int):
            raise ValueError("L'age ne peut etre qu'un nombre entier")
        self.__age =age
    def add_courses(self, cours):