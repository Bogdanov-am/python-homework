import math
import time

# используем решето Эратосфена для нахождения простых чисел
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


a = int(input())
b = []
temp = a

start_time = time.time()
prime_num = primenumbers(int(math.sqrt(a)))

i = 0

while i < len(prime_num):
    if temp % prime_num[i] == 0:
        temp = int(temp / prime_num[i])
        b.append(prime_num[i])
    else:
        i += 1

if 1 < temp < a:
    b.append(temp)

print("--- %s seconds ---" % (time.time() - start_time))
print(b)
