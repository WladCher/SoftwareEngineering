# Тема 4. Функции и модули
Отчет по Теме #4 выполнил:
- Червяков Владислав Максимович 
- ПИЭ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |   |
| Задание 7 | + |   |
| Задание 8 | + |   |
| Задание 9 | + |   |
| Задание 10 | + |   |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

---

## Лабораторная работа №4
### Задание 1

``` git
def main():
    print(2*2)

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab1.jpg)

## Выводы
Программа правильно обрабатывает и сравнивает введённые данные

---

### Задание 2

``` git
def main():
    return 2+2

if __name__ == '__main__':
    print(main())
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab2.jpg)

## Выводы
Программа корректно определяет три диапазона значений

---

### Задание 3

``` git
def main(one, two):
    result = one + two
    return result

for i in range(5):
    x = 1
    y = 10
    answer = main(x, y)
    print(answer)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab3.jpg)

## Выводы
Оператор in удобно использовать для поиска элемента в массиве

---

### Задание 4

``` git
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"one={one}\ntwo={two}\nthree={three}")
    return x+sum(args)/float(len(args))

if __name__ == '__main__':
    result = main(10,0,1,2,-1,0,-1,1,2)
    print(f"\nresult={result}")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab4.jpg)

## Выводы
Программа проверяет как наличие числа, так и его чётность

---

### Задание 5

``` git
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    
    print()

    for key in kwargs:
        print(f"{key}={kwargs[key]}")

if __name__ == '__main__':
    main(x=[1,2,3],y=[3,3,0],z=[2,3,0],q=[3,3,0],w=[3,3,0])
    print()
    main(**{'x':[1,2,3],'y':[3,3,0]})
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab5.jpg)

## Выводы
Цикл демонстрирует работу операций сравнения

---

### Задание 6

``` git
def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")
def mean(data):
    return sum(data)/float(len(data))

if __name__ == '__main__':
    main(x=[1,2,3],y=[3,3,0])
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab6.jpg)

## Выводы
Оператор else в цикле срабатывает только при отсутствии break
---

### Задание 7

``` git
def say_hello():
    print('Hello students!')
```

``` git
from for_import import say_hello

if __name__ == '__main__':
    say_hello()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab7.jpg)

## Выводы
Цикл for можно легко организовать в обратном порядке

---

### Задание 8

``` git
from math import sqrt, sin, cos
def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab8.jpg)

## Выводы
При корректном условии цикл while завершает работу правильно

---

### Задание 9

``` git
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}."
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"Через {n} дней будет {result.date()}."
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab9.jpg)

## Выводы
Вложенные циклы дают возможность проверять различные комбинации значений

---

### Задание 10

``` git
global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a*b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5*a*h

figure = input("1 - прямоугольник, 2 - треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab10.jpg)

## Выводы
Переменная flag удобно применять как индикатор выполнения условия

---

## Самостоятельная работа №4
### Задание 1

``` git
from datetime import datetime      # импортируем класс для работы с датой и временем
from math import sqrt              # импортируем функцию для вычисления квадратного корня

def main(**kwargs):                 # создаем функцию, которая принимает любое количество именованных аргументов
    for key in kwargs.items():      # проходим по всем парам (ключ,значение) в словаре kwargs
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)  # считаем длину вектора по формуле Пифагора
        print(result)               # выводим полученное значение на экран

if __name__ == '__main__':          # проверяем, что скрипт запускается напрямую, а не импортируется
    start_time = datetime.now()     # фиксируем время начала работы программы
    main(                           # вызываем функцию main с несколькими списками в качестве аргументов
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    time_costs = datetime.now() - start_time   # определяем, сколько времени заняло выполнение программы
    print(f"Время выполнения программы - {time_costs}")  # выводим продолжительность работы программы
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab2.jpg)

## Выводы
Программа выполняет задачу, используя исключительно разрешённые операции

---

### Задание 2

``` git
import random

def cube():
    value = random.randint(1, 6)
    print(f"Выпавшее число - {value}")
    
    if value in (5, 6):
        print("Вы победили")
    elif value in (3, 4):
        cube()
    else:
        print("Вы проиграли")

if __name__ == "__main__":
    cube()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab3.jpg)

## Выводы
Строка выводится по символам в обратном порядке

---

### Задание 3

``` git
import time
from datetime import datetime

for i in range(5):
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)                            
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab4.jpg)

## Выводы
Программа правильно обрабатывает диапазоны чисел

---

### Задание 4

``` git
def average(*args):
    return sum(args) / len(args)

if __name__ == "__main__":
    print("Среднее арифметическое - ", average(4, 12, 8, 1, 2))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab5.jpg)

## Выводы
Программа выполняет все операции со строкой: подсчитывает символы, переводит в нижний регистр, считает количество гласных с помощью строки гласных, заменяет слова в предложении, начинает строку с The и завершает на end

---

### Задание 5

``` git
import math

def f_heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
```

``` git
from triangle import f_heron

if __name__ == "__main__":
    a = float(input("Cторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))
    
    area = f_heron(a, b, c)
    print("Площадь треугольника равна - ", area)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab1.jpg)

## Выводы
Программа отображает необходимые строки в консоли

---

## Общие выводы по теме
Операторы выполняют арифметические действия, сравнения и работу с логическими выражениями. Условные конструкции (if, elif, else) позволяют выбирать различные ветви выполнения программы в зависимости от входных данных. Циклы (for, while) дают возможность повторять действия многократно: for удобен для перебора последовательностей, а while — для выполнения действий до наступления определённого условия. Дополнительно, использование break, continue, else в циклах и переменных-индикаторов (flag) обеспечивает гибкое управление выполнением кода.
