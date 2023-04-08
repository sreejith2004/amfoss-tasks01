first = 1
second = 2
result = [second]
while True:
    fibonacci = first + second
    first = second
    second = fibonacci
    if fibonacci > 4000000:
        break
    if fibonacci % 2 == 0:
        result.append(fibonacci)
sum(result)
