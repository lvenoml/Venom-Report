# Enter your code here. Read input from STDIN. Print output to STDOUT
k=()
h=[]
n=int(input())
a=set(input().split())
m=int(input())
b=set(input().split())
z=a.difference(b)
x=b.difference(a)
#z=list(z).sort()
#b=list(x).sort()
k=z.union(x)
#print(z)
h=list(k)
for i in range(len(h)):
    h[i]=int(h[i])
h.sort()
for i in range(len(h)):
    print(h[i])
