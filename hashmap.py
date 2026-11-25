def countfreq(n):
  freq=[0]*10
  while (n != 0):
    last_digits=n%10
    freq(last_digits)+=1
    n//=10

  return freq  
n=1323156875
res=countfreq(n)

for i in range(len(res)):
  print(f"{i}->{res[i]}")

    

