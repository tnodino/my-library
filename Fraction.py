mod = 10 ** 9 + 7
a = int(input())
b = int(input())
print(a * pow(b,mod-2,mod) % mod)

# a / b = a * pow(b,mod-2,mod) % mod