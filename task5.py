from itertools import combinations


def foo(a, b):
    for index, (val_a, val_b) in enumerate(zip(a, b)):
        if val_a != val_b:
            return index
    return min(len(a), len(b))


lst_array: list[list[int]] = []
cnt_array: int = int(input())
for _ in range(cnt_array):
    cnt_el = int(input())
    array = list(map(int, input().split()))
    lst_array.append(array)

total_closeness = sum(foo(a, b) for a, b in combinations(lst_array, 2))
print(f'Близость {total_closeness}')
