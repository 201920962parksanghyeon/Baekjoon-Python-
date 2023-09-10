n = int(input())
file_names = [input() for _ in range(n)]

result = ''
for i in range(len(file_names[0])):
    chars = set(f[i] for f in file_names)
    if len(chars) == 1:
        result += next(iter(chars))
    else:
        result += '?'

print(result)
    
