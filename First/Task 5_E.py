import time
import random

# start_list = [int(i) for i in input().split(' ')]
start_list = [random.randrange(1, 1500, 1) for i in range(3000000)]

# start_time = time.time()
#
# out_list = []
#
# for a in start_list:
#     if not a in out_list:
#         out_list.append(a)
#
# print(len(out_list))
# print("---%s seconds---" % (time.time() - start_time))


start_time = time.time()

m = 0
for a in range(1, 1500, 1):
    if a in start_list:
        m += 1


print(m)
print("---%s seconds---" % (time.time() - start_time))


# start_time = time.time()
#
# i = 0
# size = len(start_list)
# while i < size:
#     j = i + 1
#     while j < size:
#         if start_list[j] == start_list[i]:
#             del start_list[j]
#             size -= 1
#         else:
#             j += 1
#     i += 1
#
# print(len(start_list))
# print("---%s seconds---" % (time.time() - start_time))

