n = int(input())
a = []
for i in range(n):
  a.append(int(input()))

max_n = 0
for i in range(len(a)-1):
  if (a[i-1]+a[i]+a[i+1]) > max_n:
    max_n = a[i-1]+a[i]+a[i+1]
    
if (a[-2]+a[-1]+a[0])  > max_n:
  max_n = a[-2]+a[-1]+a[0]
  
print(max_n)  