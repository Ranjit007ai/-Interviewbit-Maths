def gcd_euclidean(m,n):
    if m == 0:
        return n
    return gcd_euclidean(n% m,m)

m = 10
n = 5 
ans = gcd_euclidean(m,n)
print(ans)
