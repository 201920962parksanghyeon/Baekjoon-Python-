a = int(input())

arr = list(map(int, input().split()))

b = int(input())
c = 0
j = 0

for j in range(a):
   if(arr[j] == b):
      c = c+1

print(c)
