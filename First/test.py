def primenumbers(num):
    if num < 2:
        return []

    start_list = list(range(3, num + 2, 2))
    out_list = [2]

    for i in range(int((num - 1) / 2)):
        if start_list[i] != 0:
            out_list.append(start_list[i])
            for j in range(i, int((num - 1) / 2), start_list[i]):
                start_list[j] = 0
    return out_list


a = 1
for i in primenumbers(35):
    a *= i

print(a)