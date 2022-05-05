# from data_structures.queue import Queue
from data_structures.stack import Stack

def multi_bracket_validation(str):
    if len(str) %2 != 0:
        return False
    s = Stack()
    openers = ['(', '[', '{']
    closers = [')', ']', '}']
    matches = {'(': ')', '[': ']', '{': '}'}
    for char in str:
        if char in openers:
            s.push(char)
        elif char in closers:
            if s.is_empty():
                return False
            elif matches[s.peek()] == char:
                s.pop()
            else:
                return False
    return s.is_empty()

#methods: peek, push, pop, is_empty, top
#returns a bool
#bool shows whether or not brackets in str are balanced
