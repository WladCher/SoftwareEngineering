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