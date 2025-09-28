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

## Лабораторная работа №3
### Задание 1

``` git
one = int(input("Введите значение первой переменной: "))
two = int(input("Введите значение второй переменной: "))
if one >= two:
    print("Выполняется")
else:
    print("Не выполняется")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab1.jpg)

## Выводы
Программа правильно обрабатывает и сравнивает введённые данные

---

### Задание 2

``` git
one = int(input("Введите значение переменной: "))
if one < 0:
    print("Меньше 0")
elif 0 < one < 10:
    print("Переменная больше 0 и меньше 10")
else:
    print("Переменная больше 10")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab2.jpg)

## Выводы
Программа корректно определяет три диапазона значений

---

### Задание 3

``` git
numbers = [1, 3, 4, 6, 8, 9]
value = int(input("Введите значение переменной: "))
if value in numbers:
    print("Переменная есть в данном массиве")
else:
    print("Переменной нет в этом массиве")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab3.jpg)

## Выводы
Оператор in удобно использовать для поиска элемента в массиве

---

### Задание 4

``` git
numbers = [1, 3, 4, 6, 8, 9, 15, 16, 73, 321, 322]
value = int(input("Введите значение переменной: "))
if value in numbers:
    if value % 2 == 0:
        print("Переменная четная и есть вмассиве")
    else:
        print("Переменная нечетная и есть в массиве")
else:
    print(f"Переменной нет в массиве и она равна {value}")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab4.jpg)

## Выводы
Программа проверяет как наличие числа, так и его чётность

---

### Задание 5

``` git
for i in range(10):
    print('i = ', i)
    if i ==0:
      i+=2
    if i == 1:
      continue
    if i == 2 or i == 3:
      print("Переменная равна 2 или 3")
    elif i in [4,5,6]:
      print("Переменная равна 4, 5 или 6")
    else:
      break
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab5.jpg)

## Выводы
Цикл демонстрирует работу операций сравнения

---

### Задание 6

``` git
string = "Привет всем изучающим Python!"
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква '{value}' есть в строке под {index} индексом")
        break
else:
    print(f"Буквы '{value}' нет в указанной строке")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab6.jpg)

## Выводы
Оператор else в цикле срабатывает только при отсутствии break
---

### Задание 7

``` git
value = 100
for i in range(10, -1, -1):
    value -= i
    print(i, value)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab7.jpg)

## Выводы
Цикл for можно легко организовать в обратном порядке

---

### Задание 8

``` git
value = 0
while value < 100:
    if value == 0:
      value+=10
    elif value // 5 > 1:
      value*=5
    else:
      value-=5
    print(value)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab8.jpg)

## Выводы
При корректном условии цикл while завершает работу правильно

---

### Задание 9

``` git
value = 0
for i in range(10):
    for j in range(10):
        if i != j:
          value+=j
        else:
          pass
print(value)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab9.jpg)

## Выводы
Вложенные циклы дают возможность проверять различные комбинации значений

---

### Задание 10

``` git
even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True
        break
if flag is True:
  print("В массиве есть нечетное число")
else:
  print("В массиве все числа четные")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/lab10.jpg)

## Выводы
Переменная flag удобно применять как индикатор выполнения условия

---

## Самостоятельная работа №3
### Задание 1

``` git
x = 1
for i in range(2): 
    x *= 5
    x += 1
print(x)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab2.jpg)

## Выводы
Программа выполняет задачу, используя исключительно разрешённые операции

---

### Задание 2

``` git
for ch in "Hello World"[::-1]:
    print(ch)
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab3.jpg)

## Выводы
Строка выводится по символам в обратном порядке

---

### Задание 3

``` git
x = int(input("Введите число 0-10: "))
if 0 <= x <= 10:
    if x <= 3:
        print("0–3")
    elif x <= 6:
        print("3–6")
    else:
        print("6–10")
else:
    print("Число вне диапазона")
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab4.jpg)

## Выводы
Программа правильно обрабатывает диапазоны чисел

---

### Задание 4

``` git
s = input("Введите предложение: ")
print("Длина:", len(s))
print("Нижнем регистр:", s.lower())
print("Количество гласных:", sum(ch in "aeiou" for ch in s.lower()))
print("Замена ugly:", s.replace("ugly", "beauty"))
print("Начинается с 'The':", s.startswith("The"))
print("Заканчивается на 'end':", s.endswith("end"))
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab5.jpg)

## Выводы
Программа выполняет все операции со строкой: подсчитывает символы, переводит в нижний регистр, считает количество гласных с помощью строки гласных, заменяет слова в предложении, начинает строку с The и завершает на end

---

### Задание 5

``` git
string = 'hello'
values = [0,2,4,6,8,10]
counter = 0
while ' world' not in string:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    if counter < 10:
        string = memory
    counter += 1
```
### Результат.
![Меню](https://github.com/WladCher/SoftwareEngineering/blob/Tema_3/pic/samrab1.jpg)

## Выводы
Программа отображает необходимые строки в консоли

---

## Общие выводы по теме
Операторы выполняют арифметические действия, сравнения и работу с логическими выражениями. Условные конструкции (if, elif, else) позволяют выбирать различные ветви выполнения программы в зависимости от входных данных. Циклы (for, while) дают возможность повторять действия многократно: for удобен для перебора последовательностей, а while — для выполнения действий до наступления определённого условия. Дополнительно, использование break, continue, else в циклах и переменных-индикаторов (flag) обеспечивает гибкое управление выполнением кода.
