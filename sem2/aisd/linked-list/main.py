from linkedList import LinkedList, Node, merge

if __name__ == "__main__":

    temp = [Node("1"), Node("2"), Node("3")]

    myList1 = LinkedList()
    myList2 = LinkedList()

    # for node in temp:
    #     myList1.prepend(node)
    #     myList2.prepend(node)

    myList3 = merge(myList1, myList2)

    myList3.listPrint()
    myList1.listPrint()
    myList2.listPrint()
