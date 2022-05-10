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

    def find_maximum_value(self):
        if self.root:
            vals = self.in_order()
            max_val = vals[0]

            for num in vals:
                if num > max_val:
                    max_val = num
            return max_val

        else:
            return 'empty tree'


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
