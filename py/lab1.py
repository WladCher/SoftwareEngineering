class Vlad:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Влад':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Влад"

person1 = Vlad('Влад')
person2 = Vlad('Евгений')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'