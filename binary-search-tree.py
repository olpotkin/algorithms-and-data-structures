
# Represents Nodes (Vertices) of BST
class Node(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        # Left Child - smaller than a parent, Right child - greater than a parent
        self.leftChild = None                   # Reference to the left child
        self.rightChild = None                  # Reference to the right child


class BinarySearchTree(object):
    # Constructor
    def __init__(self):
        self.root = None                        # Root node

    # Insert
    def insert(self, data):
        if not self.root:                       # If root node is empty -
            self.root = Node(data)              # - create root node
        else:
            self.insertNode(data, self.root)

    # Insert (only non-root nodes)
    # Runtime complexity - O(logN) If the tree is balanced!
    def insertNode(self, data, node):
        # Left insertion
        if data < node.data:                    # If data the smaller than parent Node
            if node.leftChild:                  # If LEFT child exists -
                # - recursively call InsertNode to the LEFT child
                self.insertNode(data, node.leftChild)
            else:                               # If left child not exists -
                node.leftChild = Node(data)     # - create new Node
        # Right insertion
        else:
            if node.rightChild:                 # If RIGHT child exists -
                # - recursively call InsertNode to the RIGHT child
                self.insertNode(data, node.rightChild)
            else:                               # If right child not exists -
                node.rightChild = Node(data)    # - create new Node

    # Remove data from BST
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

        return node

    def getPredeccessor(self, node):
        if node.rightChild:
            return self.getPredeccessor(node.rightChild)
        return node


    # Returns minimum value of the tree
    # O(logN)
    def getMinValue(self):
        # If self.root is not a None (tree is not empty)
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        # Minimum values always in the left side of the tree
        if node.leftChild:                      # if not a None
            return self.getMin(node.leftChild)  # recursive call
        return node.data

    # Returns maximum value of the tree
    # O(logN)
    def getMaxValue(self):
        # If self.root is not a None (tree is not empty)
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        # Maximum values always in the right side of the tree
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def traverse(self):
        # If tree is not empty
        if self.root:
            self.traverseInOrder(self.root)

    # O(N)
    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("{0}".format(node.data))          # Print root node of SUBTREE

        if node.rightChild:
            self.traverseInOrder(node.rightChild)


# Testing Insertion and Traverse
bst = BinarySearchTree()

bst.insert(10)                                  # root node
bst.insert(13)
bst.insert(5)
bst.insert(14)

print("Minimum value: {0}".format(bst.getMinValue()))
print("Maximum value: {0}".format(bst.getMaxValue()))
print("Numerical order:")
bst.traverse()

# Testing Deletion
bst.remove(10)
print("Numerical order:")
bst.traverse()

