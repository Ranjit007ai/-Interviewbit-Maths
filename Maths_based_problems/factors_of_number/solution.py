def factors(num):
    factors_list = []
    for i in range(1,num+1):
        if num % i == 0:
            factors_list.append(i)
    return factors_list


num = 10
ans = factors(num)
print(ans)
