import random
import time


def sort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
               min = j
        a[i], a[min] = a[min], a[i]
    return a

times = [[]]
sample_time_count = 50
sample_list_count = 10
times.clear()

for j in range(sample_list_count):
    same_start_list = random.choices(range(1001), k=1000)
    times.append([])
    print(j)
    for i in range(sample_time_count):
        start_time = time.time()
        sort(same_start_list)
        times[j].append(time.time() - start_time)


min_time = float('inf')
max_time = 0
min_average = float('inf')
max_average = 0
total_average = 0

for list in times:
    temp = 0
    for t in list:
        min_time = min(t, min_time)
        max_time = max(t, max_time)
        total_average += t
        temp += t
    min_average = min(temp, min_average)
    max_average = max(temp, max_average)

print('min average = %.3f\n max average = %.3f' % (min_average / sample_time_count, max_average / sample_time_count))
print('total average time = %.3f[units?]\n min time = %.3f\n max time = %.3f' % (total_average / (sample_time_count * sample_list_count), min_time, max_time))
print('feel it?')
