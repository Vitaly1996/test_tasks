from collections import Counter


def diversity_calculation(collection_1: Counter, collection_2: Counter) -> int:
    general = collection_1 & collection_2
    unique_1 = collection_1 - general
    unique_2 = collection_2 - general
    return sum(unique_1.values()) + sum(unique_2.values())


n, m, q = map(int, input().split())
A = Counter(map(int, input().split()))
B = Counter(map(int, input().split()))

diversity: list[int] = []

for _ in range(q):
    type_actions, player, card = input().split()
    type_actions = int(type_actions)
    card = int(card)
    if player == 'A':
        if type_actions == 1:
            A[card] += 1
        else:
            A[card] -= 1
            if A[card] == 0:
                del A[card]
    else:
        if type_actions == 1:
            B[card] += 1
        else:
            B[card] -= 1
            if B[card] == 0:
                del B[card]
    # calculation the diversity for every iteration
    diversity.append(diversity_calculation(A, B))
print(*diversity)
