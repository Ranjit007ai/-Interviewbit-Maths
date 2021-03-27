def binary(num):
    binary_list = []
    while num != 0:
        remainder = num % 2
        binary_list.append(str(remainder))
        num = num // 2
    binary_list.reverse()

    return ''.join(binary_list)

num = 2
ans = binary(num)
print(ans)