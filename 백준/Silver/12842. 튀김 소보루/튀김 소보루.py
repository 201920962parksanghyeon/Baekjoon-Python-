from sys import stdin
z=1
j=1

n,s = map(int,stdin.readline().split())

m = int(stdin.readline())
t = [0]* m
for a in range(m):
   t[a]= (int(stdin.readline()))

sum = 0
for z in range (0,n-s):
   for j in range(m):
      if(z % t[j] == 0):
         sum= sum+1
         if(sum >= n-s):
            print(j+1)
            exit()