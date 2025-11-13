import time

def measure_time(func):
    def inner(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_finish = time.time()
        duration = t_finish - t_start
        print(f"\nПрограмма выполнилась за {duration:.4f} секунд")
        return result
    return inner

@measure_time
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' , ')

if __name__ == '__main__':
    fibonacci()