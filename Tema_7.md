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
Файл должен располагаться в той же директории, что и файл с кодом

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
С помощью readline() можно считать строку из файла, а open позволяет указать путь к файлу и режим доступа — здесь используется r

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
С помощью readlines() строки файла считываются в виде массива

---

### Задание 4

``` git
with open('input1.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_7/pic/lab4.jpg)

## Выводы
Конструкция with open обеспечивает удобное и безопасное использование файла в программе

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
Каждую строку файла можно выводить отдельно с помощью цикла

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
Различные режимы доступа к файлу дают разные возможности работы с ним; например, режим a+ позволяет добавлять строки в файл

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
С помощью цикла можно одновременно записать в файл несколько строк

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
Модуль os предоставляет возможности для работы с функциями операционной и файловой системы

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
Можно обрабатывать строки из файла и находить среди них слово с максимальной длиной

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
С помощью функций для работы с файлами можно открывать CSV-файлы и записывать в них данные

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
Программа правильно подсчитала общее количество слов в файле и выявила слово, встречающееся чаще всего

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
Программа позволяет добавлять новые расходы и просматривать весь список трат из файла, корректно записывая и считывая данные

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
Программа корректно подсчитала статистику текстового файла, определив количество букв, слов и строк

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
Все запрещённые слова заменяются звёздочками с сохранением длины и без учёта регистра

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
Программа позволяет пользователю добавить новую задачу в список и сохраняет её в текстовом файле, демонстрируя взаимодействие с файлом для хранения и отображения данных

---

## Общие выводы по теме

Работа с файлами является одним из базовых навыков Python-разработчика


Открытие и чтение файлов (open, read, readlines) позволяет получать данные из внешних источников

Запись файлов (write, writelines, режим a) используется для сохранения и дополнения информации

Контекстный менеджер (with open(...)) обеспечивает автоматическое закрытие файла

Обработка текста (split, replace, re) позволяет анализировать и модифицировать содержимое


Изучение этой темы даёт возможность создавать полноценные программы для чтения, анализа и сохранения данных, делая Python эффективным инструментом для реальных задач

