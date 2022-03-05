db = [
    {
        "id": 1,
        "imię": "Hubert",
        "nazwisko": "Kowalski",
        "konto1": {
            "id": 1,
            "bank": "PKO",
            "saldo": 2200
        },
        "konto2": {
            "id": 2,
            "bank": "NBP",
            "saldo": 21000
        },
        "konto3": {
            "id": 3,
            "bank": "NBP",
            "saldo": 210
        }
    },
]


bank = input("Proszę podać bank: ").upper()


def sumMoney(db, bank: str):
    result = 0
    for row in db:
        for i in range(1, len(list(row.keys())[3:]) + 1):
            if row[f"konto{i}"]["bank"] == bank:
                result += row[f"konto{i}"]["saldo"]
    return result


print(sumMoney(db, bank))
