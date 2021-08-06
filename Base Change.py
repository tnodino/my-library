def Base_n_to_10(x,n):
    x = str(x)
    ret = 0
    for i in range(1,len(x)+1):
        ret += int(x[-i]) * pow(n,i-1)
    return ret

def Base_10_to_n(x,n):
    y = x
    ret = ''
    while y:
        ret = str(y%n) + ret
        y //= n
    return int(ret)

def Change_eight_to_five(x):
    y = x
    ret = ''
    while y:
        if y % 10 == 8:
            ret = '5' + ret
        else:
            ret = str(y%10) + ret
        y //= 10
    return int(ret)

n,k = map(int,input().split())
if n:
    for _ in range(k):
        n = Base_n_to_10(n,8)
        n = Base_10_to_n(n,9)
        n = Change_eight_to_five(n)
print(n)