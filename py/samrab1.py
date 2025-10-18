def list_and_tuple(text):
    nums = []
    for part in text.split(','):
        part = part.strip()
        if part.isdigit():
            nums.append(int(part))
    return nums, tuple(nums)

if __name__ == '__main__':
    s = "1, 2, 3, 4, 5"
    lst, tpl = list_and_tuple(s)
    print("Изначальная строка -> ", s)
    print("Список -> ", lst)
    print("Кортеж -> ", tpl)