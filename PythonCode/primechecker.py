def prime(n):
    if n == 1:
        return False
    for i in range(2, int((n**0.5)+1)):
        if n % i == 0:
            return False
    return True

Prime_checked = int(input("Input number to be checked for prime: "))
try:
    int(Prime_checked)
    Check = prime(Prime_checked)
    if Check == True:
        print("The number is a prime number")
    else:
        print("The number is not a prime number")
except:
    print("Number inputted is not an int")
