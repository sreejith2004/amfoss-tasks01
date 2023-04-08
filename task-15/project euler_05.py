num = 2
while True:
    if all(num % n == 0 for n in range(1,20)):
        print(num)
        break
    else:
        num += 2
