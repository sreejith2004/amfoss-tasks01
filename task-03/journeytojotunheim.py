t = int(input())

for i in range(t):
    x = int(input())
    a, b, c = map(int, input().split())

    # check if the key for the first portal is available
    if x == 1 and (b == 1 or c == 1):
        print("YES")
    # check if the key for the second portal is available
    elif x == 2 and (a == 2 or c == 2):
        print("YES")
    # check if the key for the third portal is available
    elif x == 3 and (a == 3 or b == 3):
        print("YES")
    else:
        print("NO")
