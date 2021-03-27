# given the string ,we need to convert to the number
# ex :'AA'-27,'B':2
def excel(S):
    # S is the string
    result = 0
    for i in range(0,len(S)):
        result *= 26
        result += (ord(S[i]) - ord('A') + 1) 
    return result

S = 'Z'
ans = excel(S)
print(ans)