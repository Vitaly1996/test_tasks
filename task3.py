from collections import defaultdict

cnt_row, cnt_column, limit = list(map(int, input().split()))
column = input().split()
rows = [list(map(int, input().split())) for _ in range(cnt_row)]

limits = defaultdict(list)

for _ in range(limit):
    column_name, operator, value = input().split()
    value = int(value)
    column_index = column.index(column_name)
    limits[column_index].append((operator, value))


def row_satisfies_constraints(row):
    for column_index, checks in limits.items():
        for operator, value in checks:
            if operator == '>' and not row[column_index] > value:
                return False
            elif operator == '<' and not row[column_index] < value:
                return False
    return True


total_sum = sum(sum(row) for row in rows if row_satisfies_constraints(row))
print(total_sum)
