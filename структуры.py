import math

def nod(N):
    max_d = 1
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i <= N // 2:
                max_d = max(max_d, i)
            if N // i <= N // 2:
                max_d = max(max_d, N // i)
    return max_d, N - max_d

N = int(input())
A, B = nod(N)
print(A, B)
