arr=[0,1,0,3,12]
j=0
for i in range(0,len(arr),1):
    if (arr[i]!=0):
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j+=1      
print(arr)         