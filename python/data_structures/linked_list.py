class LinkedList:
    """
    Put docstring here
    """


    def __init__(self):
        # initialization here
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += f"{{ {str(current.value)} }} -> "
            current = current.next
        return result + "NULL"


    def insert(self, value):
        if self.head == None:
             self.head = Node(value,None)
             self.tail = Node(value, None)
             self.count += 1
        elif self.head:
            next_node = self.head
            self.head = Node(value, next_node)
            self.count += 1


    def includes(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False


    def append(self, new_val):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(new_val, None)
        self.count += 1


    def insert_before(self, val, new_val):
        #add error handling
        if not self.head:
            raise TargetError

        if not self.includes(val):
            raise TargetError

        current = self.head
        new_node = Node(new_val)
        previous_node = None



        while current.value != val:
            previous_node = current
            current = current.next

        #now, current.value == val
        new_node.next = current

        #here, previous_node = node before node with matching val
        if previous_node:
            previous_node.next = new_node
            self.count += 1
        else:
            self.head = new_node
            self.count += 1


    def insert_after(self, val, new_val):
        #add error handling
        if not self.head:
            raise TargetError

        if not self.includes(val):
            raise TargetError

        current = self.head

        while current.value != val:
            current = current.next
        #now, current.value == val

        #right side of next line evaluates first
        #ends up as current -> Node -> current.next(original)
        current.next = Node(new_val, current.next)
        self.count += 1

    def kth_from_end(self, k):

        if k < 0:
            raise TargetError

        if k >= self.count:
            raise TargetError

        print('self.count', self.count)
        position = self.count - k
        current = self.head

        for i in range(position -1):
            current = current.next

        return current.value


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TargetError(BaseException):
    pass

