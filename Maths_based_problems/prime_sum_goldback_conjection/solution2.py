# The idea is that sum for Num is A[i]+ A[sum-i],and we are going to check if does numbers are prime or not . if yes then return them.
def isprime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def goldman(num):
    for i in range(0,num+1):
        if isprime(i) and isprime(num-i):
            return i, (num - i)

num = 10
p1, p2 = goldman(num)
print(p1,p2)
