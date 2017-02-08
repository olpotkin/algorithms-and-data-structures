
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


    def insert(self, data):
        self.root = self.insertNode(data, self.root)


    def insertNode(self, data, node):
        if not node:                            # if node is None ->
            return Node(data)                   # -> return new Node initialized with a given data

        if data < node.data:
            # Recursive call for left subtree
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)
        # Update the height parameter
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)


    def settleViolation(self, data, node):
        balance = self.calcBalance(node)

        # case 1: left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation...")
            return self.rotateRight(node)
        # case 2: right right heavy situation -> single left rotation
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy situation...")
            return self.rotateLeft(node)
        # case 3: Left right heavy situation
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        # case 4: Right left heavy situation
        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node



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


    def traverse(self):
        # if root node exists
        if self.root:
            self.traverseInOrder(self.root)


    def traverseInOrder(self, node):
        # If left child exists
        if node.leftChild:
            # Recursive call
            self.traverseInOrder(node.leftChild)
        print("{0}".format(node.data))
        # If right child exists
        if node.rightChild:
            self.traverseInOrder(node.rightChild)


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


    # Remove data from AVL
    def remove(self, data):
        if self.root:                           # If tree is not empty
            self.root = self.removeNode(data, self.root)


    def removeNode(self, data, node):
        if not node:                            # If node is None
            return node

        if data < node.data:                    # If item we are looking - in the LEFT subtree
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:                  # If item we are looking - in the RIGHT subtree
            node.rightChild = self.removeNode(data, node.rightChild)
        else:                                   # We are standing at the Node we need to remove

            # 1. Left child and Right child are equal to None ->
            # -> it's leaf node
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None
            # 2. Node with 1 child
            if not node.leftChild:
                print("Removing a node with single RIGHT child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node with single LEFT child...")
                tempNode = node.leftChild
                del node
                return tempNode

            # 3. Node with 2 childs
            print("Removing a node with 2 childs...")
            tempNode = self.getPredeccessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        # left left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)
        # left right heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        # right right heavy situation
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)
        # right left heavy situation
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node


# Testing
avl = AVL()

avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)

avl.traverse()

avl.remove(5)
avl.remove(4)
avl.traverse()
