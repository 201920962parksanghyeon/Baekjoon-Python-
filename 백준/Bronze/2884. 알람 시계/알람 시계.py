H,M = map(int, input().split())

if( M < 45):
    if H==0:
        H=23
        M=M+60
    else:
        H=H-1
        M += 60
S = M-45
print(H,S)