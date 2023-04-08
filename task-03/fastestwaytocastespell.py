n, m = map(int, input().split())

words_dict = {}
for i in range(m):
    a, b = input().split()
    words_dict[a] = a if len(a) <= len(b) else b

spell = input().split()

converted_words = []
for i in range(0, n, 2):
    word1, word2 = spell[i], spell[i+1]
    converted_words.append(words_dict[word1])
    converted_words.append(words_dict[word2])

print(" ".join(converted_words))
