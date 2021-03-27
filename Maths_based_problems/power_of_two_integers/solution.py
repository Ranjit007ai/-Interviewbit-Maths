def powers(num):
    if num == 1:
        return True
    for i in range(2,int(num**0.5)+1):
        cur_num = i
        while cur_num < num:
            cur_num = cur_num * i
        if cur_num == num :
            return True
    return False

num = 10
ans = powers(num)
print(ans)
