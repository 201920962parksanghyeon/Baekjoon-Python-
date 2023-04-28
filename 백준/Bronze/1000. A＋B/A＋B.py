a,b = input().split()
a = int(a)
b = int(b)
if(0<a):
    if(b<10):
      print(a+b)
    else:
      print("b값은 10보다 작아야합니다.")
else:
    print("a는 0보다는 커야합니다.")
