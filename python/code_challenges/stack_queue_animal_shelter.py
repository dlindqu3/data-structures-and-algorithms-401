from data_structures.queue import Queue
# from data_structures.invalid_operation_error import InvalidOperationError
# from data_structures.linked_list import Node


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal.type == 'dog':
            self.dogs.enqueue(animal)

        elif animal.type == 'cat':
            self.cats.enqueue(animal)


    def dequeue(self, pref):
        if pref == 'dog' and not self.dogs.is_empty():
            return self.dogs.dequeue()
        elif pref == 'dog' and self.dogs.is_empty():
            return None
        if pref == 'cat' and not self.cats.is_empty():
            return self.cats.dequeue()
        elif pref == 'cat' and self.cats.is_empty():
            return None

        elif pref != 'cat' and pref != 'dog':
            return None


class Dog():
    def __init__(self):
        self.type = 'dog'



class Cat():
    def __init__(self):
        self.type = 'cat'

