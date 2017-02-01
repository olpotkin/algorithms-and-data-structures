
class Node(object):

    # Constructor
    def __init__(self, data):
        self.data = data                        # Data (could be different type)
        self.nextNode = None                    # Reference to the next node


class LinkedList(object):

    # Constructor
    def __init__(self):
        self.head = None                        # First node of the linked list
        self.size = 0                           # Size = 0 in the begining

    # Insert data in the beginning of the list
    # Complexity - O(1)
    def insertStart(self, data):
        self.size += 1                          # Increment the Size
        newNode = Node(data)                    # Initiate new Node

        if not self.head:                       # if insert first element
            self.head = newNode
        else:                                   # else - update pointers
            newNode.nextNode = self.head        # if insert not first element (some element/s already exist)
            self.head = newNode

    # Remove element from list
    # O(N)
    def remove(self, data):

        if self.head is None:                   # if list is empty - return
            return

        self.size -= 1
        currentNode = self.head
        previousNode = None                     # None - in the beginning

        while currentNode.data != data:         # Find element - update nodes
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    # O(1)
    # Already store reference to size
    def size1(self):
        return self.size

    # O(N) - not good!
    def size2(self):

        actualNode = self.head
        size = 0

        while actualNode is not None:           # Going through all list
            size += 1
            actualNode = actualNode.nextNode

        return size

    # Insert node at the end of list
    # O(N)
    def insertEnd(self, data):

        self.size += 1                          # Increment list size
        newNode = Node(data)                    # Init. new node
        actualNode = self.head                  # Get actual node (head of the list)

        while actualNode.nextNode is not None:  # Looking for the end of list
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode           # Update pointer of last node to newNode. Now newNode is the last.

    # Print all list's source
    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print "{0} ".format(actualNode.data)
            actualNode = actualNode.nextNode


# Test all linked list structure
linked_list = LinkedList()

linked_list.insertStart(12)
linked_list.insertStart(122)
linked_list.insertStart(3)
linked_list.insertEnd(31)

linked_list.traverseList()
print linked_list.size1()

linked_list.remove(31)
linked_list.remove(12)
linked_list.remove(122)
linked_list.remove(3)
print linked_list.size1()

