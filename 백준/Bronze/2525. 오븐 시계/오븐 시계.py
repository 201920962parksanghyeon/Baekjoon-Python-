T, M = map(int, input().split())
C = int(input())

h = (M+C)//60
m = (M+C)%60

if(M + C >= 60):
  if(T+h >= 24):
    T = T - 24
  T = T + h
  print(T, m)

else:
  if(T >= 24):
    T = T - 24
  print(T, M+C)