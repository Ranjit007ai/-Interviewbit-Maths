def unique_paths(m,n):
    dp  = [[0]*n for _ in range(0,m)]
    # each position in dp show the no of way to reach their
    # now the first row and first col will be 1 ,since their is 1 way to traverse from one position to another in single row or column vector
    for row in range(0,m):
        dp[row][0] = 1
    for col in range(0,n):
        dp[0][col] = 1
    for row in range(1,m):
        for col in range(1,n):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[m-1][n-1]

m =3
n =
ans = unique_paths(m,n)
print(ans)

