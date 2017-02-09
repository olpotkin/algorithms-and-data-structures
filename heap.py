class Heap(object):

    HEAP_SIZE = 10

    # Constructor
    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):

        if self.isFull():
            print("Heap is full...")
            return
        self.currentPosition += 1               # shift current position
        self.heap[self.currentPosition] = item  # put item to new position
        self.fixUp(self.currentPosition)

    def fixUp(self, index):

        parentIndex = int((index-1)/2)

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index = parentIndex
            parentIndex = int((index-1)/2)

    def isFull(self):

        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False

    # After replacement of elements during the sorting
    def fixDown(self, index, upto):

        while index <= upto:
            leftChild = 2*index + 1
            rightChild = 2*index + 2

            if leftChild <= upto:
                childToSwap = None

                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap
            else:
                break

    # Perform O(N*logN) sorting IN PLACE!
    def heapsort(self):
        for i in range(0, self.currentPosition + 1):
            temp = self.heap[0]                 # maximum value in the root
            print("{0}".format(temp))
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition - i] = temp
            self.fixDown(0, self.currentPosition - i - 1)


# Testing
heap = Heap()

heap.insert(1)
heap.insert(71)
heap.insert(81)
heap.insert(-33)
heap.insert(4)
heap.insert(22)

heap.heapsort()
