from data_structures.stack import Stack
from data_structures.linked_list import Node

# a stack reverses order, a queue doesn't
# 2 stacks (double reverse) act like a queue

class PseudoQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, value):
        self.in_stack.push(Node(value))
        print('top of self.in_stack: ', self.in_stack.peek())

    def dequeue(self):
        while self.in_stack.top:
            temp_item = self.in_stack.pop()
            self.out_stack.push(temp_item)

        if self.out_stack.top:
            popped = self.out_stack.pop()

        while self.out_stack.top:
            temp_2 = self.out_stack.pop()
            self.in_stack.push(temp_2)
        return popped.value


