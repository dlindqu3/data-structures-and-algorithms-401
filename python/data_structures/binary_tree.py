class BinaryTree:
    def __init__(self):
        self.root = None


    def pre_order(self):
        ordered_values = []
        def walk(root, values):
            if not root:
                return
            # Task 1: do something
            values.append(root.value)
            # Task 2: go left
            walk(root.left, values)
            # Task 3: go right
            walk(root.right, values)
        walk(self.root, ordered_values)
        return ordered_values

    def in_order(self):
        ordered_values = []
        def walk(root, values):
            if not root:
                return
            # Task 1: go left
            walk(root.left, values)
            # Task 2: do something
            values.append(root.value)
            # Task 3: go right
            walk(root.right, values)
        walk(self.root, ordered_values)
        return ordered_values

    def post_order(self):
        ordered_values = []
        def walk(root, values):
            if not root:
                return
            # Task 1: go left
            walk(root.left, values)
            # Task 2: go right
            walk(root.right, values)
            # Task 3: do something
            values.append(root.value)
        walk(self.root, ordered_values)
        return ordered_values

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
