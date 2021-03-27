def rearrange(A):
    # A is the given list
    # we will increment the A[i] by (A[A[i]] % n) * n
    # now after the modification of the value to get the old value A{i} % n ,and to get new value A[i]//n
    n = len(A)
    for i in range(0,n):
        A[i] += ( A[A[i]] % n ) * n

    # Now in order to get the new values
    for i in range(0,n):
        A[i] = A[i] // n
    return A


# the A[i] should range from 0 to n-1
A = [1,2,4,3,2]
ans = rearrange(A)
print(ans)