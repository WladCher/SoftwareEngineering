# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
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

## Лабораторная работа №8
### Задание 1

``` git
class Car:
    def __init__(self, make, model):#функция инициализации 
        self.make = make #марка авто
        self.model = model #модель авто

my_car = Car("Toyota", "Corolla") #создание объекта
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/lab1.jpg)

## Выводы
С помощью class можно создать класс и выполнить его инициализацию

---

### Задание 2

``` git
class Car:
    def __init__(self, make, model): #функция инициализации 
        self.make = make #марка авто
        self.model = model #модель авто
    
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") #создание объекта
my_car.drive()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/lab2.jpg)

## Выводы
Внутри класса можно определять атрибуты и методы

---

### Задание 3

``` git
class Car:
    def __init__(self, make, model): #функция инициализации 
        self.make = make #марка авто
        self.model = model #модель авто
    
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") #создание объекта
my_car.drive()

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"Chatging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/lab3.jpg)

## Выводы
Классы можно наследовать, указывая родительский класс в скобках: class Class1(РодительскийКласс)

---

### Задание 4

``` git
class Car:
    def __init__(self, make, model): #функция инициализации 
        self._make = make #марка авто
        self.__model = model #модель авто
    
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") #создание объекта
print(my_car._make)
my_car.drive()

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"Chatging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/lab4.jpg)

## Выводы
Инкапсуляция с использованием _ или __ определяет уровень доступа к атрибуту

---

### Задание 5

``` git
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle(5, 10)
circle = Circle(7)

shapes = [rect, circle]

for shape in shapes:
    print("Площадь фигуры:", shape.area())
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/lab5.jpg)

## Выводы
Каждую строку можно выводить отдельно с помощью цикла

---

## Самостоятельная работа №8
### Задание 1

``` git
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"Книга '{self.title}' написана {self.author} и содержит {self.pages} страниц."

    def is_long(self):
        return self.pages > 300


my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)

print(my_book.description())
print("Это длинная книга." if my_book.is_long() else "Это короткая книга.")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/samrab1.jpg)

## Выводы
Создан класс Book с полями для названия, автора и количества страниц, а также методами description(), который выводит информацию о книге, и is_long(), проверяющим, является ли книга длинной

---

### Задание 2

``` git
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def description(self):
        return f"Книга '{self.title}' написана {self.author} и содержит {self.pages} страниц."

    def is_long(self):
        return self.pages > 300

    def read(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        return f"Сейчас вы на странице {self.current_page}."


my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)

print(my_book.description())
print("Это длинная книга." if my_book.is_long() else "Это короткая книга.")
print(my_book.read(50))
print(my_book.read(100))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/samrab2.jpg)

## Выводы
Создан класс Book с полями для названия, автора и количества страниц, добавлен атрибут current_page для отслеживания прогресса чтения, а также методы description() для вывода информации о книге, is_long() для проверки длины книги и read(pages) для "чтения" определённого количества страниц

---

### Задание 3

``` git
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def description(self):
        return f"Книга '{self.title}' написана {self.author} и содержит {self.pages} страниц."

    def is_long(self):
        return self.pages > 300

    def read(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        return f"Сейчас вы на странице {self.current_page}."

class AudioBook(Book):
    def __init__(self, title, author, pages, duration_minutes):
        super().__init__(title, author, pages)
        self.duration_minutes = duration_minutes
        self.current_minute = 0

    def listen(self, minutes):
        self.current_minute += minutes
        if self.current_minute > self.duration_minutes:
            self.current_minute = self.duration_minutes
        return f"Вы прослушали {self.current_minute} из {self.duration_minutes} минут аудиокниги."

    def description(self):
        return f"Аудиокнига '{self.title}' автора {self.author}, длительность: {self.duration_minutes} минут."

paper_book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)
audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 384, 720)

print(paper_book.description())
print(paper_book.read(50))
print(paper_book.is_long())

print(audio_book.description())
print(audio_book.listen(120))
print(audio_book.listen(300))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/samrab3.jpg)

## Выводы
Созданы классы Book и AudioBook, где AudioBook наследует Book и добавляет поля для длительности и прогресса прослушивания. Реализованы методы description() для вывода информации, read(pages) для чтения страниц и listen(minutes) для прослушивания аудиокниги, демонстрируя наследование и расширение функционала

---

### Задание 4

``` git
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__current_page = 0

    def description(self):
        return f"Книга '{self.__title}' написана {self.__author} и содержит {self.__pages} страниц."

    def read(self, pages):
        if pages < 0:
            return "Невозможно прочитать отрицательное количество страниц."
        self.__current_page += pages
        if self.__current_page > self.__pages:
            self.__current_page = self.__pages
        return f"Сейчас вы на странице {self.__current_page}."

    def get_current_page(self):
        return self.__current_page

    def set_current_page(self, page):
        if 0 <= page <= self.__pages:
            self.__current_page = page
            return f"Страница установлена на {self.__current_page}."
        else:
            return "Недопустимый номер страницы."

my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)

print(my_book.description())
print(my_book.read(50))
print(my_book.get_current_page())
print(my_book.set_current_page(200))
print(my_book.get_current_page())
print(my_book.set_current_page(500))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/samrab4.jpg)

## Выводы
Создан класс Book с приватными атрибутами для названия, автора, количества страниц и текущей страницы, а также методами description() для вывода информации о книге, read(pages) для чтения страниц и get_current_page() / set_current_page(page) для безопасного доступа и изменения текущей страницы, демонстрируя инкапсуляцию

---

### Задание 5

``` git
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Машина едет по дороге."

class Boat(Vehicle):
    def move(self):
        return "Лодка плывёт по воде."

class Plane(Vehicle):
    def move(self):
        return "Самолёт летит в небе."


transport = [Car(), Boat(), Plane()]

for t in transport:
    print(t.move())
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_8/pic/samrab5.jpg)

## Выводы
Созданы классы Vehicle, Car, Boat и Plane с методом move(), который переопределяется в каждом наследнике, демонстрируя полиморфизм: один и тот же метод выполняет разное действие для разных объектов

---

## Общие выводы по теме

ООП — это фундаментальный подход к проектированию программ, основанный на моделировании реальных объектов и их взаимодействий. Принципы инкапсуляции, наследования, полиморфизма и абстракции делают код более структурированным и читаемым, облегчают масштабирование и сопровождение, позволяют повторно использовать компоненты в новых проектах и приближают логику программы к реальному миру. Выполнение всех заданий позволило глубже понять и применить ключевые концепции ООП на практике в Python
