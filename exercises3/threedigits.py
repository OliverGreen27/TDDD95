
n = int(input())

fac = 1
for i in range(1,n+1):
    fac *= i
    while fac % 10 == 0:
        fac //= 10
    fac %= 1000000000000

str_fac = str(fac)[-3:]
print(str_fac)