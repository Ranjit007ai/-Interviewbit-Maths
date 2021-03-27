def unique_paths(m,n):
    # m is the position of row
    # n is the position of col
    # base condition:
    if m ==0 or n == 0: # if it only row vector or column vector then there is only ONE way
        return 1
    return unique_paths(m-1,n) + unique_paths(m,n-1)

m = 2
n = 2
ans = unique_paths(m,n)
print(ans)
