t = int(input())

while t != 0:
    n = int(input())
    l = list(map(int,input().split()))
    use_first_loop = False
    equal = 0
    count = 0
    if use_first_loop == False:
        for i in l:
            for j in l[1:] :
                if i == j:
                    equal += 1
                    l[l.index(i)]  = 0
                    print("equal = ",equal)
                use_first_loop = True
    if use_first_loop == True:
        for i in l:
            for j in l[1:] :
                if i < j:
                    count += 1
                    l[l.index(2)] = l[l.index(1)]
                    print("count = ",count)
                    use_first_loop = False

    mana = count+(equal-1)
    print(mana)
    t-=1
