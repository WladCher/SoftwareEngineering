# Тема 7. Работа с файлами (ввод, вывод)
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
Hello world!
SoftwareEngineering
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab1.jpg)

## Выводы
Словари позволяют удобно обращаться к элементам по ключу, заменяя конструкции if/elif/else

---

### Задание 2

``` git
f = open('input1.txt','r')
print(f.readline())
f.close()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab2.jpg)

## Выводы
С помощью функций и **kwargs можно динамически создавать словари, а pprint обеспечивает удобный вывод информации

---

### Задание 3

``` git
f = open('input1.txt','r')
print(f.readlines())
f.close()
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab3.jpg)

## Выводы
С помощью tuple можно разложить строку по символам без использования условий

---

### Задание 4

``` git
with open('input1.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab4.jpg)

## Выводы
В качестве аргумента функции можно передавать кортеж

---

### Задание 5

``` git
with open('input1.txt') as f:
    for line in f:
        print(line)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab5.jpg)

## Выводы
Кортеж можно сортировать и проверять каждый его элемент

---

### Задание 6

``` git
with open('input1.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input1.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab6.jpg)

## Выводы
Словари позволяют удобно обращаться к элементам по ключу, заменяя конструкции if/elif/else

---

### Задание 7

``` git
lines = ['one', 'two', 'three']
with open('input1.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab7.jpg)

## Выводы
С помощью функций и **kwargs можно динамически создавать словари, а pprint обеспечивает удобный вывод информации

---

### Задание 8

``` git
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-'*40)

print_docs('D:/учеба/3_курс/Программная_инжинерия/Лаб_7/py')
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab8.jpg)

## Выводы
С помощью tuple можно разложить строку по символам без использования условий

---

### Задание 9

``` git
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab9.jpg)

## Выводы
В качестве аргумента функции можно передавать кортеж

---

### Задание 10

``` git
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
    time.sleep(0.01)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab10.jpg)

## Выводы
Кортеж можно сортировать и проверять каждый его элемент

---

## Самостоятельная работа №7
### Задание 1

``` git
from collections import Counter

with open("article.txt", encoding="utf-8") as f:
    text = f.read().lower().split()

word_count = len(text)
most_common = Counter(text).most_common(1)[0]

print(f"Количество слов: {word_count}")
print(f"Самое частое слово: '{most_common[0]}' — встречается {most_common[1]} раз(а)")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab1.jpg)

## Выводы
Простая и надёжная функция вручную разбивает строку, преобразует элементы в целые числа и возвращает список и кортеж, корректно обрабатывая пробелы и пустые токены

---

### Задание 2

``` git
def append_record(file_path):
    cat = input("Введите категорию: ")
    cost = float(input("Введите сумму: "))
    comment = input("Добавьте комментарий: ")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{cat},{cost},{comment}\n")

def display_records(file_path):
    with open(file_path, encoding="utf-8") as file:
        for record in file:
            cat, cost, comment = record.rstrip().split(",")
            print(f"{cat}: {cost} руб. — {comment}")

if __name__ == "__main__":
    append_record("expenses.txt")
    print("\nСписок расходов:")
    display_records("expenses.txt")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab2.jpg)

## Выводы
Функция удаляет первое найденное вхождение, при этом кортеж остаётся неизменяемым — создаётся новый. Если элемент отсутствует, возвращается исходный кортеж

---

### Задание 3

``` git
with open("input.txt", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)
letters = sum(ch.isalpha() for ch in text)
words = len(text.split())
lines_count = len(lines)

print("Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines_count} lines")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab3.jpg)

## Выводы
Для выбора трёх наиболее частых элементов используется алгоритм, выбирающий максимум три раза
Итоговый словарь содержит ровно три пары {digit: count} (если в исходном тексте меньше трёх различных цифр — возвращает столько, сколько есть), при этом ключи при выводе упорядочены по возрастанию

---

### Задание 4

``` git
import re

with open("input.txt", encoding="utf-8") as file:
    forbidden = file.read().split()

sample_text = "Приветствие, Спасибо, Ты готов? До завтра! Вчера было тепло"

for term in forbidden:
    mask = re.compile(term, re.IGNORECASE)
    sample_text = mask.sub("*" * len(term), sample_text)

print(sample_text)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/samrab4.jpg)

## Выводы
Функция правильно обрабатывает все три случая: 0, 1 и ≥2 вхождения

---

### Задание 5

``` git
import os

def add_task():
    task = input("Введите новую задачу: ")
    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")

def show_tasks():
    if not os.path.exists("tasks.txt"):
        print("Список задач пока пуст.")
        return
    with open("tasks.txt", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]
    print("\nВаши задачи:")
    for num, task in enumerate(tasks, 1):
        print(f"{num}. {task}")

if __name__ == "__main__":
    add_task()
    show_tasks()
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
