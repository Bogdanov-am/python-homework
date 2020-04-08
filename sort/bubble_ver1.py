import matplotlib.pyplot as plt
import random
import time

def sort(a):

    for j in range(len(a)):
        need_sort = False
        for i in range(len(a) - 1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                need_sort = True
        if not need_sort:
            break
    return a


times = []
# sort_list = []
#
# step = 1
# to = 1
#
# for i in [i * 10 for i in range(1, to, step)]:
#
#     start_list = random.choices(range(i), k=i)
#     start_time = time.time()
#     sort_list = sort(start_list)
#     times.append(time.time() - start_time)


#plt.plot([i * 1000 for i in range(1, to, step)], times)  # thats why constants should be named!
#plt.show()  # axis labels!

sample_count = 100
times.clear()
same_start_list = random.choices(range(10001), k=10000)
for i in range(sample_count):
    start_time = time.time()
    sort(same_start_list)
    times.append(time.time() - start_time)


min_time = float('inf')
max_time = 0
average = 0
for t in times:
    min_time = min(t, min_time)
    max_time = max(t, max_time)
    average += t
print('average time = %.6f[units?]\n min time = %.6f\n max time = %.6f' % (average / len(times), min_time, max_time))
print('feel it?')
