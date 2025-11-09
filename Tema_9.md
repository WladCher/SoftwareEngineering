# Тема 9. Концепции и принципы ООП
Отчет по Теме #9 выполнил:
- Червяков Владислав Максимович 
- ПИЭ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

---

## Лабораторная работа №9
### Задание 1

``` git
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
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_9/pic/lab1.jpg)

## Выводы
Создание класса с помощью class позволяет описывать собственные типы данных с заданными свойствами и поведением. Использование __slots__ ограничивает набор допустимых атрибутов и предотвращает создание несуществующих свойств (например, surname). Это делает класс более структурированным и помогает контролировать допустимые поля объекта.

---

### Задание 2

``` git
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')

icecream = Icecream()
icecream.composition()
icecream = Icecream("шоколадом")
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_9/pic/lab2.jpg)

## Выводы
Внутри класса можно задавать атрибуты и методы, которые управляют состоянием объекта. Проверка типа с помощью isinstance обеспечивает более надёжное выполнение операций. Такой подход отражает принцип инкапсуляции — объединение данных и поведения внутри одного объекта.

---

### Задание 3

``` git
class MyClass:
    def __init__(self, value):
        self._value = value
    
    def set_value(self, value):
        self._value = value
    
    def get_value(self):
        return self._value
    
    def del_value(self):
        del self._value

    value = property(get_value,set_value,del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_9/pic/lab3.jpg)

## Выводы
Здесь показано применение инкапсуляции и свойств (getter, setter, deleter) с использованием property. Такой механизм позволяет контролировать доступ к приватным данным и управлять изменением их значений. Ошибка при обращении к удалённому атрибуту _value демонстрирует важность аккуратного обращения с внутренним состоянием объекта.

---

### Задание 4

``` git
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"cat is {cat.className}, but they say {cat.sounds}")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_9/pic/lab4.jpg)

## Выводы
В этом задании показано наследование — принцип, при котором дочерние классы (Dog, Cat) получают свойства и методы родительского (Mammal). Такой подход делает код компактным, упрощает повторное использование и расширение функциональности. Уникальные атрибуты подклассов иллюстрируют специализацию объектов.

---

### Задание 5

``` git
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_9/pic/lab5.jpg)

## Выводы
Пример демонстрирует полиморфизм — возможность вызывать один и тот же метод (greet(language)) у разных классов (Russian, English), получая при этом различное поведение. Такой подход делает код более гибким, универсальным и удобным для расширения.

---

## Самостоятельная работа №9
### Задание 1

``` git
class Tomato:
    # стадии созревания (статическое свойство)
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зелёный', 3: 'красный'}

    def __init__(self, index: int):
        # _index — номер томата (приватное)
        # _state — стадия созревания (приватное)
        self._index = index
        self._state = 0  # первая стадия

    def grow(self):
        # перевод томата на следующую стадию
        if self._state < max(Tomato.states.keys()):
            self._state += 1
        print(f"Томат {self._index} теперь {Tomato.states[self._state]}")

    def is_ripe(self):
        # проверка, что томат созрел
        return self._state == max(Tomato.states.keys())


class TomatoBush:
    def __init__(self, count: int):
        # список томатов
        self.tomatoes = [Tomato(i) for i in range(1, count + 1)]

    def grow_all(self):
        print("\nКуст растёт")
        for t in self.tomatoes:
            t.grow()

    def all_are_ripe(self):
        # проверка, что все томаты спелые
        return all(t.is_ripe() for t in self.tomatoes) if self.tomatoes else False

    def give_away_all(self):
        # сбор урожая
        self.tomatoes.clear()
        print("Урожай собран, куст пуст")


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        # name — имя садовника (публичное)
        # _plant — куст (приватное)
        self.name = name
        self._plant = plant

    def work(self):
        print(f"\n{self.name} ухаживает за растением")
        self._plant.grow_all()
        print(f"{self.name} закончил уход")

    def harvest(self):
        print(f"\n{self.name} проверяет урожай")
        if not self._plant.tomatoes:
            print("На кусте нет томатов")
            return
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собрал урожай")
        else:
            print("Не все томаты созрели, собирать рано")

    @staticmethod
    def knowledge_base():
        print("""Справка по садоводству:
1. Томат проходит стадии: отсутствует -> цветение -> зелёный -> красный
2. Чтобы собрать урожай, нужно ухаживать за кустом до полной зрелости
3. После созревания плоды можно собрать""")


if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener("Влад", bush)

    gardener.work()
    gardener.harvest()

    gardener.work()
    gardener.harvest()

    gardener.work()
    gardener.harvest()

----------------------

Вывод программы:

Справка по садоводству:
1. Томат проходит стадии: отсутствует -> цветение -> зелёный -> красный
2. Чтобы собрать урожай, нужно ухаживать за кустом до полной зрелости
3. После созревания плоды можно собрать

Влад ухаживает за растением

Куст растёт
Томат 1 теперь цветение
Томат 2 теперь цветение
Томат 3 теперь цветение
Влад закончил уход

Влад проверяет урожай
Не все томаты созрели, собирать рано

Влад ухаживает за растением

Куст растёт
Томат 1 теперь зелёный
Томат 2 теперь зелёный
Томат 3 теперь зелёный
Влад закончил уход

Влад проверяет урожай
Не все томаты созрели, собирать рано

Влад ухаживает за растением

Куст растёт
Томат 1 теперь красный
Томат 2 теперь красный
Томат 3 теперь красный
Влад закончил уход

Влад проверяет урожай
Урожай собран, куст пуст
Влад собрал урожай
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_9/pic/samrab1.jpg)

## Выводы
Пример объединяет ключевые принципы ООП: инкапсуляцию (скрытие свойств _index и _state), композицию (взаимодействие класса Gardener с TomatoBush), и полиморфизм (единый интерфейс обращения к объектам Tomato). Также продемонстрировано применение статического метода (knowledge_base), который выполняет вспомогательную функцию, не требуя создания экземпляра класса.

---

## Общие выводы по теме

ООП — это мощный подход, моделирующий реальные объекты и их взаимодействие через классы и экземпляры. Использование принципов инкапсуляции, наследования, полиморфизма и абстракции делает программы на Python более структурированными и понятными, упрощает расширение и поддержку кода, а также обеспечивает повторное использование решений в разных проектах.
