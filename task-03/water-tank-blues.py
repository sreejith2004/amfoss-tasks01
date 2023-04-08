t = int(input())

for _ in range(t):
    n = int(input())
    tanks = list(map(int, input().split()))

    # Find the deepest tank and its index
    deepest_tank = max(tanks)
    deepest_tank_index = tanks.index(deepest_tank)

    # Transfer water from each tank above the deepest tank to the one below it
    operations = 0
    for i in range(deepest_tank_index-1, -1, -1):
        if tanks[i] > tanks[i+1]:
            operations += tanks[i] - tanks[i+1]
            tanks[i] = tanks[i+1]

    print(operations)
