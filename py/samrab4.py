def average(*args):
    return sum(args) / len(args)

if __name__ == "__main__":
    print("Среднее арифметическое - ", average(4, 12, 8, 1, 2))