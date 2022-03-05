pawn = 1,
hetman = 5
isEndangered = False

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

indexesOfHetmans: list[list[int]] = []
indexOfPawn: list[int] = []

# Sprawdza jakie współrzędne ma każda figura i je zapisuje
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 5:
            indexesOfHetmans.append([i, j])
        if board[i][j] == 1:
            indexOfPawn = [i, j]

# Sprawdza czy figury znajdują się w pionie
for index in indexesOfHetmans:
    if index[0] == indexOfPawn[0]:
        isEndangered = True

# Sprawdza czy figury znajdują się w poziomie
for row in board:
    if 1 in row and 5 in row:
        isEndangered = True

# Sprawdza czy figury znajdują się po swoich przekątych
for index in indexesOfHetmans:
    if sum(indexOfPawn) == sum(index):
        isEndangered = True
    elif indexOfPawn[0] - indexOfPawn[1] == index[0] - index[1]:
        isEndangered = True

if isEndangered:
    print("Pion jest zagrożony.")
else:
    print("Pion nie jest zagrożony.")
