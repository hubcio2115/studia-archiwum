arr = ["penis", "cipa", "hotdog", "burger"]

temp = []
for word in arr:
    temp.append(tuple([word, len(word)]))

print(temp)
