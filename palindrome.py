a=input()
x=len(a)
c=""
while x>0:
    b=a[x-1:x]
    c=c+b
    x-=1
if a==c:
    print('It is a palindrome')
else:
    print('It is not a palindrome')


