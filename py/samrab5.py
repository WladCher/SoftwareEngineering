from collections import Counter

def get_at_least_three(lst):
    counts = Counter(lst)
    seen = set()
    res = []
    for x in lst:
        if counts[x] >= 3 and x not in seen:
            res.append(x)
            seen.add(x)
    return tuple(res)

if __name__ == '__main__':
    print(get_at_least_three([1, 2, 3, 2, 1, 1, 2, 4]))
    print(get_at_least_three([7, 7, 7, 7]))
    print(get_at_least_three([1, 2, 3, 4]))
    print(get_at_least_three(['x','x','x','y','y','y','z']))