def print_rangoli(size):
    # your code goes here
    for i in range(size-1):
        a=("-"*(size-1-i)*2)+i*("*"+"-")+"*"+i*("-"+"+")+("-"*(size-1-i)*2)
        for j in range(size):
            a=a.replace("*",chr(96+size-j),1)
            a=a.replace("+",chr(96-i+size+1+j),1)
        print(a)
    for i in range(size-1,-1,-1):
        a=(("-"*(size-1-i)*2)+i*("*"+"-")+"*"+i*("-"+"+")+("-"*(size-1-i)*2))
        for j in range(size):
            a=a.replace("*",chr(96+size-j),1)
            a=a.replace("+",chr(96+j+size+1-i),1)
        print(a)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
