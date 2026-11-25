arr=[100,101,100,102,101,100]
freq=[0]*6
for i in arr:
    freq[i-100]+=1
for i in range(len(freq)):
    print(f"{i+100} occurs {freq[i]} times")


         
