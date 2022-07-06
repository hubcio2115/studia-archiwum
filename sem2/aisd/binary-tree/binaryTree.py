class Node:
    def __init__(self, key, amount=1):
        self.key = key
        self.amount = amount
        self.left = None
        self.right = None
        self.parent = None


class MyBST:
    def __init__(self):
        self.root = None

    def search(self, key):
        x = self.root
        while x != None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def insert(self, node):
        root = self.root
        father = None
        while root != None:
            father = root
            if node.key < root.key:
                root = root.left
            elif node.key > root.key:
                root = root.right
            else:
                root.amount += 1
                break
        node.parent = father
        if father == None:
            self.root = node
        else:
            if node.key < father.key:
                father.left = node
            elif node.key > father.key:
                father.right = node

    def delete(self, node):
        if(node.amount > 1):
            node.amount = node.amount - 1
        else:
            if node.left == None:
                self.transplant(node, node.right)
            elif node.right == None:
                self.transplant(node, node.left)
            else:
                y = self.minimum(node.right)
                if y.parent != node:
                    self.transplant(y, y.right)
                    y.right = node.right
                    y.right.parent = y
                self.transplant(node, y)
                y.left = node.left
                y.left.parent = y

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        else:
            if u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
        if v != None:
            v.parent = u.parent

    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def inOrderD(self, x, d, tab=[]):
        if x == None:
            return
        self.inOrderD(x.left, d + 1, tab)
        tab.append([[x.key, x.amount], d])
        self.inOrderD(x.right, d + 1, tab)
        if d == 0:
            tab.reverse()
            for i in tab:
                print(i[1] * 3 * " ", i[0])


def printTree(root, level=0):
    if root != None:
        printTree(root.left, level + 1)
        print(f"{' ' * 4 * level} -> [{root.key}, {root.amount}]")
        printTree(root.right, level + 1)
