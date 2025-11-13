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