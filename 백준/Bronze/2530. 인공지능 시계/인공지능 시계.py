H,M,S = map(int,input().split())
C = int(input())

S=H*3600+M*60+S+C

M,S =divmod(S,60)
H,M =divmod(M,60)

H=H%24

print(H,M,S)
