import matplotlib.pyplot as plt
import random
import time


def sort(a):
    k = 1.247330950103979  # overprecision.
    # sample count is set to 100, which gives you not more than 3 meaning digits.
    # Do not print such long numbers, or your scientific work would be considered bullshit.
    # Measuring the fucking room temperature with +- 0.01 degree error is a miracle, which costs quite a lot.
    #step = float(len(a))/k  # why do you need floating point cast?
    step = len(a)/k
    for j in range(len(a)):
        need_sort = False
        #int_step = int(round(step))  # round already gives you an integer
        # print(type(round(step)))
        int_step = round(step)  # mb int() is faster than round()

        for i in range(len(a) - int_step):
            if (a[i] > a[i + int_step]):
                a[i], a[i + int_step] = a[i + int_step], a[i]
                need_sort = True
        # if int_step == 1:
        #    if not need_sort:
        if not need_sort and int_step == 1:  # need_sort is already boolean which does not need computation
            # also, "not need_sort" appears more rare, than "int_step == 1", which results in:
            # https://en.wikipedia.org/wiki/Short-circuit_evaluation
            # also, now you use "not need_sort", which takes time to compute.
            # you can switch back to "sorted" and save 1 atomic per iteration.
            break
        #step = step / k  # division is much slower than multiplication! keep than in mind
        step /= k  # make use of binary operators
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
same_start_list = random.choices(range(10001), k=10000)  # this was an example of time averaging.
# averaging of random input is also required
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
print('average time = %.3f[units?]\n min time = %.3f\n max time = %.3f' % (average / len(times), min_time, max_time))
print('feel it?')
