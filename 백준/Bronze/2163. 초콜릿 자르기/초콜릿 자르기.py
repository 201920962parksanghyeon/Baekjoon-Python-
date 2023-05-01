N,M = map(int,input().split())
if(N >= 1):
    if(M <= 300):
        sum= N * M - 1
        print(sum)
    else :
        print("M의 값은 300보다 적어야합니다.")
else:
 print("N의 값은 1보다 커야합니다.")

