from math import sqrt

points = [
    {"x": 5, "y": 4},
    {"x": 0, "y": 0},
    {"x": 3, "y": 2},
]


def whoIsTheClosest(points: list[dict[str, int]]) -> list[int]:
    result = [0, 0]
    minimal = sqrt((points[1]["x"] - points[0]["x"])
                   ** 2 + (points[1]["y"] - points[0]["y"]) ** 2)

    for i in range(len(points)):
        for j in range(len(points)):
            current = sqrt((points[j]["x"] - points[i]["x"])
                           ** 2 + (points[j]["y"] - points[i]["y"]) ** 2)
            if current < minimal and current != 0.0:
                minimal = current
                result = [i, j]
    return result


print(whoIsTheClosest(points))
