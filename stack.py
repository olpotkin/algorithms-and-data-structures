
class Stack(object):
    # Constructor:
    def __init__(self):
        self.stack = []                         # Empty list (for stack implementation)
        self.numOfItems = 0                     # Num of items in the stack

    # Empty list or not
    def isEmpty(self):
        return self.stack == []

    # Insert items in the stack
    def push(self, data):
        self.stack.insert(self.numOfItems, data)
        self.numOfItems += 1                    # Increase number of items

    # Return item and remove it from stack
    def pop(self):
        self.numOfItems -= 1                    # Decrement number of items
        data = self.stack.pop(self.numOfItems)
        return data

    # Return the stack size
    def stack_size(self):
        return len(self.stack)


# Testing
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.stack_size())
print(stack.pop())
print(stack.stack_size())
