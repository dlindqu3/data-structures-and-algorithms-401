from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        if not self.front:
            self.front = Node(value)
            self.rear = self.front
            return
            # return self.front.value
        temp = self.rear
        self.rear = Node(value)
        temp.next = self.rear
        return




        # elif self.front:
        #     self.rear.next

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        old_front = self.front
        self.front = old_front.next
        old_front.next = None
        return old_front.value

    def is_empty(self):
        if self.front is None:
            return True
        return False


    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
