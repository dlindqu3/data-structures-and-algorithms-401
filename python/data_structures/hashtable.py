from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    ## in the assignment on Canvas, it asks for these methods:
        ## set
        ##get
        ##contains
        ##keys
        ##hash

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.buckets = [None] * self.size


    def set(self, key, val):
        index = self.hash(key)
        # if self.buckets[index] == None:
        #     return None
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()
        bucket = self.buckets[index]
        # if bucket is None:
        #     self.buckets[index] = bucket
        # add: handle updates vs adds
        bucket.insert([key, val])


    def get(self, key):
        index = self.hash(key)
        if not self.buckets[index]:
            return None
        bucket = self.buckets[index]

        current = bucket.head
        ## current is the head of the linked list, which is a node that is a pair of data
        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]
            current = current.next
        return None

    def contains(self, key):
        ## return a boolean of whether given key is in the table
        return bool(self.get(key))

    def keys(self):
        ## return all keys in the table
        all_keys = set()
        for item in self.buckets:
            if item:
                current_node = item.head
                while current_node:
                    all_keys.add(current_node.value[0])
                    current_node = current_node.next
        return all_keys

    def hash(self, key):
        sum_of_chars = 0
        for char in key:
            sum_of_chars += ord(char)
        primed = sum_of_chars * 971
        index = primed % self.size
        return index

