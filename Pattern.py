n = int(input("Enter the value of n:"))
a = list(range(1, n * 6 + 1))
k = 0
l = n*6-1

for i in range(n,0,-1):
    for j in range((n-i)*2):
        print("-",end='')
    for h in range(i):
        print(a[k],end="*")
        k+=1
    for d in range(i,0,-1):
        print(a[l-i+1],end = "*")
        l+=1
    print()
    l=l-i





    