class LinkedList:
    """
    Put docstring here
    """
    #
    def __init__(self):
        # initialization here
        self.head = None

    def insert(self, value):
        self.head = Node(value)



    def to_string(self):
        pass

    def includes(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = None

class TargetError:
    pass
