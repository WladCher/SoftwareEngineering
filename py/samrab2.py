def fib(n):
    a, b = 1, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    nums = list(fib(200))

    print("1–200 числа Фибоначчи:")
    print(*nums)

    with open("fib.txt", "w") as f:
        for number in nums:
            f.write(str(number) + "\n")