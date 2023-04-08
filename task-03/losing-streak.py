n, m = map(int, input().split())

rounds = 0

while m != n:
    if m // 2 >= n and m // 2 * 2 != m:
        m //= 2
    elif m // 3 >= n and m // 3 * 3 != m:
        m //= 3
    else:
        rounds = -1
        break
    rounds += 1

print(rounds)
