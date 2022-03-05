def program():
    ifBreak = input("Czy chcesz zakończyć program? (t/n): ")

    if ifBreak == "t":
        return 0

    program()


program()
