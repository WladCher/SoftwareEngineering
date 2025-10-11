list_1 = [2,3,4,5,3,4,5,2,2,5,3,4,3,5,4]
list_2 = [4,2,3,5,3,5,4,2,2,5,4,3,5,3,4]
list_3 = [5,4,3,3,4,3,3,5,5,3,3,3,3,4,4]

def update_marks(values):
    result = []
    for mark in values:
        if mark == 2:
            continue
        result.append(4 if mark == 3 else mark)
    return result

fixed_1 = update_marks(list_1)
fixed_2 = update_marks(list_2)
fixed_3 = update_marks(list_3)

print("Вариант 1:", fixed_1)
print("Вариант 2:", fixed_2)
print("Вариант 3:", fixed_3)
