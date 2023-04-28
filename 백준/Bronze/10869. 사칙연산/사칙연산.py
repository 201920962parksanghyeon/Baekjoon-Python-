a,b = input().split()
a = int(a)
b = int(b)
c = int(a/b)
if(1<=a):
    if(b<=10000):
      print(a+b)
      print(a-b)
      print(a*b)
      print(c)
      print(a%b)
    else:
      print("b값은 10000보다 작아야합니다.")
else:
    print("a는 1보다는 커야합니다.")
