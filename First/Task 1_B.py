# AX + BY = 1
# if A > B then X > 0 and Y < 0
# if B > A then X < 0 and Y > 0

def find_ab(firstIn, secondIn):
    for i in range(10000):
        if (1 - firstIn * i) % secondIn == 0:
            if int((1 - firstIn * i) / secondIn) < 10000:
                return i, int((1 - firstIn * i) / secondIn)
    return 0, 0


A = int(input())
B = int(input())

if A > B:
    X, Y = find_ab(A, B)
else:
    Y, X = find_ab(B, A)

print(X, Y)
