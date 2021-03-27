def factors(num):
     # 1 and the num itself are always the factor of nums so
    factors_list = [1,num]
    for i in range(2,(num//2) + 1):
        if num % i == 0:
            factors_list.append(i)
    factors_list.sort()
    return factors_list

num = 10
ans = factors(num)
print(ans)