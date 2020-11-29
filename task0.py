n = int(input("Enter n:"))
a = list(int(num) for num in input("Enter list a numbers:").strip().split())[:n]
b = list(int(num) for num in input("Enter list b numbers:").strip().split())[:n]
c = []    
for i in range(n):
   c.append(a[i] - b[i])
k = 0
p = 0
for i in range(n):
    if c[i] != 0:
      m = i  
      k = c[i]
      for i in range(m,n):
         if c[i] - k != 0:
           l = i
           for i in range(l,n):
             if c[i] != 0:
                 p += 1
                 break

if p == 0:
    print("YES")
else:
    print("NO")
