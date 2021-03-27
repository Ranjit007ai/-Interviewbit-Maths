def prime(num):
    # if the number is 1 then it is not prime number
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


num = 11
ans = prime(num)
print(ans)