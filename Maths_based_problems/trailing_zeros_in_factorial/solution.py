# this approach is not optimal ,may fail in case of large no factrials.

# function to calculate the factorial of number
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

def zeros(num):
    # factorial of num
    fact = factorial(num)
    # counting the zeros from right side of fact by dividing till remainder is zero
    count = 0
    while fact % 10 == 0 :
        fact = fact // 10
        count += 1
    return count

num = 25
ans = zeros(num)
print(ans)
 