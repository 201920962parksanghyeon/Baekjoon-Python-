import sys

S = int(sys.stdin.readline())
N = []
for _ in range(S):
    N.append(int(sys.stdin.readline()))
N.sort()

for i in N:
    print(i)