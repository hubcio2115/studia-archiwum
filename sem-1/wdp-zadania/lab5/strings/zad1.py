word1 = input("Proszę podać pierwsze słowo: ")
word2 = input("Proszę podać drugie słowo: ")

if word1 == word2:
    print("Słowa są takie same, więc mają tą samą długość.")
if word1 > word2:
    print("Słowo pierwsze jest prędzej w porządku leksykograficznym.")
else:
    print("Słowo drugie jest prędzej w porządku leksykograficznym.")

if len(word1) > len(word2):
    print("Słowo pierwsze jest dłuższe od słowa drugiego.")
else:
    print("Słowo drugie jest dłuższe od słowa pierwszego.")
