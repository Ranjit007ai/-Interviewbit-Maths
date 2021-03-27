def primefactor(num):
    li = [1]
    if num == 1:
        return 
    i = 2
    while num != 1:
        if num % i == 0:
            li.append(i)
            num //= i
        else:
            i += 1
    return li

        
            

def gcd(m,n):
    # finding the primefactors of m and n 
    pf_m = primefactor(m)
    pf_n = primefactor(n)
    l = min(len(pf_m),len(pf_n))
    res = 1
    for i in range(0,l):
        if pf_m[i] == pf_n[i]:
            res *= pf_m[i]
    return res

m = 9
n = 2
ans = gcd(m,n)
print(ans)