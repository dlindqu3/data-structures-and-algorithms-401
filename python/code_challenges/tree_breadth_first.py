# from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue

def breadth_first(tree):
    result = []

    if tree is None:
        return result
    if tree.root is None:
        return result

    my_q = Queue()
    my_q.enqueue(tree.root)

    while not my_q.is_empty():
        front_node = my_q.dequeue()
        result.append(front_node.value)

        if front_node.left is not None:
            my_q.enqueue(front_node.left)

        if front_node.right is not None:
            my_q.enqueue(front_node.right)
    return result
