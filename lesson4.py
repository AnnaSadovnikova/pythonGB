n = int(input())
a = []
for i in range(n):
  a.append(int(input()))

m = int(input())
b = []
for i in range(m):
  b.append(int(input()))

print(a)
print(b)
print(set(a).intersection(set(b)))  
for i in a:
  if i in b:
    print(i, end="")