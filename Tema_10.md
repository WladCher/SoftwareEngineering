# Тема 10. Декораторы и исключения
Отчет по Теме #10 выполнил:
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

## Лабораторная работа №10
### Задание 1

``` git
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    print(fibonacci(100))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/lab1.jpg)

## Выводы
С помощью class можно создать класс и выполнить его инициализацию

---

### Задание 2

``` git
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопусимый возраст'
        input_func(name, age)
        
    return output_func

@check
def personal_info(name, age):
    print(f"Name: {name} Age: {age}")

if __name__ == '__main__':
    personal_info('Владимир', 38)
    personal_info('Александр', -5)
    personal_info('Петр', 138, 15, 48, 2)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/lab2.jpg)

## Выводы
Внутри класса можно определять атрибуты и методы

---

### Задание 3

``` git
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i]*15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')

if __name__ == '__main__':
    data([1,15,'Hello','i','try','to','crash','your','site',38,45])
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/lab3.jpg)

## Выводы
Классы можно наследовать, указывая родительский класс в скобках: class Class1(РодительскийКласс)

---

### Задание 4

``` git
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException("Длина более 10 символов")
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '12345678910'
    check_name(name)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/lab4.jpg)

## Выводы
Инкапсуляция с использованием _ или __ определяет уровень доступа к атрибуту

---

### Задание 5

``` git
class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func
    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного включения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/lab5.jpg)

## Выводы
Каждую строку можно выводить отдельно с помощью цикла

---

## Самостоятельная работа №10
### Задание 1

``` git
import time

def measure_time(func):
    def inner(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_finish = time.time()
        duration = t_finish - t_start
        print(f"\nПрограмма выполнилась за {duration:.4f} секунд")
        return result
    return inner

@measure_time
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' , ')

if __name__ == '__main__':
    fibonacci()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/samrab1.jpg)

## Выводы
Создан класс Book с полями для названия, автора и количества страниц, а также методами description(), который выводит информацию о книге, и is_long(), проверяющим, является ли книга длинной

---

### Задание 2

``` git
def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                raise ValueError("Файл пустой")
            print("Содержимое файла:\n", content)
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    read_file("not_empty.txt")
    read_file("empty.txt")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/samrab2.jpg)

## Выводы
Создан класс Book с полями для названия, автора и количества страниц, добавлен атрибут current_page для отслеживания прогресса чтения, а также методы description() для вывода информации о книге, is_long() для проверки длины книги и read(pages) для "чтения" определённого количества страниц

---

### Задание 3

``` git
def plus_two():
    try:
        num = float(input("Введите число: "))
        print("Ответ:", num + 2)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    plus_two()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/samrab3.jpg)

## Выводы
Созданы классы Book и AudioBook, где AudioBook наследует Book и добавляет поля для длительности и прогресса прослушивания. Реализованы методы description() для вывода информации, read(pages) для чтения страниц и listen(minutes) для прослушивания аудиокниги, демонстрируя наследование и расширение функционала

---

### Задание 4

``` git
class CountCalls:
    # конструктор получает функцию
    def __init__(self, func):
        self.func = func
        self.count = 0  # счётчик вызовов

    # вызывается при каждом вызове функции
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Функция {self.func.__name__} вызвана {self.count} раз")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(name):
    return f"Привет {name}"

@CountCalls
def square(x):
    return x ** 2


if __name__ == "__main__":
    print(say_hello("Влад"))
    print(say_hello("Екатерина"))
    print(square(5))
    print(square(10))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/samrab4.jpg)

## Выводы
Создан класс Book с приватными атрибутами для названия, автора, количества страниц и текущей страницы, а также методами description() для вывода информации о книге, read(pages) для чтения страниц и get_current_page() / set_current_page(page) для безопасного доступа и изменения текущей страницы, демонстрируя инкапсуляцию

---

### Задание 5

``` git
# собственное исключение, если строка пустая
class EmptyTextError(Exception):
    """Ошибка: пустой текст"""
    pass


# первая функция — проверяет имя пользователя
def check_name(name):
    if not name.strip():  # если пусто или только пробелы
        raise EmptyTextError("Имя не может быть пустым")
    print(f"Имя принято: {name}")


# вторая функция — проверяет комментарий
def check_comment(comment):
    if not comment.strip():
        raise EmptyTextError("Комментарий не должен быть пустым")
    print("Комментарий сохранён:", comment)


if __name__ == "__main__":
    try:
        check_name("  ")  # вызывает исключение
    except EmptyTextError as e:
        print("Ошибка:", e)

    try:
        check_comment("Hello world!")  # всё хорошо
    except EmptyTextError as e:
        print("Ошибка:", e)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_10/pic/samrab5.jpg)

## Выводы
Созданы классы Vehicle, Car, Boat и Plane с методом move(), который переопределяется в каждом наследнике, демонстрируя полиморфизм: один и тот же метод выполняет разное действие для разных объектов

---

## Общие выводы по теме

ООП — это фундаментальный подход к проектированию программ, основанный на моделировании реальных объектов и их взаимодействий. Принципы инкапсуляции, наследования, полиморфизма и абстракции делают код более структурированным и читаемым, облегчают масштабирование и сопровождение, позволяют повторно использовать компоненты в новых проектах и приближают логику программы к реальному миру. Выполнение всех заданий позволило глубже понять и применить ключевые концепции ООП на практике в Python
