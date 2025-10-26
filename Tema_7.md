# Тема 7. Базовые коллекции: словари, кортежи
Отчет по Теме #7 выполнил:
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

## Лабораторная работа №7
### Задание 1

``` git
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab1.jpg)

## Выводы
Словари позволяют удобно обращаться к элементам по ключу, заменяя конструкции if/elif/else

---

### Задание 2

``` git
from pprint import pprint
my_dict = {'first':'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Владислав', age=20, weight=58, eyes_color='gray')
pprint(my_dict)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab2.jpg)

## Выводы
С помощью функций и **kwargs можно динамически создавать словари, а pprint обеспечивает удобный вывод информации

---

### Задание 3

``` git
input_string = 'HelloWorld'
result=tuple(input_string)
print(result)
print(list(result))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab3.jpg)

## Выводы
С помощью tuple можно разложить строку по символам без использования условий

---

### Задание 4

``` git
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab4.jpg)

## Выводы
В качестве аргумента функции можно передавать кортеж

---

### Задание 5

``` git
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5,5,3,1,9)))
    print(tuple_sort((5,5,2.1,'1',9)))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab5.jpg)

## Выводы
Кортеж можно сортировать и проверять каждый его элемент

---

### Задание 6

``` git
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab6.jpg)

## Выводы
Словари позволяют удобно обращаться к элементам по ключу, заменяя конструкции if/elif/else

---

### Задание 7

``` git
from pprint import pprint
my_dict = {'first':'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Владислав', age=20, weight=58, eyes_color='gray')
pprint(my_dict)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab7.jpg)

## Выводы
С помощью функций и **kwargs можно динамически создавать словари, а pprint обеспечивает удобный вывод информации

---

### Задание 8

``` git
input_string = 'HelloWorld'
result=tuple(input_string)
print(result)
print(list(result))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab8.jpg)

## Выводы
С помощью tuple можно разложить строку по символам без использования условий

---

### Задание 9

``` git
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab9.jpg)

## Выводы
В качестве аргумента функции можно передавать кортеж

---

### Задание 10

``` git
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5,5,3,1,9)))
    print(tuple_sort((5,5,2.1,'1',9)))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab10.jpg)

## Выводы
Кортеж можно сортировать и проверять каждый его элемент

---

## Самостоятельная работа №7
### Задание 1

``` git
def list_and_tuple(text):
    nums = []
    for part in text.split(','):
        part = part.strip()
        if part.isdigit():
            nums.append(int(part))
    return nums, tuple(nums)

if __name__ == '__main__':
    s = "1, 2, 3, 4, 5"
    lst, tpl = list_and_tuple(s)
    print("Изначальная строка -> ", s)
    print("Список -> ", lst)
    print("Кортеж -> ", tpl)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab1.jpg)

## Выводы
Простая и надёжная функция вручную разбивает строку, преобразует элементы в целые числа и возвращает список и кортеж, корректно обрабатывая пробелы и пустые токены

---

### Задание 2

``` git
def remove_first_element(tpl, value):
    if value not in tpl:
        return tpl
    index = tpl.index(value)
    return tpl[:index] + tpl[index + 1:]

if __name__ == '__main__':
    examples = [
        ((1, 2, 3), 1),
        ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
        ((2, 4, 6, 6, 4, 2), 9)
    ]

    for tpl, val in examples:
        print("Изначальный кортеж -> ", tpl, "Удалить -> ", val)
        res = remove_first_element(tpl, val)
        print("Результат -> ", res)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab2.jpg)

## Выводы
Функция удаляет первое найденное вхождение, при этом кортеж остаётся неизменяемым — создаётся новый. Если элемент отсутствует, возвращается исходный кортеж

---

### Задание 3

``` git
def get_digit_counts(text):
    counts = {}
    for ch in text:
        if ch.isdigit():
            num = int(ch)
            counts[num] = counts.get(num, 0) + 1
    return counts


def top3_digits(text):
    counts = get_digit_counts(text)
    if not counts:
        return {}

    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    top = sorted_items[:3]
    return dict(sorted(top))


if __name__ == '__main__':
    s = "987654321098765432109876543210987654"
    s2 = "000111222333444555666777888999000111222"

    all_counts = get_digit_counts(s2)
    top3 = top3_digits(s2)

    print("Cловарь -> ", all_counts)
    print("3 самых частых -> ", top3)           
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab3.jpg)

## Выводы
Для выбора трёх наиболее частых элементов используется алгоритм, выбирающий максимум три раза
Итоговый словарь содержит ровно три пары {digit: count} (если в исходном тексте меньше трёх различных цифр — возвращает столько, сколько есть), при этом ключи при выводе упорядочены по возрастанию

---

### Задание 4

``` git
def first_to_second(tpl, value):
    if value not in tpl:
        return ()
    first = tpl.index(value)
    if value not in tpl[first + 1:]:
        return tpl[first:]
    second = tpl.index(value, first + 1)
    return tpl[first:second + 1]

if __name__ == '__main__':
    print(first_to_second((1, 2, 3), 8))
    print(first_to_second((1, 8, 3, 4, 8, 9, 2), 8))
    print(first_to_second((1, 2, 8, 5, 1, 2, 9), 8))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab4.jpg)

## Выводы
Функция правильно обрабатывает все три случая: 0, 1 и ≥2 вхождения

---

### Задание 5

``` git
from collections import Counter

def get_at_least_three(lst):
    counts = Counter(lst)
    seen = set()
    res = []
    for x in lst:
        if counts[x] >= 3 and x not in seen:
            res.append(x)
            seen.add(x)
    return tuple(res)

if __name__ == '__main__':
    print(get_at_least_three([1, 2, 3, 2, 1, 1, 2, 4]))
    print(get_at_least_three([7, 7, 7, 7]))
    print(get_at_least_three([1, 2, 3, 4]))
    print(get_at_least_three(['x','x','x','y','y','y','z']))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab5.jpg)

## Выводы
Задача проверяет корректность подсчёта и сохранения порядка первого появления элементов

---

## Общие выводы по теме

Коллекции данных (списки, кортежи, множества, словари) являются основой для хранения и обработки информации в Python


Списки (list) — изменяемые упорядоченные коллекции, удобные для добавления и удаления элементов

Кортежи (tuple) — неизменяемые последовательности, часто используются для хранения фиксированных данных

Множества (set) — неупорядоченные коллекции уникальных элементов, полезные для удаления повторов

Словари (dict) — хранят пары ключ–значение и обеспечивают быстрый доступ к данным по ключу


Применение встроенных структур данных, таких как Counter и set, а также понимание принципов итерации и индексации позволяет создавать эффективные алгоритмы для анализа и обработки информации
