def zeros(n):
    count = 0
    # keep dividing the number by power of 5 and update the count
    i = 5
    while(n//i >= 1):
        count += int(n/i)
        i *= 5
    return int(count)

num = 26
ans = zeros(num)
print(ans)