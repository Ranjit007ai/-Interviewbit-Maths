def factors(num):
    li = []
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            li.append(i)
            if num // i != i :
                li.append(num //i )
    return li

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

def coprime(A,B):
    # first finding the factors of A
    f_list = factors(A)
    # now Traversing the the f_list from right to left and checking if gcd() == 1
    for i in range(len(f_list)-1,-1,-1):
        if gcd(f_list[i],B) == 1:
            return f_list[i]
    
A = 30
B = 12 
ans = coprime(A,B)
print(ans)
