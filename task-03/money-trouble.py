n, m = map(int, input().split())

# check if x is a whole number
if n % m != 0:
    print(-1)
else:
    x = n // m
    # check if we can make up the total amount using only 1's and 2's
    if x % 2 == 0:
        print(x // 2 * m)
    elif n >= 5:
        print(x // 2 * m + 1)
    else:
        print(-1)
