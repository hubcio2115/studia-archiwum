dates = [
    {
        "day": 29,
        "month": 8,
        "year": 2001
    },
    {
        "day": 3,
        "month": 1,
        "year": 2022
    },
    {
        "day": 1,
        "month": 1,
        "year": 2015
    }
]


def sortDates(dates: list[dict[str, int]]) -> list[dict[str, int]]:
    sortedDates = dates

    for i in range(len(dates)-1):
        current = dates[i]["year"]
        next = dates[i + 1]["year"]

        if current > next:
            sortedDates[i], sortedDates[i +
                                        1] = sortedDates[i + 1], sortedDates[i]
        elif current == next:
            current = dates[i]["month"]
            next = dates[i + 1]["month"]

            if current > next:
                sortedDates[i], sortedDates[i +
                                            1] = sortedDates[i + 1], sortedDates[i]
            elif current == next:
                current = dates[i]["day"]
                next = dates[i + 1]["day"]

                if current > next:
                    sortedDates[i], sortedDates[i +
                                                1] = sortedDates[i + 1], sortedDates[i]

    return sortedDates


print(sortDates(dates))
