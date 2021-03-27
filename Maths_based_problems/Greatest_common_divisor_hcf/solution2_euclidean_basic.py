def gcd_euclidean(m,n):
    # the idea is that subracting the larger from smaller ,the difference will have the same gcd as of original
    if m == 0:
        return n
    if n == 0:
        return m
    if m == n:
        return m
    if m > n :
        return gcd_euclidean(m-n,n)
    return gcd_euclidean(m,n-m)

m = 10
n = 5
ans = gcd_euclidean(m,n)
print(ans)
