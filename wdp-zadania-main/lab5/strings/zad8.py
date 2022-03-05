word1 = input("Proszę wprowadzić pierwsze słowo.")
word2 = input("Proszę wprowadzić drugie słowo.")

temp1, temp2 = "", ""

if word2 > word1:
    temp1, temp2 = word2, word1
else:
    temp1, temp2 = word1, word2

if temp2 in temp1:
    print("Tak")
else:
    print("Nie")
