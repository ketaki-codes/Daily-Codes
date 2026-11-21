arr = [10, 20, 30, 10, 40]
x = 10
j = 0

for i in range(0, len(arr), 1):
    if arr[i] != x:
        arr[j] = arr[i]
        j = j + 1

for i in range(j, len(arr), 1):
    arr.pop()

print(arr)      
