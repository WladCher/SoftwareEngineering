# Тема 5. Базовые коллекции: множества, списки
Отчет по Теме #5 выполнил:
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

## Лабораторная работа №5
### Задание 1

``` git
set_1 = {'White','Black','Red','Pink'}
set_2 = {'Red','Green','Blue','Red'}
print('1', set_1 - set_2)

set_1 = {'White','Black','Red','Pink','Black','White'}
set_2 = {'Red','Green','Blue','Red'}
print('2', set_1 - set_2)

set_1 = {'White','Black','Red','Pink','Red','Red'}
set_2 = {'Red','Green','Red','Red','Red'}
print('3', set_1 - set_2)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab1.jpg)

## Выводы
С помощью функции main и точки входа результат успешно выводится

---

### Задание 2

``` git
a = set('abcdefg')
print(a)
for i in range(1,5):
    a.add(i)
print(a)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab2.jpg)

## Выводы
С помощью функции main с return и точки входа результат успешно выводится

---

### Задание 3

``` git
def replace(input_list):
    memory = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = memory

    return input_list

print(replace([1,2,3,4,5]))
```
``` git
lst = [1, 2, 3, 4, 5]
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab3.1.jpg)
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab3.2.jpg)

## Выводы
Функция позволяет работать с переданными аргументами

---

### Задание 4

``` git
a = [12,54,32,57,843,2346,765,75,25,234,756,23]
print(a[2:6])
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab4.jpg)

## Выводы
Кортежи позволяют выполнять массовые вычисления, а *args принимает множество аргументов

---

### Задание 5

``` git
def useless(lst):
    return max(lst) / len(lst)

print(useless([3, 5, 7, 3,33]))
print(useless([-12.5, 54, 77.3, 0,-36,98.2,-63,21.7,47,-89.6]))
print(useless([-25.8, 86, 12.5, -56,73.2,0,43,-91.5,65.9,-7]))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab5.jpg)

## Выводы
Имена параметров выступают в роли ключей, а оператор ** собирает аргументы в словарь

---

### Задание 6

``` git
superheroes = ['superman', 'spiderman', 'batman']
nikolay, vasiliy, ivan = superheroes

print('Николай - ', nikolay)
print('Василий - ', vasiliy)
print('Иван - ', ivan)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab6.jpg)

## Выводы
В программе реализованы две функции: первая принимает произвольное количество именованных аргументов (**kwargs) и передаёт их во вторую функцию, которая вычисляет среднее арифметическое

---

### Задание 7

``` git
a = [-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]
a.sort()
print('Отсортированный список:\n ', a)
a.pop(0)
print('Отсортированный список без наименьшего элемента:\n ', a)
```

### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab7.jpg)

## Выводы
С помощью import можно подключать функции из других .py файлов, если они расположены в одной директории

---

### Задание 8

``` git
from random import randint

def list_maker():
    a = [randint(1,100)]*randint(3,10)
    return a

if __name__ == '__main__':
    result = []
    for i in range(randint(1,5)):
        result.append(list_maker())

    print(result)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab8.jpg)

## Выводы
С помощью модуля math можно вычислять различные математические функции и применять операторы (sqrt — корень, sin — синус, cos — косинус)

---

### Задание 9

``` git
def superset(set_1, set_2):
    if set_1 == set_2:
        print(f"Множества равны")
    elif set_1 > set_2:
        print(f"Объект {set_1} является чистым супермножеством")
    elif set_2 > set_1:
        print(f"Объект {set_2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

if __name__ == '__main__':
    superset({1,8,3,5}, {3,5})
    superset({1,8,3,5}, {5,3,8,1})
    superset({3,5}, {5,3,8,1})
    superset({90,100}, {3,5})
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab9.jpg)

## Выводы
Встроенные модули Python datetime и timedelta позволяют выполнять операции с временем

---

### Задание 10

``` git
my_list = [2,5,8,3]
print(my_list[::-1])
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/lab10.jpg)

## Выводы
Глобальная переменная result хранит одно значение, доступное для всех функций

---

## Самостоятельная работа №4
### Задание 1

``` git
from collections import Counter

check = [8734,2345,8201,6621,9999,1234,5678,8201,8888,4321,3365,
1478,9865,5555,7777,9998,1111,2222,3333,4444,5556,6666,
5410,7778,8889,4445,1439,9604,8201,3365,7502,3016,4928,
5837,8201,2643,5017,9682,8530,3250,7193,9051,4506,1987,
3365,5410,7168,7777,9865,5678,8201,4445,3016,4506,4506]

total_checks = len(check)
unique_visitors = len(set(check))

counter = Counter(check)
most_common_code, maxcount = counter.most_common(1)[0]

print("Всего чеков:", total_checks)
print("Разных людей:", unique_visitors)
print("Чаще всех приходил код:", most_common_code, "-", maxcount, "раз(а)")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/samrab1.jpg)

## Выводы
Программа вычисляет длины векторов по координатам, переданным через кортеж с именованными элементами **kwargs, и отображает время выполнения

---

### Задание 2

``` git
results = [10.2,14.8,19.3,22.7,12.5,33.1,38.9,21.6,26.4,17.1,30.2,35.7,16.9,
           27.8,24.5,16.3,18.7,31.9,12.9,37.4]
best_of_3 = sorted(results)[:3]
worst_of_3 = sorted(results)[-3:]
from_10 = results[10:]


print("Три лучших результата:", best_of_3)
print("Три худших результата:", worst_of_3)
print("Результаты начиная с 10:", from_10)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/samrab2.jpg)

## Выводы
Функция правильно моделирует бросок кубика и обрабатывает различные исходы с помощью конструкций if else

---

### Задание 3

``` git
import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def triangle_area(x, y, z):
    half_p = (x + y + z) / 2
    return math.sqrt(max(0, half_p * (half_p - x) * (half_p - y) * (half_p - z)))

sides_max = (max(one), max(two), max(three))
sides_min = (min(one), min(two), min(three))

area_max = triangle_area(*sides_max)
area_min = triangle_area(*sides_min)

print("Стороны (max):", sides_max, "Площадь: ", area_max)
print("Стороны (min): ", sides_min, "Площадь:", area_min)                        
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/samrab3.jpg)

## Выводы
Программа каждую секунду отображает текущее время в течение 5 секунд с использованием библиотеки datetime и функции strftime

---

### Задание 4

``` git
list_1 = [2,3,4,5,3,4,5,2,2,5,3,4,3,5,4]
list_2 = [4,2,3,5,3,5,4,2,2,5,4,3,5,3,4]
list_3 = [5,4,3,3,4,3,3,5,5,3,3,3,3,4,4]

def update_marks(values):
    result = []
    for mark in values:
        if mark == 2:
            continue
        result.append(4 if mark == 3 else mark)
    return result

fixed_1 = update_marks(list_1)
fixed_2 = update_marks(list_2)
fixed_3 = update_marks(list_3)

print("Вариант 1:", fixed_1)
print("Вариант 2:", fixed_2)
print("Вариант 3:", fixed_3)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/samrab4.jpg)

## Выводы
Функция вычисляет среднее значение для произвольного числа аргументов

---

### Задание 5

``` git
def make_special_set(nums):
    output = set()
    for value in set(nums):
        repeat = nums.count(value)
        output.add(value)
        for i in range(2, repeat + 1):
            output.add(str(value) * i)
    return output

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(make_special_set(list_1))
print(make_special_set(list_2))
print(make_special_set(list_3))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_5/pic/samrab5.jpg)

## Выводы
Программа вычисляет площадь треугольника по формуле Герона, разделяя логику на модуль и основной код

---

## Общие выводы по теме
Функции — это блоки кода, которые можно вызывать многократно, что помогает избежать дублирования и облегчает работу с программой

Модули — это отдельные файлы с функциями, которые подключаются через import, расширяя функциональные возможности программы

Конструкция if **name** == "**main**": указывает, что код внутри неё выполняется только при прямом запуске файла, а при импорте модуля не запускается, что позволяет разделять логику программы и функции

*args позволяет функции принимать произвольное количество аргументов, которые внутри функции представлены в виде кортежа
**kwargs позволяет функции принимать произвольное количество именованных аргументов (ключ=значение), которые внутри функции представлены в виде словаря

Кортежи (tuple) — это упорядоченные наборы данных, полезные для хранения фиксированных значений, которые не должны изменяться
