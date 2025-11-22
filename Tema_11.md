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
Применение декоратора @lru_cache ускоряет выполнение рекурсивных функций, таких как вычисление чисел Фибоначчи, за счёт кеширования ранее вычисленных значений. Это показывает, как декораторы могут повышать производительность программы без изменения основной логики функции

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
Декоратор проверяет корректность введённого возраста перед выполнением основной функции, вынося логику проверки на отдельный уровень

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
Вложенные блоки try/except/finally позволяют обрабатывать исключения и предотвращать сбои при работе с некорректными типами данных. Исключения перехватываются и обрабатываются без прерывания выполнения программы, а блок finally обеспечивает выполнение завершающих действий. Это показывает, как исключения помогают управлять ошибками и поддерживать стабильность программы

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
Создание собственного исключения через наследование от Exception позволяет обрабатывать специфические ошибки программы. В данном случае пользовательское исключение сигнализирует о слишком длинном имени при регистрации. Такой подход делает код более понятным и обеспечивает механизм обработки ошибок, что особенно важно в крупных проектах

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
Класс-декоратор SiteChecker с методами __init__ и __call__ выполняет дополнительные действия до и после вызова функции. Это пример объектно-ориентированного декоратора, который логирует выполнение кода, обеспечивая прозрачность и контроль за работой программы, что полезно для логирования, мониторинга и тестирования

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
Декоратор measure_time измеряет время выполнения функции, не изменяя её логику. Он оборачивает функцию fibonacci, фиксирует начало и конец выполнения и выводит длительность работы. Такой подход позволяет повторно применять измерение времени для любых функций

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
Обработка исключений FileNotFoundError и ValueError предотвращает сбои при работе с файлами. Если файл пустой, программа сообщает об этом, не прерывая выполнение. Такой подход делает ввод-вывод надёжным и безопасным

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
Блок try/except корректно перехватывает исключение ValueError при попытке преобразовать введённую строку в число. Это показывает, как стандартные исключения помогают защищать программу от некорректного ввода

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
Класс-декоратор CountCalls добавляет функционал подсчёта вызовов функции без изменения её исходного кода. Он демонстрирует ООП-подход в реализации декораторов: объект-декоратор хранит ссылку на функцию, ведёт счётчик вызовов и управляет её выполнением. Такой подход удобно использовать для логирования, мониторинга использования функций и анализа их работы.

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
Создание пользовательского исключения EmptyTextError позволяет централизованно обрабатывать специфические ошибки, связанные с пустыми строками. Оно повышает читаемость и расширяемость кода, обеспечивая единообразную обработку ошибок в разных функциях. Пример демонстрирует, как можно расширять систему исключений Python для удовлетворения требований конкретного проекта.

---

## Общие выводы по теме

Тема декораторов и исключений объединяет два важных аспекта — гибкость и надёжность кода

Декораторы позволяют добавлять дополнительное поведение (логирование, измерение времени, проверку прав, кеширование) без изменения исходной логики функций
Исключения обеспечивают контроль ошибок и предотвращают аварийное завершение программы

Применение этих инструментов делает код расширяемым, устойчивым к ошибкам и более профессионально оформленным
