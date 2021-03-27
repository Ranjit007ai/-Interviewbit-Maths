# the idea is to find the primes number till the given number using sieve algo
# then check if the pair of sum is present or not if Yes then return them
def prime_nos(num):
    prime_list = [True]* (num+1)
    prime_list[0] = False
    prime_list[1] = False
    for i in range(2,num+1):
        for j in range(2,num//i):
            prime_list[i*j] = False

    # Now at this stage ,in the prime_list all the prime number are marked True
    # We know that sum of two number = num i.e A[i] + A[num-i] ,so both are True then return them
    for i in range(0,num+1):
        if prime_list[i] and prime_list[num - i]:
            return i,(num-i)

# According to Goldman conjection ,every even number greater than 2 can be expressed as sum of two prime numbers.
num = 10
p1,p2 = prime_nos(num)
print(p1,p2)