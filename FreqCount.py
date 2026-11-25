def countfreq(n,k):
  freq=[0]*10
  
  while (n != 0):
    last_digits=n%10
    freq[last_digits]+=1
    n//=10
  res=[]

  for i in range(len(freq)):
    if freq[i] >= k:
     res.append(i)
  return res

 n=155232154

res=countfreq(n,3)
print(res)

