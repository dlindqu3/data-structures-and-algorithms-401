class LinkedList:
    """
    Put docstring here
    """
    #
    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += f"{{ {str(current.value)} }} -> "
            current = current.next
        return result + "NULL"


    def insert(self, value):
        self.head = Node(value, self.head)


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
        self.next = next

class TargetError:
    pass
