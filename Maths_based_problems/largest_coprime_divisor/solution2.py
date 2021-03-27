# The idea is that the largest no divisble by A is A,check if A and B are coprime,i.e gcd(A,B) == 1 ,return X as A,
# Else remove the common factor of A and B from A .i.e A = A//gcd(A,B) ,while gcd(A,B) != 1
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)


def coprime(A,B):
    while(gcd(A,B)!=1):
        A = A//gcd(A,B)
    return A

A = 30
B = 12
ans = coprime(A,B)
print(ans)