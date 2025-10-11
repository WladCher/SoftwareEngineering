def make_special_set(nums):
    output = set()
    for value in set(nums):
        repeat = nums.count(value)
        output.add(value)
        for i in range(2, repeat + 1):
            output.add(str(value) * i)
    return output

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(make_special_set(list_1))
print(make_special_set(list_2))
print(make_special_set(list_3))
