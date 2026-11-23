
arr=[3,2,2,3]
val=3
j=0

for i in range(0,len(arr),1):
    if arr[i]!=val:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1

print(j)
print(arr)