class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None
        self.tail = None

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
        elif self.head:
            next_node = self.head
            self.head = Node(value, next_node)


    def includes(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False


    def append(self, new_val):
        pass


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
        else:
            self.head = new_node


    def insert_after(self, val, new_val):
        #add error handling
        current = self.head

        while current.value != val:
            current = current.next
        #right side of next line evaluates first
        current.next = Node(new_val, current.next)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TargetError(BaseException):
    pass

