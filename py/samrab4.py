def first_to_second(tpl, value):
    if value not in tpl:
        return ()
    first = tpl.index(value)
    if value not in tpl[first + 1:]:
        return tpl[first:]
    second = tpl.index(value, first + 1)
    return tpl[first:second + 1]

if __name__ == '__main__':
    print(first_to_second((1, 2, 3), 8))
    print(first_to_second((1, 8, 3, 4, 8, 9, 2), 8))
    print(first_to_second((1, 2, 8, 5, 1, 2, 9), 8))