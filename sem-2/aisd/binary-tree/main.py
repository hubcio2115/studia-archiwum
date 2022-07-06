from binaryTree import Node, MyBST, printTree

if __name__ == "__main__":
    tree = MyBST()

    tree.insert(Node("jeden"))
    tree.insert(Node("dwa"))
    tree.insert(Node("trzy"))
    tree.insert(Node("cztery"))
    tree.insert(Node("cztery"))
    tree.insert(Node("jeden"))
    tree.insert(Node("dwa"))

    print(tree.search("dwa").key + ", " + str(tree.search("dwa").amount))

    printTree(tree.root)

    tree.delete(tree.search("dwa"))
    tree.delete(tree.search("cztery"))
    tree.delete(tree.search("cztery"))

    print()
    printTree(tree.root)
