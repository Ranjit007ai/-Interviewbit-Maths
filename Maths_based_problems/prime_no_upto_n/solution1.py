# function to find if the number is prime number or not
def isprime(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# function to find all the prime numbers upto n(Including n)
def all_prime(num):
    prime_list = []
    # since 1 is never a prime number so iterating from 2
    for i in range(2,num+1):
        if isprime(i):
            prime_list.append(i)
    return prime_list

num = 10
ans = all_prime(num)
print(ans)