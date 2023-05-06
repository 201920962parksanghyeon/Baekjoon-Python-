Case = int(input())
for i in range(Case):
    A,B = map(int, input().split())
    if(A>0 and B<10):
      print(A+B)
    else:
        print("A는 0보다 커야하며, B는 10보다 작아야합니다.")