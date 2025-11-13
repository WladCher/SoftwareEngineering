def plus_two():
    try:
        num = float(input("Введите число: "))
        print("Ответ:", num + 2)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    plus_two()