
class Node(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.height = 0                         # required to check: Does the tree need rotation or not?
        self.leftChild = None
        self.rightChild = None


class AVL(object):
    # Constructor
    def __init__(self):
        self.root = None                        # no root in the beginning

    def calcHeight(self, node):
        if not node:                            # if node is None ->
            return -1                           # -> there is no child Node: length = -1
        return node.height

    # If it returns value > 1  --> it is a LEFT HEAVY tree  --> RIGHT rotation
    # If it returns value < -1 --> it is a RIGHT HEAVY tree --> LEFT rotation
    def calcBalance(self, node):
        if not node:                            # if node is None ->
            return 0                            # -> there is leaf node
        # Calculate difference between left subtree and right subtree
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rotateRight(self, node):
        print("Rotating to the RIGHT on node {0}".format(node.data))

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def rotateLeft(self, node):
        print("Rotating to the LEFT on node {0}".format(node.data))

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1

        return tempRightChild
