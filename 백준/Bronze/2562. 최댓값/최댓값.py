i = 1

arr = []
max = 0
count=0
for i in range(0,9):
     arr.append(int(input()))
     if(max<arr[i]):
        max=arr[i]
        count=i+1

print(max)
print(count)