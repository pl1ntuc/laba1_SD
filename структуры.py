import math

def max_gcd_split(N):
    max_d = 1
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i <= N // 2:
                max_d = max(max_d, i)
            if N // i <= N // 2:
                max_d = max(max_d, N // i)
    return max_d, N - max_d
with open('input.txt', 'r') as infile:
    N = int(infile.readline().strip())
    
A, B = max_gcd_split(N)   

with open('output.txt', 'w') as outfile:
    outfile.write(f"{A} {B}\n")
