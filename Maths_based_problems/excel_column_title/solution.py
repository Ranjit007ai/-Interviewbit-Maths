def excel(num):
    # S is the list of string
    S = []
    while num != 0 :
        re = num % 26
        if re == 0:
            S.append('Z')
            num = (num // 26) - 1  
        else:
            s = chr(ord('A') + re - 1 )
            S.append(s)
            num = num // 26
    S.reverse()
    return ''.join(S)

num = 28
ans = excel(num)
print(ans)