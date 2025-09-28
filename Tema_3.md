# Тема 3. Операторы, условия, циклы
Отчет по Теме #3 выполнил:
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

## Лабораторная работа №2
### Задание 1

``` git
print(123)
print("123")
print(1.23)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab1.jpg)

## Выводы
Программа отображает три типа данных: строку, целое число и вещественное число

---

### Задание 2

``` git
print(1823-486)
print(5.1 + 8.27)
print(3+7.04+1+2.33)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab2.jpg)

## Выводы
Сложение и вычитание правильно выполняются с целыми числами, вещественными числами и их сочетанием

---

### Задание 3

``` git
print('Привет, Мир!')

world = 'Мир'
print(f"Привет, {world}!")

one = 'Привет, '
two = 'Мир!'
print(one+two)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab3.jpg)

## Выводы
Строки можно выводить напрямую, объединять с переменными и соединять между собой (конкатенация)

---

### Задание 4

``` git
one = 'Hello'
print(bool(one))

two = 142
print(float(two))

three = None
print(str(three))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab4.jpg)

## Выводы
Функции bool(), float() и str() используются для преобразования переменных в другие типы данных

---

### Задание 5

``` git
one = input('one:')
two = input('two:')
three = input('three:')
print(one, two, three)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab5.jpg)

## Выводы
Функция input() дает возможность вводить данные с клавиатуры и присваивать их переменным

---

### Задание 6

``` git
a = 12
b = 5
print('Возведение в степень:', a**b)
print('Обычное деление:', a/b)
print('Целочисленное деление:', a//b)
print('Нахождение остатка от деления:', a%b)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab6.jpg)

## Выводы
В Python доступны различные типы деления и вычисления остатка от деления

---

### Задание 7

``` git
line = 'Hello!'
print(line*6)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab7.jpg)

## Выводы
Строки можно умножать на целые числа, чтобы повторить их содержимое несколько раз

---

### Задание 8

``` git
sentence = 'Hello World'
print(sentence.count('o'))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab8.jpg)

## Выводы
Метод .count() подсчитывает, сколько раз символ или подстрока встречается в строке

---

### Задание 9

``` git
print('Hello\nWorld!')
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab9.jpg)

## Выводы
Символ \n используется для переноса текста на следующую строку внутри одной команды print()

---

### Задание 10

``` git
sentence = 'Hello World'
print(sentence[1])
print(sentence[:5])
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/lab10.jpg)

## Выводы
Индексация (\[ ]) позволяет извлечь конкретный символ, а срез (\[: ]) — выделить часть строки

---

## Самостоятельная работа №2
### Задание 1

``` git
print(bool(0))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab1.jpg)

## Выводы
Применение bool(0) дает False, потому что ноль воспринимается как ложное значение в логическом контексте

---

### Задание 2

``` git
a,b,c = 11,22,33
print(a,b,c)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab2.jpg)

## Выводы
С помощью одного выражения можно сразу присвоить значения нескольким переменным и затем вывести их в одной строке

---

### Задание 3

``` git
x = int(input())
print(x)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab3.jpg)

## Выводы
Функция int() преобразует строку в число, а при некорректном вводе (например, буквы) возникает ошибка ValueError

---

### Задание 4

``` git
a = "abcde"
print(a*8)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab4.jpg)

## Выводы
Умножение строки на число дает возможность многократного повторения её содержимого

---

### Задание 5

``` git
day,month,year = 22,"сентября",2025
print(f"Сегодня {day} {month} {year}.", end=" Всего хорошего!")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab5.jpg)

## Выводы
Форматированные строки (f"") позволяют легко вставлять переменные в текст

---

### Задание 6

``` git
a = "Hello World"
print(a.replace(" ", " my "))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab6.jpg)

## Выводы
Метод .replace() меняет подстроку в строке, что удобно для корректировки текста

---

### Задание 7

``` git
print(len("Hello World"))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab7.jpg)

## Выводы
Функция len() определяет число символов в строке

---

### Задание 8

``` git
print("HELLO WORLD".lower())
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab8.jpg)

## Выводы
Метод .lower() преобразует все символы строки в строчные

---

### Задание 9

``` git
a, b = 7, 4
print('сторона 1:', a, ', сторона 2:', b)
print('площадь:', a*b)
print('периметр:', 2*(a+b))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab9.jpg)

## Выводы
Функции сложения и умножения позволяют найти площадь и периметр фигуры

---

### Задание 10

``` git
a = "SoftwareEngineering"
print(len(a))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_2/pic/samrab10.jpg)

## Выводы
Функция len() определяет число символов в строке


## Общие выводы по теме
Python — это лёгкий и удобный язык для освоения основ программирования. В этих заданиях закреплены ключевые моменты:

Вывод данных: целые числа, строки, числа с плавающей точкой
- Преобразование типов: int, float, bool, str
- Ввод данных с клавиатуры через input()
- Различные виды деления, вычисление остатка, возведение в степень
- Операции со строками: конкатенация, умножение на число, замена подстроки, поиск символов
- Использование индексов и срезов для извлечения символов
- Работа с логическими значениями
- Форматированные строки для вывода переменных
Главное преимущество Python — простота и удобство, что делает его подходящим для разнообразных задач.
