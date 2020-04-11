import random
import time
import copy

def sort(a):
    for i in range(len(a)):
        j = i - 1
        while j >= 0 and a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            j -= 1
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
        temp_list = copy.copy(same_start_list)
        start_time = time.time()
        sort(temp_list)
        times[j].append(time.time() - start_time)
        temp = time.time() - start_time


min_time = float('inf')
max_time = 0
min_average = float('inf')
max_average = 0
total_average = 0

print(times)
for list in times:
    temp = 0
    for t in list:
        min_time = min(t, min_time)
        max_time = max(t, max_time)
        total_average += t
        temp += t
    min_average = min(temp, min_average)
    max_average = max(temp, max_average)

print('min average = %.3fs\n max average = %.3fs' % (min_average / sample_time_count, max_average / sample_time_count))
print('total average time = %.3fs\n min time = %.3fs\n max time = %.3fs' % (total_average / (sample_time_count * sample_list_count), min_time, max_time))
print('feel it?')
