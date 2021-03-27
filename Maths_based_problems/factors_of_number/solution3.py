def factors(num):
    factor_list = []

    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            factor_list.append(i)
            if num // i != i :
                factor_list.append(num//i)
    factor_list.sort()
    return factor_list


num = 10
ans = factors(num)
print(ans)
