case = input()
case = int(case)
for i in range(0,case):
    A,B = map(int, input().split())
    C = A+B
    print(f"Case #{i+1}:",C)
    C = 0