sentence = input("Proszę podać zdanie: ")

polishSignDict = {
    "ą": "a",
    "ć": "c",
    "ę": "e",
    "ł": "l",
    "ń": "n",
    "ś": "s",
    "ó": "o",
    "ź": "z",
    "ż": "z"
}

polishSigns = list(polishSignDict.keys())

if sentence.isalpha():
    pass
else:
    temp = ""
    for sign in sentence:
        if sign in polishSigns:
            temp = sentence.replace(sign, polishSignDict[sign])

    print(temp)
