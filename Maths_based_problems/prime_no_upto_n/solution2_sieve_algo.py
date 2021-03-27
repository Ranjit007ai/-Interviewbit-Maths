def sieve(num):
    # create a list from 0 to num and assume all are prime number intially (True)
    prime_list = [True] * (num+1)
    # now we all know that 0 and 1 are not a prime number
    prime_list[0] = False
    prime_list[1] = False
    # The idea is that the multiple of prime no are not prime numbers
    # traversing the list
    for i in range(2,num+1):
        if prime_list[i] == True:
            # j is for multiple of i : i*2,i*3.....
            for j in range(2,num//i):
                prime_list[i*j] = False
    # now at end all the positions having True are the prime numbers
    final_list = []
    for i in range(2,num+1):
        if prime_list[i] == True:
            final_list.append(i)
    return final_list

num = 10
ans = sieve(num)
print(ans)