min_value = 100 * 100
max_value = 999 * 999
palindromes = []


for number in range(min_value, max_value):
    if str(number) == str(number)[::-1]:
        palindromes.append(number)

result = []
for number in palindromes:
    for i in range(100,1000):
        if number % i == 0 and len(str(int(number/i))) == 3:
            result.append(number)

max(result)
