from data_structures.linked_list import LinkedList, Node

def zip_lists(a, b):
    result = LinkedList()

    current_a = a.head
    current_b = b.head

    if current_a == None:
        return b
    elif current_b == None:
        return a

    while current_a and current_b:
        result.append(current_a.value)
        current_a = current_a.next
        result.append(current_b.value)
        current_b = current_b.next
    while current_a:
        result.append(current_a.value)
        current_a = current_a.next
    while current_b:
        result.append(current_b.value)
        current_b = current_b.next

    return result






