data = [75, 31, 33, 82, 10, 12, 9, 33, 71, 5, 42]

max_gaps = 0
max_gaps2 = 0
first_group = 0
second_group = 0

data_sorted = sorted(data)

for i in range(len(data_sorted) - 1):
    gap = data_sorted[i + 1] - data_sorted[i]
    if gap > max_gaps:
        max_gaps2 = max_gaps
        max_gaps = gap
        second_group = first_group
        first_group = i
    elif gap > max_gaps2:
        max_gaps2 = gap
        second_group = i

first_group, second_group = sorted([first_group, second_group])

final = []
for i in data:
    ind = data_sorted.index(i)
    if ind <= first_group:
        final.append(1)
    elif ind <= second_group:
        final.append(2)
    else:
        final.append(3)

print(final)
