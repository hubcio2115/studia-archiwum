word1 = input("Proszę wprowadzić pierwsze słowo: ")
word2 = input("Proszę wprowadzić drugie słowo: ")

temp1, temp2 = "", ""

if len(word1) < len(word2):
    temp1, temp2 = word2, word1
else:
    temp1, temp2 = word1, word2

result = ""
for i in range(len(temp2)):
    result += temp1[i] + temp2[i]
result += temp1[len(temp2):]

print(result)
