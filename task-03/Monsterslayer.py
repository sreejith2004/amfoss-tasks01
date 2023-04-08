t = int(input())

for i in range(t):
    n = int(input())
    healths = list(map(int, input().split()))

    # debuff the monsters using the spell
    while True:
        debuffed = False
        for j in range(1, n):
            if healths[j] > 0 and healths[j-1] > 0:
                diff = healths[j-1] - healths[j]
                if diff >= 0:
                    healths[j-1] -= healths[j]
                    healths[j] = 0
                    debuffed = True
                else:
                    healths[j] -= healths[j-1]
                    healths[j-1] = 0
                    debuffed = True
        if not debuffed:
            break

    # check if all monsters have been defeated
    for j in range(n):
        if healths[j] > 0:
            # use the sword to kill the remaining monster
            healths[j] = 0
            break

    # output the result
    if all(h == 0 for h in healths):
        print("YES")
    else:
        print("NO")
