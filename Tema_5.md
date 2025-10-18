# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил:
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

## Лабораторная работа №6
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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/lab1.jpg)

## Выводы
В множествах дубликаты удаляются автоматически, а операция set_1 - set_2 отображает различия между ними

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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/lab2.jpg)

## Выводы
Множество set является изменяемым, а frozenset — неизменяемым

---

### Задание 3

``` git
input_string = 'HelloWorld'
result=tuple(input_string)
print(result)
print(list(result))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/lab3.jpg)

## Выводы
Перестановку можно выполнить одной строкой с помощью множественного присваивания

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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/lab4.jpg)

## Выводы
Срез [2:6] возвращает элементы с индексами от 2 до 5 включительно

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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/lab5.jpg)

## Выводы
Функция возвращает «бесполезное число» — результат деления наибольшего элемента на длину списка

---

## Самостоятельная работа №6
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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/samrab1.jpg)

## Выводы
Подсчёт выполняется стандартными средствами: len() — общее количество, set() — уникальные элементы, Counter — наиболее часто встречающийся элемент

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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/samrab2.jpg)

## Выводы
Для выбора лучших и худших используется sorted(), срезы возвращают подмножества по индексам, а фильтрация по условию выполняется через list comprehension

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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/samrab3.jpg)

## Выводы
Построение треугольников из экстремальных значений списков и использование формулы Герона дают ожидаемые площади

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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/samrab4.jpg)

## Выводы
Функция fix_grades возвращает новый список без двоек и с исправленными оценками

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
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_6/pic/samrab5.jpg)

## Выводы
Вложенным циклом подсчитывается количество повторений каждого числа, число добавляется в множество, а через while создаются строки 'x', повторяющиеся в зависимости от количества

---

## Общие выводы по теме
Все задачи решаются стандартными средствами Python: set, list (срезы), sorted, Counter и другие

Для работы с повторяющимися элементами и подсчётом частот удобно применять Counter

Полезные функции для работы с массивами: pop(), sort(), add()
